from django.urls import path
from .views import AnswerView, QuizView

urlpatterns = [
    path('quiz/post/', QuizView.as_view(), name='quiz'),
    path('words/get/<str:ans>/', AnswerView.as_view(), name='words'),
]