from django.shortcuts import render ,redirect
from .forms import EmailAbonelikForm
from .models import EmailAbonelik

def index(request):
    return render(request, 'abonelik/index.html')

def EmailKayit(request):
    if request.method == 'POST':
        form = EmailAbonelikForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmailAbonelikForm()
    return render(request, 'abonelik/emailkayit.html', {'form': form})

def EmailListe(request):
    aboneler = EmailAbonelik.objects.all()
    return render(request, 'abonelik/liste.html',{'aboneler':aboneler})