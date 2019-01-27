from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from .models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list,}
    return render(request,'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("To jest pytanie %s." % question_id)

def results(request, question_id):

    response = "To są wyniki pytania %s."

    return HttpResponse(response % question_id)

def vote(request, question_id):
    choice_id = request.POST['choice']
    print("id_choice" + str(request.POST['choice']))
    print("question_id" + str(question_id))
    q = Question.objects.get(pk=question_id)
    print(q.question_text)
    odp = Choice.objects.get(pk=choice_id)
    # odp.vote()
    print(f"Odp: {odp.choice_text}, głosów: {odp.votes} ")
    return HttpResponse("Głosujesz na pytanie %s." % question_id)


def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    context= {'question': question}
    return render(request, 'polls/detail.html',context)
   # return HttpResponse(question.question_text)
