from django.shortcuts import render, redirect
from .models import Todo
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, View):
    login_url='/login/'
    def get(self, request):
        todos = Todo.objects.filter(actor=request.user)
        return render(request, "index.html", {'todos': todos})
    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')

        # validasi dan messages
        # validasi kalau title dan kontenya kosong
        if not title and not content:
            messages.error(request, message="Title and Content required")
        
        else:
           # user = User.objects # anon  / user context
            Todo.objects.create(title=title, content=content, actor=request.user)

        #print(f"Judul: {title}, Content: {content}")
        return redirect('index')

    
# Create your views here.
# def index_view(request):
#     if request.method == 'POST':

#     else:
class DetailView(View):
    def get(self, request, id):
        
        todo = Todo.objects.get(id=id)

        return render(request, 'detail.html', {'todo':todo})


#def detail_view(request, id):
    
class DeleteView(View):
    def post(self, request, id):
        todo = Todo.objects.get(id = id)

        todo.delete()

        return redirect('index')
    
class UpdateView(View):
    def get(self, request, id):
        todo = Todo.objects.get(id = id)
        return render(request, 'edit.html', {'todo':todo})
    
    def post(self, request, id):
        title = request.POST.get('title')
        content = request.POST.get('content')

        todo = Todo.objects.get(id = id)
        todo.title = title
        todo.content = content

        todo.save()
        
        return redirect('index')