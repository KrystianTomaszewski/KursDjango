from django.db import models
from django.utils import timezone
import datetime
from django.urls import reverse
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >=timezone.now() -datetime.timedelta(days=1)

    def get_absolute_url(self):
        return reverse('polls:detail', kwargs={'pk': self.pk})
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text + '-' + str(self.votes)

    def vote(self):
        self.votes = self.votes + 1
        self.save()

    def get_absolute_url(self):
        return reverse('polls:detail', kwargs={'pk': self.pk})