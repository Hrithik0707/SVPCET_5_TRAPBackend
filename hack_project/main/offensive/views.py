from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PollForm
from .models import PollOffensive

# Create your views here.
@login_required
def create_poll(request):
    if request.method=='POST':
           
        #Accepting data changes from Profile form
        form = PollForm(request.POST)  
        # Check - If the form is valid
        if form.is_valid(): 
            form.save()
            return redirect('/')
    else:
        form = PollForm()
        return render(request, 'offensive/create_a_poll.html', {'form' : form}) 

@login_required
def list_of_polls(request):
    if request.method== 'GET':
        list=PollOffensive.objects.all();

        return render(request, 'offensive/list_polls.html',{'page_obj' : list})

@login_required
def vote_poll(request):
    if request.method== 'POST':
        sentence = request.POST['sentence']
        vote = request.POST['vote']

        voting = PollOffensive.object.filter(offensive_sentence=sentence)
        
        if vote == 'yes':
            vote_count = voting.vote_yes
            voting.vote_yes = vote_count+1
        elif vote == 'no':
            vote_count = voting.vote_no
            voting.vote_no = vote_count+1
        # getting all the posts 
        Posts = Product.objects.filter(product_category=category)  
        return render(request, 'product_category.html',{'shop_images' : Posts,'category':category})
    
