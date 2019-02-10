from django.shortcuts import render

# Create your views here.
from .forms import SubscriberForm


def landing(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = SubscriberForm()

    return render(request,'landing/landing.html',{'form': form})