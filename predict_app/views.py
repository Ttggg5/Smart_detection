from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        return render(request, 'register.html', {'state': '註冊成功', 'state_color': 'seagreen'})

    return render(request, 'register.html')
