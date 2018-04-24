from django.db import models

class cursos(models.Model):
    cursos=models.CharField(max_length=150)
    def __str__(self):
        return self.cursos
class disciplina(models.Model):
    Cursoo = models.ForeignKey(cursos, on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    código = models.CharField(max_length=150)
    def __str__(self):
        return self.nome
class dadosaluno(models.Model):
    Nome = models.CharField(max_length=150)
    materias=models.ManyToManyField(disciplina)
    def __str__(self):
        return  self.Nome

class respostas(models.Model):
    Curso=models.ForeignKey(cursos, on_delete=models.CASCADE)
    nome=models.ForeignKey(dadosaluno, on_delete=models.CASCADE)
    código=models.ForeignKey(disciplina, on_delete=models.CASCADE)
    resp1= (
        ('Prefiro não opinar', 'Prefiro não opinar'),
        ('Muito fraco', 'Muito fraco'),
        ('Fraco', 'Fraco'),
        ('Regular', 'Regular'),
        ('Bom', 'Bom'),
        ('Excelente', 'Excelente'),
    )
    resp2= (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
        ('Em parte', 'Em parte'),
    )
    resp3= (
        ('Sim', 'Sim'),
        ('Não', 'Não')
    )
    pergunta1 = models.CharField(verbose_name= 'a) adequação da carga horária ao programa proposto.', max_length=50, choices=resp1, default='1')
    pergunta2 = models.CharField(verbose_name= 'b) importância na formação profissional.', max_length=150, choices=resp1, default='1')
    pergunta3 = models.CharField(verbose_name= 'c) conhecimentos técnicos adquiridos.', max_length=150, choices=resp1, default='1')
    pergunta4 = models.CharField(verbose_name= 'a) assiduidade (inclusive repondo as aulas quando necessário)?', max_length=150, choices=resp1, default='1')
    pergunta5 = models.CharField(verbose_name= 'b)	aproveitamento do tempo de aula (inclusive pontualidade)?', max_length=150, choices=resp1, default='1')
    pergunta6 = models.CharField(verbose_name= 'c) imparcialidade na avaliação dos alunos?', max_length=150, choices=resp1, default='1')
    pergunta7 = models.CharField(verbose_name= 'd)	promoção/manutenção de respeito mútuo em aula?', max_length=150,choices=resp1, default='1')
    pergunta8 = models.CharField(verbose_name= 'e)	atendimento fora do horário das aulas?', max_length=150, choices=resp1, default='1')
    pergunta9 = models.CharField(verbose_name= 'a)	o Plano de trabalho da disciplina (ementa, pré-requisitos, objetivos, conteúdo programático, metodologia de avaliação, bibliografia) foi apresentado?', max_length=150, choices=resp2, default='1')
    pergunta10 = models.CharField(verbose_name= 'b) o Plano de trabalho da disciplina foi cumprido?', max_length=150, choices=resp2, default='1')
    pergunta11 = models.CharField(verbose_name= 'c) o uso de atividades não presenciais é superior a 20% da carga horária da disciplina?', max_length=150, choices=resp3, default='1')
    pergunta12 = models.CharField(verbose_name= 'd) as médias das avaliações bimestrais foram definidas por meio de mais de uma nota?', max_length=150, choices=resp2, default='1')
    pergunta13 = models.CharField(verbose_name= 'e) as notas foram entregues com antecedência de pelo menos 48 horas em relação à avaliação (prova, trabalho, etc.) subsequente?', max_length=150, choices=resp2, default='1')
    pergunta14 = models.CharField(verbose_name= 'a) estímulo à participação dos alunos nas aulas?', max_length=150, choices=resp1, default='1')
    pergunta15 = models.CharField(verbose_name= 'b) clareza e objetividade na exposição do conteúdo?', max_length=150, choices=resp1, default='1')
    pergunta16 = models.CharField(verbose_name= 'c) utilização de exemplos, exercícios e questões que facilitem a aprendizagem?', max_length=150, choices=resp1, default='1')
    pergunta17 = models.CharField(verbose_name= 'd) vinculação da teoria com a prática nas colocações dos conteúdos programáticos?', max_length=150, choices=resp1, default='1')
    pergunta18 = models.CharField(verbose_name= 'e)relação dos conteúdos com outras disciplinas?', max_length=150, choices=resp1, default='1')
    pergunta19 = models.CharField(verbose_name= 'f) O material didático utilizado na disciplina (apostilas, livros, slides, etc.) favorece o ensino-aprendizagem?', max_length=150, choices=resp1, default='1')
    pergunta20 = models.CharField(verbose_name= 'g) O material didático utilizado na disciplina (apostilas, livros, slides, etc.) é atualizado?', max_length=150, choices=resp1, default='1')
    pergunta21 = models.CharField(verbose_name= 'h) O método de ensino (abordagem do tema pelo professor) favorece o ensino- aprendizagem?', max_length=150, choices=resp1, default='1')
    pergunta22 = models.CharField(verbose_name= 'a) As avaliações estão de acordo com a abordagem dos conteúdos programáticos apresentados nas aulas?', max_length=150, choices=resp2, default='1')
    pergunta23 = models.CharField(verbose_name= 'b) As avaliações corrigidas são discutidas com os alunos?', max_length=150, choices=resp2, default='1')
    pergunta24 = models.CharField(verbose_name= 'a) disponibilidade de bens de consumo (materiais, reagentes, softwares, etc.)?', max_length=150, choices=resp1, default='1')
    pergunta25 = models.CharField(verbose_name= 'b) disponibilidade de equipamentos (computadores, estufas, etc.)?', max_length=150, choices=resp1, default='1')
    pergunta26 = models.CharField(verbose_name= 'c) atualização tecnológica (softwares e equipamentos)?', max_length=150, choices=resp1, default='1')
    pergunta27 = models.CharField(verbose_name= 'd) segurança e saúde do ambiente de trabalho (uso de EPIs e EPCs)?', max_length=150, choices=resp1, default='1')
    pergunta28 = models.CharField(verbose_name= 'a) Ao iniciar a disciplina, eu já possuía os conhecimentos prévios exigidos?', max_length=150, choices=resp1, default='1')
    pergunta29 = models.CharField(verbose_name= 'b) Eu compareci às aulas?', max_length=150, choices=resp1, default='1')
    pergunta30 = models.CharField(verbose_name= 'c) Aproveitei todo o tempo de aula (pontualidade e permanência até o fim da aula)?', max_length=150, choices=resp1, default='1')
    pergunta31 = models.CharField(verbose_name= 'd) Estudei e fiz as atividades exigidas pela disciplina?', max_length=150, choices=resp1, default='1')
    pergunta32 = models.CharField(verbose_name= 'e) Procurei relacionar o conteúdo abordado com as demais disciplinas?', max_length=150, choices=resp1, default='1')
    pergunta33 = models.CharField(verbose_name= 'f) Participei das aulas (tirei dúvidas, fiz apontamentos, etc.)?', max_length=150, choices=resp1, default='1')
    pergunta34 = models.CharField(verbose_name= 'g) Utilizei a bibliografia apresentada pelo docente?', max_length=150, choices=resp1, default='1')
    pergunta35 = models.CharField(verbose_name= 'h) Utilizei os horários extras para tirar dúvidas (monitoria ou professor)?', max_length=150, choices=resp1, default='1')
    Sugestão = models.CharField(verbose_name= '', max_length=900)



