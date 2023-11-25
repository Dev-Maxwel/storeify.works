from django.db import models

# Create your models here.

class emailMarketing(models.Model):
    email = models.EmailField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class imageControls(models.Model):
    image1 = models.ImageField(upload_to="storeifyworks_cdn", height_field=None, width_field=None, max_length=None, blank=True, null=True) 
    alt1 = models.TextField(blank=True, null=True, max_length=120)  
    description1 = models.TextField(blank=True, null=True) 
    
    image2 = models.ImageField(upload_to="storeifyworks_cdn", height_field=None, width_field=None, max_length=None, blank=True, null=True) 
    alt2 = models.TextField(blank=True, null=True, max_length=120)  
    description2 = models.TextField(blank=True, null=True) 
    
    image3 = models.ImageField(upload_to="storeifyworks_cdn", height_field=None, width_field=None, max_length=None, blank=True, null=True) 
    alt3 = models.TextField(blank=True, null=True, max_length=120)  
    description3 = models.TextField(blank=True, null=True) 
    
    image4 = models.ImageField(upload_to="storeifyworks_cdn", height_field=None, width_field=None, max_length=None, blank=True, null=True) 
    alt4 = models.TextField(blank=True, null=True, max_length=120)  
    description4 = models.TextField(blank=True, null=True) 
    
    image5 = models.ImageField(upload_to="storeifyworks_cdn", height_field=None, width_field=None, max_length=None, blank=True, null=True) 
    alt5 = models.TextField(blank=True, null=True, max_length=120)  
    description5 = models.TextField(blank=True, null=True) 
    
    image6 = models.ImageField(upload_to="storeifyworks_cdn", height_field=None, width_field=None, max_length=None, blank=True, null=True) 
    alt6 = models.TextField(blank=True, null=True, max_length=120)  
    description6 = models.TextField(blank=True, null=True) 

    