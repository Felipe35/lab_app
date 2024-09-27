##Introduction
This is a Monolith CRUD web applications that fix some issues on
a small laboratory business using Django as framework.

###Why is the reason of this we app?
The main goal is to solve few things that the laboratory had, as part
of data base management, pdf file storing, dependence on the use of
excel. One of the main problems of this laboratory is the amount of
hard steps to view a pdf file per patient in their data base.

Because the laboratory was using excel for their db, they could create
urls inside of the db excel per patient link to some files in their
disk and then, from there they can clik on the pdf files they need
to view. This proccess was laborious and a better aproach was taken.

The laboratory also have some potential improvments in the future
that I think I can solve latter. Such as: create a form to write
their laboratory results and so on.

###What the app can do?
The application is capable to CRUD "create, read, update, delete" the data base in a user friendly way, also
provides with a basic navegation to go around urls that can do
few operations.
- Here an example:

![](https://ibb.co/CQVsB5V)

Ofcourse the application handles well basic errors of typing, and
does not allow to leave few inputs in blank.

![](https://ibb.co/2dq62XQ)

Styling was important but not to much. Using Bootstrap and CSS was
really enough to achive what this application needs. 

###About DataBase
- One to many relation tables.
- Tables with 2nd normal form.
- SQLite3 db
- Tables (Files - Patients)

In conclusion the data base implementation was simple, due to the needs. The CRUD desing was mainly integrate with the respective tables using JOIN clause to work with them. Another features were added, such as filters to get data to a corresponding input.

### About Views
Views were implemented by class view. At start stage, functions were
implemented but then, was really need to change to something more
abstract and less code, and that's where class view can do.

- Django View Sample: Fecth data and list it to the browser.

```python
class PatientFileListView(ListView):
    queryset = File.objects.all()
    template_name = "lab_app/files_list.html"
    model = File
    ordering = ["id"]
    context_object_name = "files"
    paginate_by = 200

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = FileFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
      
        context['form'] = self.filterset.form
        return context
```
###About Templates
Separete html files were split into Django templates to work better and
have better understanding as well as the elimination of having all files
in one place. Loops and if else statments played really well when 
presenting data organized and concise

###About Uploads
Django provides with images and files uploading system that can
fecth through the upload file system path. The settings as well as
the urls.py were setting up in a secure way to protect and display
pdf files on this case.s

###Problems
The application have few problems that later will be implemented.

Because only one person will use this program, it will be ok for the moment.

- User authentication: Although the application has a login page
and does not allow to view other urls without passing the user
and passwords correct; if I know the urls path I can navigate to
the application
- Pagination: Although the application has pagination, it will need
in the future to have infinity pagination. However because is a 
really small laboratory the pagination on this stage is ok but not
effucient. A pagination of 100 per page was giving base on the amount
of records thye used to have per year.

Conclusion
This is in general of what the application can do, and only does
what the company really wanted to do, without using extra features
that they do not need. Later, new implementations will be added
to keep removing the need of using excel as a program. To mention
that the application will be running in AWS in a free tier, using
PostgreSQL.

###Technologies
Using Python Django Framework, HTML, CSS, to work on the backend 
and basic frontend.
