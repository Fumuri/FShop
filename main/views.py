from django.shortcuts import render

def show_main(request):
    context = {
        'app' : 'FShop',
        'name': 'Muhammad Fakhri',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)