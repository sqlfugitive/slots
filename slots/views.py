from django.shortcuts import render
from .forms import NameForm
from django.http import HttpResponseRedirect
from django.contrib import messages


def home(request, pk):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            messages.add_message(request, messages.INFO, 'Thanks')
            # redirect to a new URL:
            return HttpResponseRedirect(request.path)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'home.html', {'user': pk,
                                            'form': form})
