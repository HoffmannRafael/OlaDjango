from django.contrib import admin
from .models import Pessoa, TipoPessoa, InteracoesPessoa

admin.site.register(Pessoa)
admin.site.register(TipoPessoa)
admin.site.register(InteracoesPessoa)
