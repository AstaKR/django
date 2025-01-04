from django.contrib import admin

from bi_servers.models import CategoryModels,SubCategoryModels

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display =["Category_no", "Category_name", "Active"]

class SubCategoryAdmin(admin.ModelAdmin):
    list_display =["SubCategory_no", "SubCategory_name", "Active"]


admin.site.register(CategoryModels, CategoryAdmin)
admin.site.register(SubCategoryModels, SubCategoryAdmin)
