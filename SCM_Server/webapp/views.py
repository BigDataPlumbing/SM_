from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
import datetime


def page(request):
    now = datetime.datetime.now()
    site = open('/SCM/web/templates/SCM_index.html')
    data = Template(site.read())
    site.close()
    html = data.render(Context({'current_date': now}))
    return HttpResponse(html)
