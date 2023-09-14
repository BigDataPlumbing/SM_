from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
import datetime


def page(request):
    now = datetime.datetime.now()
    fp = open('/SCM/web/templates/SCM_index.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
