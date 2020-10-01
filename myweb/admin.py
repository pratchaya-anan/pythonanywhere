from django.contrib import admin
# from .models import AllProduct, PhotoPattern

# Register your models here.
# admin.site.register(AllProduct)
# admin.site.register(PhotoPattern)




















from .models import Question, Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)