from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось, ха-ха-ха!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
