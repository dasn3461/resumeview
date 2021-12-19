from django.shortcuts import render
from .forms import StudentRegistration
from django.views import View
from .models import User
# Create your views here.

class HomeView(View):
    def get(self, request):
        form=StudentRegistration()
        candidates=User.objects.all()
        return render(request, 'myapp/home.html', {'form':form, 'candidates':candidates})
    
    def post(self,request):
        form=StudentRegistration(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/home.html', {'form':form})
        
        
class CandidateView(View):
    def get(self, request, pk):
        candidate=User.objects.get(pk=pk)
        return render(request, 'myapp/candidate.html', {'candidate':candidate})        
            


