import django_tables2 as tables
from .models import Games

class ALLGAMETABLE(tables.Table):
    class Meta:
        model = Games
        template_name = "django_tables2/bootstrap.html"