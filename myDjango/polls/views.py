from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Qusetion
# Create your views here.

def index(request):
    # return HttpResponse("Hello, world.")
    latest_question_list = Qusetion.objects.order_by("-pub_date")[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Qusetion, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
