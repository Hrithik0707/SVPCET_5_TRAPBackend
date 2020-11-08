from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PollForm
from .models import PollOffensive
import joblib
import os
from tensorflow.keras import models
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Create your views here.
@login_required
def create_poll(request):
    if request.method=='POST':
           
        #Accepting data changes from Profile form
        text = request.POST['text']
        PollOffensive.objects.create(user = request.user , offensive_sentence = text , vote_yes =0 , vote_no=0)
        return redirect('list')
    else:
        form = PollForm()
        return render(request, 'offensive/create_a_poll.html', {'form' : form}) 

@login_required
def list_of_polls(request):
    if request.method== 'POST':
        sentence = request.POST['sentence']
        vote = request.POST.get('vote')

        voting = PollOffensive.objects.get(id=sentence)
        print(voting)
        if vote == 'yes':
            vote_count = voting.vote_yes
            voting.vote_yes = vote_count+1
            voting.save()
            return redirect('list')
        elif vote == 'no':
            vote_count = voting.vote_no
            voting.vote_no = vote_count+1
            voting.save()
            return redirect('list')
        return redirect('list')
    else:
        lists =PollOffensive.objects.all()
        return render(request, 'offensive/list_polls.html',{'page_obj' : lists})


@login_required
def classify(request):
    if request.method== "POST":
        is_offensive = 'N'
        text = request.POST['text']
        tkn = joblib.load(os.path.dirname(__file__)+'/'+'tokenizer.pkl')
        print(os.path.dirname(__file__)+'/'+'tokenizer.pkl')
        t_reviews = [tkn.convert_tokens_to_ids(tkn.tokenize(text))]
        a = pad_sequences(t_reviews, maxlen=64, dtype='int32', padding='pre', truncating='pre',value=0)
        print(a)
        return redirect('respos')
        model = models.load_model('main/offensive/model')
        score = model.predict(a)
        if score>0.85:
            is_offensive= 'Y'
        print(is_offensive)

    else:
        return render(request, 'offensive/index.html')


def result(request):
    return render(request, 'offensive/respos.html')

def resultn(request):
    return render(request, 'offensive/resneg.html')