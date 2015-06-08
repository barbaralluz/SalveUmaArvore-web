# coding: utf-8

from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save

class Tree(models.Model):
    
    country = models.CharField(verbose_name=u'País', max_length=100)
    administrative_area_level_1 = models.CharField(verbose_name=u'Estado', max_length=100)
    locality = models.CharField(verbose_name=u'Cidade', max_length=100)
    neighborhood = models.CharField(verbose_name=u'Bairro', max_length=100)
    route = models.CharField(verbose_name=u'Endereço', max_length=100)
    numero = models.CharField(verbose_name=u'Número', max_length=100)
    postal_code = models.CharField(verbose_name=u'CEP', max_length=100)
    point_of_interest = models.TextField(u'Ponto de Referência', null=True, blank=True)
    
    geometry = models.PointField(verbose_name=u'Localização da Árvore no Mapa')
    objects = models.GeoManager()
    
    especie = models.CharField(verbose_name=u'Espécie', max_length=200)
    altura = models.CharField(u'Altura', max_length=100)
    diametro = models.CharField(u'Diâmetro', max_length=100)
    informacoes_adicionais = models.TextField(u'Informações Adicionais', null=True, blank=True)
    data_cadastro = models.DateField(default=datetime.now)  
    foto = models.ImageField(upload_to="img/trees", null=True, blank=True)
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


