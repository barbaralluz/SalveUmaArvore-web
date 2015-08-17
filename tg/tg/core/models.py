# coding: utf-8

from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from municipios.models import UF, Municipio

class Tree(models.Model):
    
    country = models.CharField(verbose_name=u'País', max_length=100)
    administrative_area_level_1 = models.ForeignKey(UF)
    locality = models.ForeignKey(Municipio)
    neighborhood = models.CharField(verbose_name=u'Bairro', max_length=100)
    route = models.CharField(verbose_name=u'Endereço', max_length=100)
    numero = models.CharField(verbose_name=u'Número', max_length=100)
    postal_code = models.CharField(verbose_name=u'CEP', max_length=100)
    point_of_interest = models.CharField(u'Ponto de Referência', null=True, blank=True, max_length=200)
    
    geometry = models.PointField(verbose_name=u'Localização da Árvore no Mapa')
    objects = models.GeoManager()

    COND_CHOICES = (
        ('Boa', 'Boa - Sem sinal de praga, danos ou doenças'),
        ('Regular', 'Regular - Pequenos sinais de praga, danos ou doenças'),
        ('Ruim', 'Ruim - Risco de queda, sinal de forte ataque de pragas, doenças e danos'),
        ('Caída', 'Caída - Árvore caída'),
    )
    
    condicao_arvore = models.CharField(u'Condição', max_length=100, choices=COND_CHOICES)
    
    especie = models.CharField(verbose_name=u'Espécie', null=True, blank=True, max_length=200)

    HEIGHT_CHOICES = (
        ('Muda', 'Muda - Até 1 m'),
        ('Pequeno Porte', 'Pequeno Porte - Entre 1 e 3 m'),
        ('Médio Porte', 'Médio Porte - Entre 3 e 6 m'),
        ('Grande Porte', 'Grande Porte - Mais que 6 m'),
    )

    altura = models.CharField(u'Altura', max_length=100, choices=HEIGHT_CHOICES)

    RAIZ_CHOICES = (
        ('Não apresenta problemas', 'Raízes profundas e sem danos a edificações e pisos próximos'),
        ('Aponta', 'Raízes superficiais, sem rachaduras, elevação ou desníveis'),
        ('Quebra', 'Raízes  expostas, presença de algumas rachaduras'),
        ('Destrói', 'Raízes expostas, destruição da calçada'),
    )
    
    condicao_raiz = models.CharField(u'Raízes', max_length=100, choices=RAIZ_CHOICES)

    LUZ_CHOICES = (
        ('Presente sem conflito', 'Presente sem conflito'),
        ('Presente com conflito', 'Presente com conflito'),
        ('Ausente', 'Ausente')
    )
    
    condicao_luz = models.CharField(u'Rede elétrica', max_length=100, choices=LUZ_CHOICES)

    MAN_CHOICES = (
        ('Ausente', 'Ausente'),
        ('Afastamento de construção', 'Afastamento de construção'),
        ('Liberação da rede elétrica', 'Liberação da rede elétrica'),
        ('Levantamento de copa', 'Remover ramos que atrapalham trânsito de pedestres ou veículos')
    )
    
    condicao_man = models.CharField(u'Manutenção', max_length=100, choices=MAN_CHOICES)

    descricao = models.TextField(u'Descrição', null=True, blank=True)
    data_cadastro = models.DateField(default=datetime.now)  
    foto1 = models.ImageField(u'Foto 1', upload_to="img/trees", null=True, blank=True)
    foto2 = models.ImageField(u'Foto 2', upload_to="img/trees", null=True, blank=True)
    foto3 = models.ImageField(u'Foto 3', upload_to="img/trees", null=True, blank=True)
    usuario = models.ForeignKey(User)
    

    def __unicode__(self):
        return u"Código: %d " % (
            self.id)    


    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:    
            this = Tree.objects.get(id=self.id)
            if this.foto != self.foto:
                this.foto.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(Tree, self).save(*args, **kwargs)      

    def delete(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Tree.objects.get(id=self.id)
            this.foto.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(Tree, self).delete(*args, **kwargs)    

class Profile(models.Model):
    user = models.OneToOneField(User)

# funcao que cria um perfil toda vez que um usuario for criado pelo Django.contrib.auth
def create_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#configurando o signal que detecta quando um usuario é criado
#ao detectar, executa a funcao acima (create_user) para termos o
# "perfil" ligado ao usuario
post_save.connect(create_user, sender=User)

