from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myapp.forms import lobForm, pinForm,NameForm,ContactForm
# Create your views here.
def hello(request):
    if request.method == 'POST':
        form= lobForm(request.POST)
        if form.is_valid():
            return HttpResponse("Values accepted")
    else:
        form= lobForm()
        return render(request,'form.html',{'form': form})


def pins(request):
    if request.method == 'POST':
        pin= pinForm(request.POST)
        if pin.is_valid():
            return HttpResponse("Values accepted")
        else:
            return HttpResponse("Values not found")
    else:
        pin= pinForm()
        return render(request,'form.html',{'pin': pin})




def get_name(request):
# if this is a POST request we need to process the form data
    if request.method == 'POST':
# create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
# check whether it's valid:
        if form.is_valid():
# process the data in form.cleaned_data as required
# ...
# redirect to a new URL:
            return HttpResponse('thanks')
    else:
        form = NameForm()
        return render(request, 'yourname.html', {'form': form})


from django.core.mail import send_mail
def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']|0
            recipients = ['aswinvishnuaaswinam@gmail.com']
            if cc_myself:
                recipients.append(sender)
                send_mail(subject, message, sender, recipients)
                return HttpResponseRedirect('/thanks/')
    else:
        form=ContactForm()
        return render(request,'contact.html',{'contactform': form})
