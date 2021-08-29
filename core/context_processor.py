from django.http import HttpRequest


def global_context(request: HttpRequest):
    '''
    Возвращает контекст, который доступен во всех шаблонах
    '''

    context = {

    }

    return context
