from django.shortcuts import render
from models import Pages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context


@csrf_exempt
def cms_annotated(request, recurso):
    if request.user.is_authenticated():
        estado = ("Eres " + request.user.username + "Logout")
    else:
        estado = ("No estas registrado. " + "Haz login")

    if request.method == 'GET':
        try:
            page = Pages.objects.get(name=recurso)
            salida = (page.page)
        except Pages.DoesNotExist:
            salida = "Recurso no encontrado"

    elif request.method == 'PUT':
        if request.user.is_authenticated():
            pagina = Pages(name=recurso, page=request.body)
            pagina.save()
            salida = ("Pagina guardada: " + request.body)
        else:
            salida = ("No se puede añadir pagina ")
    else:
        salida = "No esta disponible el metodo"

    # plantilla
    template = get_template("index.html")
    # contexto
    c = Context({'mensaje': salida, 'loggin': estado})
    renderizar = template.render(c)

    return HttpResponse(renderizar)


@csrf_exempt
def cms(request, recurso):
    if request.user.is_authenticated():
        estado = "<br><br>Hola " + request.user.username +\
                ". <a href='/admin/logout/'>Logout</a><br>"
    else:
        estado = "<br><br>No estas registrado. <a href='/admin/login/'>Login</a><br>"

    if request.method == "GET":
        try:
    		contenido = Pages.objects.get(name=recurso)
    		return HttpResponse(contenido.name+ ':' + contenido.page)
    	except Pages.DoesNotExist:
    		return HttpResponse("Recurso no encontrado: " + recurso)

    elif request.method == "PUT":
        if request.user.is_authenticated():
            pagina = Pages(name=recurso, page=request.body)
            pagina.save()
            return HttpResponse("Pagina guardada: "+ request.body)
        else:
            return HttpResponse("no se puede añadir la pagina")
    else:
        return HttpResponse( "metodo no disponible")
    return HttpResponse(estado)
