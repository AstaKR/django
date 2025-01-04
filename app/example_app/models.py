from django.db import models

# Create your models here.

class CategoryModels(models.Model):
    Category_no = models.IntegerField(unique=True)
    Category_name = models.CharField(max_length=50)
    Link_details = models.CharField(max_length=500, null=True,blank=True)
    Active = models.BooleanField()

class SubCategoryModels(models.Model):
    SubCategory_no = models.IntegerField(unique=True)
    SubCategory_name= models.CharField(max_length=50)
    category = models.ForeignKey("CategoryModels", on_delete=models.CASCADE)
    Link_details = models.CharField(max_length=500,blank=True, null=True)
    Active=models.BooleanField()





    