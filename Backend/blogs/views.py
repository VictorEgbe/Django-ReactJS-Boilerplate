from django.shortcuts import render


def index(request):
    context = {
        'title': 'My Awesome App',
    }
    return render(request, 'index.html', context)
