from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect
from .models import Question, Choice
import json

#   handling the index view for the app
def indexView(request) : 
    context = dict()
    try : 
        latest_questions = Question.objects.order_by('-pub_date')
        context = {
            "latest_questions" : latest_questions
        }
    except Question.DoesNotExist as e : 
        print(e)

    return render(request, 'index.html', context)

#   function to show individual question
def details(request, question_id) : 
    try : 
        question = Question.objects.get(id = question_id)
        choices = Choice.objects.filter(question = question)
        if len(choices) <= 0 :
            raise Http404("Choices not available for this question")
    except Question.DoesNotExist : 
        raise Http404("Question does not exist")
    return render(request, 'poll.html', {'question': question, "choices" : choices})

#   function to show the results
def results(request, question_id) : 
    return HttpResponse("Result of {}".format(question_id))

#   function to vote for items
def vote(request, question_id, choice_id) : 
    try : 
        votes = Choice.objects.get(id=choice_id)
        votes.votes+=1
        votes.save()
    except Question.DoesNotExist as e : 
        print(e)
        return None
    
    return redirect("/polls/{}/".format(question_id))

#   function to show all the questions
def allquestions(request) : 
    return HttpResponse("all questions")

