from django.shortcuts import render
from django.http import HttpResponseRedirect
from guitar_zone.models.guitar_model import Guitar
from guitar_zone.forms import RentOutGuitarForm

def rent_out_guitar(request):
    print("THIS IS REQUEST:",request.user.id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RentOutGuitarForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            post = form.save(commit=False)
            post.seller_id = request.user.id


            post.save()
            print("GOT TO SAVE")
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(redirect_to='/guitar_zone/guitars/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RentOutGuitarForm()

    return render(request, 'guitar_zone/rent_out_guitar.html', {'form': form})