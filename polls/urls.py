from django.urls import path
from rest_framework import routers
from . import views

app_name = 'polls'

router = routers.SimpleRouter()
router.register(r'questions',views.QuestionViewsets)
router.register(r'choice', views.ChoiceViewsets)
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),                                # ex: /polls/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),            # ex: /polls/5/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),  # ex: /polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'),           # ex: /polls/5/vote/
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/choiceedit/', views.UpdateChoiceView.as_view(), name='choice'),

]