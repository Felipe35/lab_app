from django.urls import path
from django.contrib.auth.decorators import login_required


from . import views

# urlpatterns = [
#     # --LOGIN
#     path("", views.LogingView.as_view(), name="login"),

#     # Patient List
#     path("employe_insert", views.LabIndexView.as_view(), name='employe_insert'),
#     path("<int:id>/", views.LabIndexView.as_view(), name="employe_update"),
#     # path("patient_list", views.SearchPatientListView.as_view(), name='patient_list'),
#     path("patient_list", views.EmpListView.as_view(), name='patient_list'),
#     # Delete
#     path("<int:id>", views.PatientDeleteView.as_view(), name="patient_delete"),
#     path("patient-upload", views.SearchView.as_view(), name="upload"),

#     # File Patients
#     path("patient-files-list/<int:id>", views.FileView.as_view(), name="file_view"),
#     path("patient-files-list", views.PatientFileListView.as_view(), name='patient-files-list'),

#     # Invalid id in Files Upload
#     path("invalid_id", views.InvalidIdView.as_view(), name="invalid_id")
   
    
# ]

urlpatterns = [
    # --LOGIN
    path("", views.LogingView.as_view(), name="login"),
    # Patient List
    path("patient_list", views.EmpListView.as_view(), name='patient_list'),
    path("employe_insert", views.LabIndexView.as_view(), name='employe_insert'),
    path("<int:id>/", views.LabIndexView.as_view(), name="employe_update"),
    # Delete
    path("<int:id>", views.PatientDeleteView.as_view(), name="patient_delete"),
    path("patient-upload", views.SearchView.as_view(), name="upload"),

    # File Patients
    path("patient-files-list/<int:id>", views.FileView.as_view(), name="file_view"),
    path("patient-files-list", views.PatientFileListView.as_view(), name='patient-files-list'),

    # Invalid id in Files Upload
    path("invalid_id", views.InvalidIdView.as_view(), name="invalid_id")
   
    
]

# BEFORE

# urlpatterns = [
#     # --LOGIN
#     path("", views.LogingView.as_view(), name="login"),

#     # Patient List
#     path("employe_insert", views.LabIndexView.as_view(), name='employe_insert'),
#     path("<int:id>/", views.LabIndexView.as_view(), name="employe_update"),
#     path("patient_list", views.EmpListView.as_view(), name='patient_list'),
#     # Delete
#     path("<int:id>", views.PatientDeleteView.as_view(), name="patient_delete"),
#     path("patient-upload", views.SearchView.as_view(), name="upload"),

#     # File Patients
#     path("patient-files-list/<int:id>", views.FileView.as_view(), name="file_view"),
#     path("patient-files-list", views.PatientFileListView.as_view(), name='patient-files-list'),

#     # Invalid id in Files Upload
#     path("invalid_id", views.InvalidIdView.as_view(), name="invalid_id")
   
    
# ]
