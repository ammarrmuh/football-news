from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406495602',
        'name': 'Ammar Muhammad Rafif',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)