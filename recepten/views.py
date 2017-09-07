from django.shortcuts import render
import django

# Create your views here.


def voegToe(request):
    if request.method == 'POST':
        naam = request.POST.get('naam')
        cal = request.POST.get('cal')
        ingr = request.POST.get('ingr')
        tijd = request.POST.get('tijd)
        if len(question) == 0:
            return render(request, 'magiceightball/index.html', {'answer': 'You have to ask something'})

        answer = r.get('question:' + question)
        if answer == None:

            answer = random.choice(possible_answers)
            answerindex = possible_answers.index(answer)
            while not cangiveanswer(answerindex):
                answer = random.choice(possible_answers)
                answerindex = possible_answers.index(answer)

            r.incr('answer:' + str(answerindex))
            r.set('question:' + question, answer)
        return render(request, 'magiceightball/index.html', {'answer': answer} )
