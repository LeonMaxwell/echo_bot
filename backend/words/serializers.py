from rest_framework import serializers
from .models import Quiz, Answer


class QuizSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['pk', 'user_id', 'age', 'birth', ]


class AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['pk', 'type_message', 'message', ]