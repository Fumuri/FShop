from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306226731',
        'name': 'Muhammad Fakhri',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)