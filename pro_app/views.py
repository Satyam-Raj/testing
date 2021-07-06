from django.shortcuts import render
from .models import Something
from .forms import Valueform


def form_view(request):
    form = Valueform(request.POST or None)
    if form.is_valid():
        form.save()

        form = Valueform()
    return render(request, 'post.html',{'form':form})




def info_view(request):
    criterias = Something.objects.all()
    context = {

        "criterias" : criterias
    }


    return render(request, 'info.html', context)
