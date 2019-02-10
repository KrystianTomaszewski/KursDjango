from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views import generic
from rest_framework import viewsets,permissions
from .serializers import QuestionSerializer, ChoiceSerializer

class QuestionViewsets(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewsets(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'

class UpdateView(generic.UpdateView):
    model = Question
    fields = '__all__'
    template_name = 'polls/update.html'

class UpdateChoiceView(generic.UpdateView):
    model = Choice
    fields = '__all__'
    template_name = 'polls/update.html'

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
