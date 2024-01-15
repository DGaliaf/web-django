from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Vote
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateObjects(request, objects, results):
    page = request.GET.get('page')
    paginator = Paginator(objects, results)

    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        objects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        objects = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, objects

@login_required()
def questions(request):
    questions = Question.objects.all()
    custom_range, questions = paginateObjects(request, questions, 3)
    context = {'questions': questions, 'custom_range': custom_range}
    return render(request, 'polls/questions.html', context)

@login_required()
def question(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = {'question': question}
    return render(request,
        'polls/question.html', context)

@login_required()
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    labels = []
    data = []
    votes = question.choice_set.select_related('question').all()
    for item in votes:
        labels.append(item.name)
        data.append(item.votes)
    context = {'question': question,
    'labels': labels,
    'data': data}
    return render(request,
        'polls/results.html', context)

@login_required()
def vote(request, question_id):
    profile = request.user.profile
    question = get_object_or_404(Question, pk=question_id)
    try:
        user_choice = question.choice_set.get(pk=request.POST['choice'])
        if not question.user_voted(request.user):
            messages.error(request,
                'Вы уже голосовали в этом опросе.')
            return render(request,
                'polls/question.html',
                {'question': question,'profile': profile})
        if user_choice:
            user_choice.votes += 1
            user_choice.save()
            vote = Vote(user=request.user, question=question, choice=user_choice)
            vote.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    except (KeyError, UnboundLocalError):
        messages.error(request, 'Вы не выбрали вариант ответа!')
        return render(request, 'polls/question.html', {'question': question})
    return render(request,
        'polls/results.html',
        {'question': question, 'profile': profile})
