from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .forms import Nomeform, Questionarioform1, Questionarioform2, Questionarioform3, Questionarioform4, Questionarioform5, Questionarioform6, Questionarioform7
from .models import cursos, dadosaluno, disciplina

def index(request):
    curso=cursos.objects.all()
    return render(request, 'index.html', {'cursos': curso})

def dados(request, curso_id):
    if request.method == 'POST':
         form = Nomeform(curso_id, request.POST)
         if form.is_valid():
             data = form.save()
             return HttpResponseRedirect("/caa/%s/formularios/" % (data.id))
    else:
        form = Nomeform(curso_id)
    return render(request, 'Iniciar.html', {'form': form}, )

def formularios(request, dadosaluno_id):
    aluno=dadosaluno.objects.get(id=dadosaluno_id)
    materia=aluno.materias.all()
    return render(request, 'formularios.html', {'materias': materia,
                                                'aluno' : aluno.id})

def questionario(request, dadosaluno_id, disciplina_id):
    disc=disciplina.objects.get(id=disciplina_id)
    materia=disc.nome
    if request.method == 'POST':
         form1 = Questionarioform1(request.POST)
         form2 = Questionarioform2(request.POST)
         form3 = Questionarioform3(request.POST)
         form4 = Questionarioform4(request.POST)
         form5 = Questionarioform5(request.POST)
         form6 = Questionarioform6(request.POST)
         form7 = Questionarioform7(request.POST)
         if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid() and form7.is_valid():
             data1 = form1.save(commit=False)
             data1.código=disc
             data1.Curso=disc.Cursoo
             data1.nome=dadosaluno.objects.get(id=dadosaluno_id)
             data1.save()
             data2 = form2.save(commit=False)
             data2.código = disc
             data2.Curso = disc.Cursoo
             data2.nome = dadosaluno.objects.get(id=dadosaluno_id)
             data2.save()
             data3 = form3.save(commit=False)
             data3.código = disc
             data3.Curso = disc.Cursoo
             data3.nome = dadosaluno.objects.get(id=dadosaluno_id)
             data3.save()
             data4 = form4.save(commit=False)
             data4.código = disc
             data4.Curso = disc.Cursoo
             data4.nome = dadosaluno.objects.get(id=dadosaluno_id)
             data4.save()
             data5 = form5.save(commit=False)
             data5.código = disc
             data5.Curso = disc.Cursoo
             data5.nome = dadosaluno.objects.get(id=dadosaluno_id)
             data5.save()
             data6 = form6.save(commit=False)
             data6.código = disc
             data6.Curso = disc.Cursoo
             data6.nome = dadosaluno.objects.get(id=dadosaluno_id)
             data6.save()
             data7 = form7.save(commit=False)
             data7.código = disc
             data7.Curso = disc.Cursoo
             data7.nome = dadosaluno.objects.get(id=dadosaluno_id)
             data7.save()
             return HttpResponseRedirect("/caa/%s/formularios/" % (dadosaluno_id))
    else:
        form1 = Questionarioform1
        form2 = Questionarioform2
        form3 = Questionarioform3
        form4 = Questionarioform4
        form5 = Questionarioform5
        form6 = Questionarioform6
        form7 = Questionarioform7
    return render(request, 'questionario.html', {'form1': form1,
                                                 'form2': form2,
                                                 'form3': form3,
                                                 'form4': form4,
                                                 'form5': form5,
                                                 'form6': form6,
                                                 'form7': form7,
                                                'disciplina': materia
                                                 })