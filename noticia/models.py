from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    data_publicacao = models.DateField(auto_created=True)
    texto = models.TextField()
    image = models.ImageField(upload_to='noticias/')
    autor = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    

        