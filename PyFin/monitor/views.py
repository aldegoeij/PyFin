from django.http import HttpResponse
from django.template import Context, loader

from PyFin.monitor.models import AuditLog

def home(request):
    """
    Views displays the home page of the PyFin Monitor application
    """
    template = loader.get_template('base.html')
    context = Context({
        'title': 'title of the page',
        'test': 'some text goes here of course', #FIXME
        })
    return HttpResponse(template.render(context))

def query_database(request):
    """
    Views displays the home page of the PyFin Monitor application
    """
    items = AuditLog.objects.all()
    template = loader.get_template('query_database.html')
    context = Context({
        'title': 'Query Database',
        'test': 'some text goes here', #FIXME
        'items': items,
    })
    return HttpResponse(template.render(context))
