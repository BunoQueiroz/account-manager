from django.shortcuts import render


def handler404(request, exception):
    return render(request, 'core/page_not_found.html')
