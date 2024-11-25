from django.shortcuts import render, get_object_or_404, redirect
from .models import Request
from .forms import RequestForm


def request_list(request):
    requests = Request.objects.all()
    return render(request, 'request_list.html', {'requests': requests})

def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_list')
    else:
        form = RequestForm()
    return render(request, 'create_request.html', {'form': form})

