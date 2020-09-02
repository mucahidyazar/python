from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
  #return HttpResponse('Ana sayfa')
  context = {
    'number1': 15,
    'number2': 25
  }
  return render(request, 'index.html', context)

def about(request):
  return render(request, 'about.html')