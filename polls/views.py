from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.template import loader
from django.shortcuts import render, get_object_or_404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list,}
    return render(request,'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("To jest pytanie %s." % question_id)

def results(request, question_id):
    pyt = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': pyt})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message': "You didin't selected a choice",
        })
    else:
        selected_choice.vote()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    context= {'question': question}
    return render(request, 'polls/detail.html',context)
   # return HttpResponse(question.question_text)
