import json

from django.views.generic import TemplateView, DetailView, ListView
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render, reverse, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string, get_template
from django.core.paginator import Paginator
from django.core.mail import send_mail

from filer.models import Image

from core.models import Static, Category, Good, Project, Certificate, AboutUsInNumbers, Service, Category



def handle_404_view(request, exception):
    response = render(request, 'core/404.html')
    response.status_code = 404
    return response


def handle_500_view(request):
    response = render(request, 'core/500.html')
    response.status_code = 500
    return response


class StaticPageView(DetailView):


    model = Static
    template_name = 'static_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_link'] = f'{self.object.slug}'
        return context


class IndexView(TemplateView):
    '''
    Главная страница
    '''

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

        about_us_in_numbers = AboutUsInNumbers.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(on_main=True)
        services = Service.objects.filter(active=True)
        goods_category_list = Category.objects.all
        goods_list = Good.objects.all()
        project_list = Project.objects.all()
        response = render(request, self.template_name, locals())

        return response


@csrf_exempt
def send_message_ajax(request):
    subject = u"Сообщение с сайта"
    files = []

    message_template = get_template('messages/email_request.txt')
    message_context = {
        'data': request.POST,
    }

    if (len(message_context["data"]["name"]) > 0 and len(message_context["data"]["phone"]) > 0):
        message = message_template.render(message_context)
        send_mail(subject, message, 'sender@fence.profograd.ru', ["vladimir@vanger.org"], fail_silently=False)
        return HttpResponse(json.dumps(1), content_type='application/javascript')
    else:
        return HttpResponse(json.dumps(0), content_type='application/javascript')
