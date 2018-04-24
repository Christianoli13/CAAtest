from django import forms
from .models import dadosaluno, disciplina, respostas
from django.forms.widgets import RadioSelect


class Nomeform(forms.ModelForm):
    def __init__(self, curso_id, *args, **kwargs):
        super(Nomeform, self).__init__(*args, **kwargs)
        self.fields['materias'].queryset = disciplina.objects.filter(Cursoo__id=curso_id)
    class Meta:
        model = dadosaluno
        fields = ['Nome', 'materias',]

class Questionarioform1(forms.ModelForm):
        class Meta:
            model = respostas
            fields =['pergunta1', 'pergunta2', 'pergunta3']

class Questionarioform2(forms.ModelForm):
    class Meta:
        model = respostas
        fields = ['pergunta4', 'pergunta5', 'pergunta6', 'pergunta7','pergunta8']

class Questionarioform3(forms.ModelForm):
    class Meta:
        model = respostas
        fields = ['pergunta9', 'pergunta10', 'pergunta11', 'pergunta12', 'pergunta13']

class Questionarioform4(forms.ModelForm):
    class Meta:
        model = respostas
        fields = ['pergunta14', 'pergunta15', 'pergunta16', 'pergunta17', 'pergunta18', 'pergunta19', 'pergunta20', 'pergunta21']

class Questionarioform5(forms.ModelForm):
    class Meta:
        model = respostas
        fields = ['pergunta22', 'pergunta23']

class Questionarioform6(forms.ModelForm):
    class Meta:
        model = respostas
        fields = ['pergunta24', 'pergunta25', 'pergunta26', 'pergunta27']

class Questionarioform7(forms.ModelForm):
    class Meta:
        model = respostas
        fields = ['pergunta28', 'pergunta29', 'pergunta30', 'pergunta31', 'pergunta32', 'pergunta33', 'pergunta34', 'pergunta35']

class Questionarioformsugest(forms.ModelForm):
    class Meta:
        model = respostas
        fields = ['Sugestão']