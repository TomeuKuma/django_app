from django.http import HttpResponse

def home(request):

    return HttpResponse("Aquesta és sa pàgina incial")
