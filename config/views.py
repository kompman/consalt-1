from django.shortcuts import render

from .models import SiteConfiguration, Partner


def home(request):
    context = dict()
    context['config'] = SiteConfiguration.get_solo()
    context['partners'] = Partner.objects.all()
    return render(request, 'index.html', context)