from django.db import models

# Create your models here.

class Articulo(models.Model):
    """Article model."""
    titulo = models.fields.CharField(max_length=1024)
    intro = models.fields.CharField(max_length=512)
    contenido = models.fields.TextField()

    def as_dict(self):
        """Transformación en dict."""
        return {
            'titulo': self.titulo,
            'intro': self.intro,
            'contenido': self.contenido,
        }

    def __str__(self):
        """Str -> self.titulo"""
        return self.titulo
