from django.http import HttpResponse
from django.template import loader

from .models import News

def index(request):
    latest_news_list = News.objects.order_by('-pub_date')[:5]
    template = loader.get_template('rml/index.html')
    context = {
        'latest_news_list': latest_news_list,
        "img": img
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)