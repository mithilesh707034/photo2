from django.db import models

# Create your models here.
from django.db import models

class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=200,default='')
    name = models.CharField(max_length=200)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='uploads',default='')
    
    def __str__(self):
        return self.name

class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads')
    
    def __str__(self):
        return f"Image for {self.portfolio.name}"
    


class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads')

    def __str__(self):
        return self.name