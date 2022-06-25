from django.db import models
# Create your models here.
class Artisans(models.Model):
	#user = models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE)
        artisan_name = models.CharField(max_length=200, null=True)
        artisan_email = models.CharField(max_length=200)
        artisan_phno = models.IntegerField(max_length=200, null=True)
        company_name = models.CharField(max_length=200, null=True)
        zip_code = models.IntegerField(max_length=200, null=True)
        company_address = models.CharField(max_length=200, null=True)
        password = models.CharField(max_length=200, null=True)

  
        def register(self):
            return self.save()
        def __str__(self):
            return self.artisan_name
