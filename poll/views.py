from django.http import HttpResponse
from django.shortcuts import render
from poll.models import Question

def index(request):
    question_list = Question.objects.all()   #전체자료 가져오기
    return render(request, 'poll/index.html', {'question_list':question_list})
    #return HttpResponse("<h1>안녕~ Djangi!!</h1>")

def detail(request, pk):
    question = Question.objects.get(id=pk)   #자료1개 가져오기
    return render(request, 'poll/detail.html', {'question':question})

def vote(request, pk):
    #투표하기
    question = Question.objects.get(id=pk)
    if request.method == "POST":
        # 선택 항목 받아 오기
        try:
            choice = request.POST['choice']
        except:
            error = "항목을 선택하세요"
            return render(request, 'poll/detail.html',
                         {'question': question, 'error':error})
        else:
            sel_choice = question.choice.set.get(id=choice) #id로 db에서 검색
            sel_choice.votes += 1  # 1 증가
            sel_choice.save()      # 저장하기
            return render(request, 'poll/result.html', {'question':question})
    else:
        return render(request, 'poll/detail.html', id=pk)

