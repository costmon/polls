from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'poll/index.html')
    #return HttpResponse("<h1>안녕~ Djangi!!</h1>")

def cart(request):
    cart = "계란"
    cartlist = ["계란", "두부", "커피"]
    return render(
        request,
        'poll/cart.html',
        {'cart':cart,'cartlist':cartlist}
    )

