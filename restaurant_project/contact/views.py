from django.shortcuts import render
from . forms import ContactForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
# Create your views here.

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, email, ['admin.example.com'])
            except BadHeaderError:
                return HttpResponse("invalid header")
            form.save()
            return HttpResponseRedirect(reverse("contact:contact"))
        else:
            return render(request, "contact/contact.html", context={
                "form": form
                })
    return render(request, "contact/contact.html", context={
        "form": ContactForm()
    })
