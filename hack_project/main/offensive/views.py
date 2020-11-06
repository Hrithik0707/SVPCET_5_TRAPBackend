from django.shortcuts import render,redirect

from .forms import PollForm

# Create your views here.
def create_poll(request):
    if request.method=='POST':
           
        # Accepting data changes from Profile form
        form = PollForm(request.POST)  
        # Check - If the form is valid
        if form.is_valid(): 
            form.save()
            return redirect('/')
    else:
        form = PollForm()
        return render(request, 'offensive/create_a_poll.html', {'form' : form}) 

    