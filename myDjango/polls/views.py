from urllib import response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

from .models import Choice, Qusetion
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
    question = get_object_or_404(Qusetion, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Qusetion, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))