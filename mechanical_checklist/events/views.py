from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CreateSubscriptionForm


@login_required
def create_subscription(request):
    if request.method == "POST":
        form = CreateSubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.user = request.user
            subscription.save()
            return redirect(subscription)
    else:
        form = CreateSubscriptionForm()
    return render(request, "subscriptions/create.html", {
        "form": form,
    })
