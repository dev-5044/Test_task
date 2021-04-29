from multiprocessing import Process
from django.http import Http404, JsonResponse
from django.views.generic import UpdateView, ListView, CreateView
from django.shortcuts import render
from bot.models import Asset

from bot.bin_logic import client, start_trade


class AssetLIstView(ListView):
    """ Клас отображения на главной странице """
    context_object_name = 'data'
    template_name = 'home.html'
    
    def get_queryset(self): #
        queryset = Asset.objects.filter(status='OPEN')
        for i in queryset:
            if not i.work:
                print('start')
                i.work = True
                i.save()
                Process(target=start_trade, args=[i], daemon=True).start()
        return queryset
                
    
    
class AssetUpdateView(UpdateView):
    """Обновляяет даные объекта"""
    model = Asset
    fields = ['limit', 'quantity']
    success_url = '/home'
    template_name = 'update.html'
    

class AssetCreateView(CreateView):
    """Создает объект asset"""
    model = Asset
    fields = ['name', 'limit', 'quantity']
    success_url = '/home'
    template_name = 'create.html'
    
