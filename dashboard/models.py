from django.db import models

# Create your models here.

class emailMarketing(models.Model):
    email = models.EmailField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    class Meta:
        verbose_name_plural = 'emailMarketing'

class urlRedirects(models.Model):
    urlstring1 = models.TextField(blank=True, null=True)        
    urlstring2 = models.TextField(blank=True, null=True)        
    urlstring3 = models.TextField(blank=True, null=True)        
    urlstring4 = models.TextField(blank=True, null=True)        
    urlstring5 = models.TextField(blank=True, null=True)        
        
class imageControls(models.Model):
    image1 = models.ImageField(upload_to="dashboard", height_field=None, width_field=None, max_length=None, blank=True, null=True, default="") 
    alt1 = models.TextField(blank=True, null=True, max_length=120, default="")  
    description1 = models.TextField(blank=True, null=True, default="") 
    
    image2 = models.ImageField(upload_to="dashboard", height_field=None, width_field=None, max_length=None, blank=True, null=True, default="") 
    alt2 = models.TextField(blank=True, null=True, max_length=120, default="")  
    description2 = models.TextField(blank=True, null=True, default="") 
    
    image3 = models.ImageField(upload_to="dashboard", height_field=None, width_field=None, max_length=None, blank=True, null=True, default="") 
    alt3 = models.TextField(blank=True, null=True, max_length=120, default="")  
    description3 = models.TextField(blank=True, null=True, default="") 
    
    image4 = models.ImageField(upload_to="dashboard", height_field=None, width_field=None, max_length=None, blank=True, null=True, default="") 
    alt4 = models.TextField(blank=True, null=True, max_length=120, default="")  
    description4 = models.TextField(blank=True, null=True, default="") 
    
    image5 = models.ImageField(upload_to="dashboard", height_field=None, width_field=None, max_length=None, blank=True, null=True, default="") 
    alt5 = models.TextField(blank=True, null=True, max_length=120, default="")  
    description5 = models.TextField(blank=True, null=True, default="") 
    
    image6 = models.ImageField(upload_to="dashboard", height_field=None, width_field=None, max_length=None, blank=True, null=True, default="") 
    alt6 = models.TextField(blank=True, null=True, max_length=120, default="")  
    description6 = models.TextField(blank=True, null=True, default="") 

    def __str__(self):
        return self.alt1
    class Meta:
        verbose_name_plural = 'imageControl'
        
class searchControl(models.Model):
    query = models.TextField(blank=True, null=True)        
    ip_address = models.TextField(blank=True, null=True)        
    
class accountsControl(models.Model):
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=50)
    
    def __str__(self):
        return self.email
    class Meta:
        verbose_name_plural = 'accountControl'
