from .models import Question, Choice
from rest_framework import serializers

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id','question_text', 'pub_date')


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    question = QuestionSerializer()
    class Meta:
        model = Choice
        fields = '__all__'
