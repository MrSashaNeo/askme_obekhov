import copy
from tempfile import template

from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


QUESTIONS = [
      {
            'title': f'Title #{i}',
            'id':i,
            'text': f'This is text for questions #{i}'
      } for i in range(30)
]

ANSWERS = [
      {
            'id':i,
            'text': f'This is text for answer #{i}'
      } for i in range(4)
]

def paginate(object_list,request,per_page):
      paginator = Paginator(object_list,per_page)
      page_number = int(request.GET.get('page',1))

      try:
            page = paginator.page(page_number)
      except PageNotAnInteger:
            page = paginator.page(1)
      except EmptyPage:
            page = paginator.page(paginator.num_pages)
      return page

def index(request):

      page=paginate(QUESTIONS,request,10)

      return render(
            request, 'index.html',
            context={'questions': page.object_list, 'page_obj': page}
      )

def hot(request):
      hot_questions = copy.deepcopy(QUESTIONS)
      hot_questions.reverse()

      page = paginate(hot_questions, request, 10)

      return render(
            request, 'hot.html',
            context={'questions': page.object_list, 'page_obj': page}
      )

def tagblablabla(request):
      tag_questions = copy.deepcopy(QUESTIONS)
      tag_questions.reverse()

      page = paginate(tag_questions, request, 10)

      return render(
            request, 'tagblablabla.html',
            context={'questions': page.object_list, 'page_obj': page}
      )

def question(request, question_id):
      one_question = QUESTIONS[question_id]
      answers = copy.deepcopy(ANSWERS)
      return render(
            request, 'question.html',
            context={'item': one_question, 'answers': answers}
      )


def ask(request):
      return render(
            request, 'ask.html'
      )

def login(request):
      return render(
            request, 'login.html'
      )


def settings(request):
      return render(
            request, 'settings.html'
      )

def signup(request):
      return render(
            request, 'signup.html'
      )