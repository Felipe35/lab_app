from django.views.generic import View, ListView
# from django.views.generic.list import ListView
# from django_filters.views import FilterView
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseRedirect
# from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login




from .models import Patient, File
from .forms import LogForm, FileForm, PatientForm
from .filters import PatientFilter, FileFilter


class LogingView(View):
    template_name = "lab_app/login.html"
    form_class = LogForm

    def get(self, request):
        form = self.form_class()
        message = ""
        return render(request, self.template_name, context={"form": form,"message": message})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data["user_name"],
                password = form.cleaned_data["password"]
            )

            if user is not None:
                login(request, user)
                return redirect("/patient_list")
            message = "Contraseña y Usuario incorrectos"
            return render(request, self.template_name, context={"form": form, "message": message})
           


class EmpListView(ListView):
    queryset = Patient.objects.all()
    template_name = "lab_app/patient_list.html"
    model = Patient
    context_object_name = "patients"
    paginate_by = 10
    ordering = ["-date"]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PatientFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_patients = Patient.objects.all()
    
        # last_ten = Patient.objects.all().order_by("-id")[:3] 
        '''This query could be implemented in future..'''
        
        context["total_patients"] = all_patients.count()
        # context["last_three"] = last_ten
        '''This query could be implemented in future..'''
        context['form'] = self.filterset.form
        return context


class PatientFileListView(ListView):
    queryset = File.objects.all()
    template_name = "lab_app/files_list.html"
    model = File
    ordering = ["id"]
    context_object_name = "files"
    paginate_by = 10


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = FileFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # all_patients = File.objects.all()
    
        # last_ten = Patient.objects.all().order_by("-id")[:3] 
        '''This query could be implemented in future..'''
        
        # context["last_three"] = last_ten
        '''This query could be implemented in future..'''
        context['form'] = self.filterset.form
        return context
    
    # def get_queryset(self):
    #     filter_val = self.request.GET.get('filter', 1)
        
        
    #     if str(filter_val).isdigit():
    #         new_context = File.objects.filter(patient=filter_val)

    #         return new_context
                    

class FileView(View):
    def get(self, request, id=0):
    
        if id:
            files = File.objects.get(pk=id)

        return render(request, "lab_app/files.html", {
            "file": files,
        })
    

class LabIndexView(View):
   
    def get(self, request, id=0):
        
        if id == 0:
           
            form = PatientForm()
        else:
            patient = Patient.objects.get(pk=id)
           
            form = PatientForm(instance=patient)
           
            
        return render(request, "lab_app/employee_form.html",{
                "form": form,
                
                })
    
    def post(self, request, id=0):
        
        if id == 0:
            form = PatientForm(request.POST)

        else:
            patient = Patient.objects.get(pk=id)
            form = PatientForm(request.POST, instance=patient)

        if form.is_valid():
            form.save()
            return redirect("/patient_list")
       
        return render(request, "lab_app/employee_form.html", {
            "form": form
        })


class SearchView(View):
    def get(self, request):
   
        form_file = FileForm()

        return render(request, "lab_app/file_form.html", {
            "file_form": form_file
        })
    

    def post(self, request):
    
        submitted_form = FileForm(request.POST, request.FILES)
        patient_id = request.POST["patient"]
       
        check_id = Patient.objects.filter(pk=patient_id).exists()
       

        if check_id == True and submitted_form.is_valid():

            get_id = Patient.objects.get(pk=patient_id)
        
            File.objects.create(patient=get_id, user_file=request.FILES["user_file"])

            return redirect("/patient-files-list")

        else:
            return render(request,"lab_app/file_form.html", {
                "file_form": submitted_form,
                "status_id": f"El paciente con ID {patient_id} no existe"
                })


class InvalidIdView(View):
    def get(self, request):
        return render(request,"lab_app/invalid_id.html", {
            "status":"upss an error"
        })
    

class PatientDeleteView(View):
    def post(self, request, id):
        patient = Patient.objects.get(pk=id)
        patient.delete()
        return redirect("/patient_list")
