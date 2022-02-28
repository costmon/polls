from django.shortcuts import render

def main(request):
    return render(request, 'control/main.html')

def cart(request):
    cart = "계란"
    cartlist = ["계란", "두부", "커피"]
    return render(
        request,
        'control/cart.html',
        {'cart':cart,'cartlist':cartlist}
    )

def count(request):
    items = ['a', 'b', 'c', 'd']
    return render(request, 'control/count.html', {'items':items})

def register(request):
    if request.method == "POST":
        # 자동 수집
        userid = request.POST['userid']
        email = request.POST['email']
        # 자료 보내기
        return render(request,'control/reg_result.html', {'userid':userid, 'email':email})
    else:     #requst.method == "GET":
        return render(request, 'contol/register.html')