from django.db import models
from polls.models import Question


# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"


    name = models.CharField(max_length=100)
    code = models.IntegerField(null=True, blank=True)
    questions = models.ManyToManyField(Question, null=True, blank=True)

    def __str__(self):
        have_questions = "" if self.questions.count() else "- no related questions"
        return self.name
