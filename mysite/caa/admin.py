from django.contrib import admin
from .models import dadosaluno, cursos, disciplina, respostas
# Register your models here.

admin.site.register(dadosaluno)
admin.site.register(cursos)
admin.site.register(disciplina)
admin.site.register(respostas)