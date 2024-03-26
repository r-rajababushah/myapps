from django.http import HttpResponse
from .models import Question
from django.template import loader

def index(request):
    myqn = Question.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mydata': myqn,
    }
    return HttpResponse(template.render(context, request))