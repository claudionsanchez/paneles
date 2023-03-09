# from django.shortcuts import render
# from django.http import HttpResponse

# def inicio(request):
#     return HttpResponse("¡Bienvenido a la venta de paneles solares!")


from django.shortcuts import render

def inicio_view(request):
    return render(request, 'inicio.html')
    # return render(request, 'ventas/inicio.html')
