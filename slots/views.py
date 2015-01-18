from django.shortcuts import render_to_response
from .forms import NameForm


def home(request, pk):
    form = NameForm()
    
    return render_to_response('home.html', {'user': pk,
                                            'form': form})
