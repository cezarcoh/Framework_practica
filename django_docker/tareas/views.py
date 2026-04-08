from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def hola_mundo(request):
    
    html = """
    <html>
        <body style="font-family: sans-serif; text-align: center; margin-top: 50px; background-color: #418a37;">
            <h1 style="color: #092e20;">¡Hola! <strong>html simple</strong></h1>    
        </body>
    </html>
    """
    return HttpResponse(html)