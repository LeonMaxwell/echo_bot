from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Answer, Quiz
from .serializers import AnswerSerializers, QuizSerializers

from rest_framework import status


class QuizView(APIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializers

    def post(self, request, *args, **kwargs):
        serializer = QuizSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        serializer.update(instance=self.queryset.get(user_id=serializer.data['user_id']), validated_data=request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnswerView(APIView):
    def get(self, request, ans, *args, **kwargs):
        answer = AnswerSerializers(Answer.objects.get(type_message=ans.upper()))
        return Response(answer.data)
