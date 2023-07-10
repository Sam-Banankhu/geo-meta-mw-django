from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    class Meta:
        app_label = 'api'

class District(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        app_label = 'api'

class City(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'api'
