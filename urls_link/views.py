import random
import string
from django.shortcuts import render, redirect
from .forms import UrldataForm
from .models import Urldata


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = UrldataForm(request.POST)
        if form.is_valid():
            shortener = ''.join(random.choice(string.ascii_letters)
                                for x in range(8))
            url = form.cleaned_data['url']
            new_url = Urldata(
                url = url,
                new_url = shortener
            )
            new_url.save()
            
            return redirect('index.html')

    else:
        form = UrldataForm()
        new_url = Urldata.objects.all()
    
    return render(request, 'index.html', {
                'new_urls' : new_url,
                'forms' : form
            })

def urlRedirect(request,link):
    urldata = Urldata.objects.get(new_url=link)
    url = urldata.url
    return redirect(url)