import copy
from tempfile import template

from django.http import HttpResponse
from django.shortcuts import render
from urllib3 import request


QUESTIONS = [
      {
            'title': f'Title {i}',
            'id':i,
            'text': f'This is text for questions # {i}'
      } for i in range(30)
]




def index(request):
      return render(
            request, 'index.html',
            context={'questions': QUESTIONS}
      )

def hot(request):
      hot_questions = copy.deepcopy(QUESTIONS)
      hot_questions.reverse()
      return render(
            request, 'hot.html',
            context={'questions': hot_questions}
      )
def question(request, question_id):
      one_question = QUESTIONS[question_id]
      return render(
            request, 'question.html',
            context={'item': one_question}
      )