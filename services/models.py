from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()


    def __str__(self):
        return f"{self.name}"

    def name_string(self):
        return str(self.name)

class Service_photo(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE,related_name="ser_ph_set")
    photo = models.ImageField()

    def __str__(self):
        return f"{self.service.name} ning rasmi"