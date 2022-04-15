from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from .models import Table



class TablePage(ListView):
    # paginate_by = 1
    model = Table
    template_name = 'table/index.html'
    context_object_name = 'table'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

    def get_queryset(self):
        # return Table.objects.all()
        search_query = self.request.GET.get('key_item')
        return Table.objects.filter(Q(title__icontains=search_query) | Q(
            quantity__icontains=search_query) | Q(distance__icontains=search_query))
