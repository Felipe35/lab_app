from django.db import models
from django.urls import reverse
from phone_field import PhoneField
# from django.core.validators import RegexValidator


# Create your models here.
class Login(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)



class Patient(models.Model):
    
    full_name = models.CharField(max_length=150, null=True)
    age = models.PositiveIntegerField(null=True)
    date = models.DateField(auto_now=True)
    address = models.CharField(max_length=250, null=True)
    p_number = PhoneField(blank=True) # Validators should be a list
    s_number = PhoneField(blank=True)

    slug = models.SlugField(default="", blank=True, null=False, db_index=True)


    class Meta:
        verbose_name_plural = "Patient Entries"

    def __str__(self):
        return f"{self.full_name}"
    
    def get_absolute_url(self):
        return reverse("employe_update", kwargs={self.slug})
    

    
class File(models.Model):
    user_file = models.FileField(upload_to="files", null=True)
    date = models.DateField(auto_now=True)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE, null=True, related_name="files")

    class Meta:
        verbose_name_plural = "File Entries"

    def __str__(self):
        return f"{self.user_file}"
    
    

    