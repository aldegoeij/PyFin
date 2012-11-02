from django.http import HttpResponse
from django.template import Context, loader

def home(request):
    """
    Views displays the home page of the PyFin Monitor application
    """
    template = loader.get_template('home.html')
    context = Context({
    })
    return HttpResponse(template.render(context))