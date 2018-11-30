 # -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import View
from django.views.generic.list import ListView
from vanilla.apps.articulos.models import Articulo

# Create your views here.
class ArticulosView(ListView):
    """View para listar artículos."""

    template_name = 'vanilla/apps/articulos/index.html'

    model = Articulo
    paginate_by = 20

class ArticulosAPIView(View):
    """View para listar artículos (API)."""

    def get(self, request):
        """GET."""
        return JsonResponse({
            'articulos': [
                art.as_dict() for art in Articulo.objects.all()
            ]
        })
