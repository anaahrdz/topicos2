from django.http import HttpResponse #importar utileria descompuesta http
from datetime import datetime

def hello_world (request):
	now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs ")
	print (now)
	return HttpResponse("Hello_World: La hora del servidor es {now}".format (now=str(now)) )
# funcion obtener usuario y edad	
def say_hi(request, name, age):
		if age < 13:
			mensaje = "lo siento! {} no puedes accerder aqui ".format(name)
		else:
			mensaje = "Bienvenido {} ".format(name)
		return HttpResponse(mensaje)
	