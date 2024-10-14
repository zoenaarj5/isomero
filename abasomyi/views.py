from django.http import HttpResponse
from django.template import loader

from abasomyi.models import Umusomyi

def bose(request):
    ilisiti = Umusomyi.objects.all().values()
    template = loader.get_template("urutonde.html")
    context = {
        'inyito':"Readers' list",
        'abas':ilisiti
    }
    return HttpResponse(template.render(context,request))
def umwe(request, id):
    uwo = Umusomyi.objects.get(id=id)
    template = loader.get_template("ibimuranga.html")
    context = {
        "inyito":"Reader's detail",
        "umus":uwo,
    }
    return HttpResponse(template.render(context,request))
def ibanze(request):
    template = loader.get_template("ingenzi.html")
    return HttpResponse(template.render())