from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .forms import Question_Name,Choice_Name
from polls.models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published question"""
        return Question.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        #Redisplaying the question voting form.
        return render(request, 'polls/detail.html', {'question':question,
                                                     'error_message':"You didn't select a choice.",
                                                     })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def enter_question(request):
    if request.method == 'POST':

        question_form=Question_Name(request.POST)
        if question_form.is_valid():
            date=request.POST.get('pub_date', '')
            question=request.POST.get('question_text', '')
            quest_obj=Question(question_text=question,pub_date=date)
            quest_obj.save()

            return HttpResponseRedirect(reverse('polls:question_input'))
    else:
        question_form = Question_Name()

        return  render(request, 'polls/question_input.html',{'question_form':question_form,})


def enter_choice(request):
    latest_question=Question.objects.all()
    if request.method == 'POST':
        choice_form=Choice_Name(request.POST)
        if choice_form.is_valid():
            choice=request.POST.get('choice_text', '')
            #question=latest_question(question=request.POST.get('quest_choice',))
            choice_obj=Choice(choice_text=choice)
            choice_obj.save()

            return HttpResponseRedirect(reverse('polls:choice_input',))

    else:
        choice_form=Choice_Name()
        return render(request,'polls/choice_input.html',{'question':latest_question,
                                                         'choice_form':choice_form,})

