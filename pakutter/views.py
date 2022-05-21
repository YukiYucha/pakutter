from django.http import HttpResponse

def index(request):
    str_out = "<p>Good Afternoon</p>"
    str_out += "<p>こんにちは</p>"
    return HttpResponse(str_out)