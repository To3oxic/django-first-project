from django.shortcuts import render,redirect,get_object_or_404

from item.models import Catagory,Item

from .forms import SignupForm


def index(request):
    items = Item.objects.all()
    catagories = Catagory.objects.all()

    return render(request, 'polls/index.html',{
         'items': items,
         'catagories': catagories,}
                  )



def contact(request):
    return render(request, 'polls/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:

        form =SignupForm()

    return render(request, 'polls/signup.html', {
        'form': form
        })
def base(request):
    return render(request, 'polls/base.html')
