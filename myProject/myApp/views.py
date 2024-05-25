from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Option

def index(request):
    return render(request, 'myApp/index.html')

def start_quiz(request):
    request.session['score'] = 0
    request.session['current_question'] = 0
    return redirect('next_question')

def next_question(request):
    current_question_index = request.session.get('current_question', 0)
    questions = Question.objects.all()
    if current_question_index < questions.count():
        question = questions[current_question_index]
        options = question.options.all()
        return render(request, 'myApp/question.html', {'question': question, 'options': options})
    else:
        score = request.session.get('score', 0)
        return render(request, 'myApp/finished.html', {'score': score})

def check_answer(request):
    if request.method == 'POST':
        question_id = int(request.POST['question_id'])
        selected_option = int(request.POST['option'])
        question = get_object_or_404(Question, pk=question_id)
        if selected_option == question.correct_answer:
            request.session['score'] += 1
        request.session['current_question'] += 1
        return redirect('next_question')
