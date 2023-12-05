from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=200)
    description = models.TextField()
    company_bgimg = models.ImageField(blank=True)
    company_logotip = models.ImageField(blank=True)
    company_location = models.CharField(max_length=500,blank=True)
    company_location_link = models.CharField(max_length=300,blank=True)
    company_phone_number = models.CharField(max_length=20,blank=True)
    company_telegram_link = models.CharField(max_length=300,blank=True)
    company_instagram_link = models.CharField(max_length=300,blank=True)


    def __str__(self):
        return self.company_name

class Company_photo(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='company_photo_set')
    photo = models.ImageField()

    def __str__(self):
        return f"{self.company} photo {self.pk} "


