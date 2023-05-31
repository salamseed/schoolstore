from django.shortcuts import render, redirect


def base(request):
    return render(request, 'home.html')


def button(request):
    return render(request, 'button.html')


def form(request):
    if request.method == 'POST':
        return redirect("/order")
    return render(request, 'order.html')


def confirmed_order(request):
    return render(request, 'confirmed_order.html')
