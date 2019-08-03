from django.contrib import admin

# Register your models here.
from .models import Researcher, Author, Paper, Category, Classification

admin.site.register(Researcher)
admin.site.register(Author)
admin.site.register(Paper)
admin.site.register(Category)
admin.site.register(Classification)
