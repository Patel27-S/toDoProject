from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from .models import CustomUser, toDoTable

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'


def home(request):
    return redirect(
               reverse('mainPage', 
                       args=[request.user.id]))


# Below needs to be changed.
def mainPage(request, pk):
    all_to_do = toDoTable.objects.filter(id=pk)
    return render(request, "home.html",{
        "all_items": all_to_do})



def toAddItems(request, pk):
    content_maker = CustomUser.objects.get(id=pk)
    add_content = toDoTable(content_maker, content = request.POST['content'])
    add_content.save()
    return redirect(
               reverse('mainPage', 
                       args=[request.user.id]))



def toDeleteItems(request, pk):
    delete_content = toDoTable.objects.get(id=pk)
    toDoTable.delete(delete_content)
    return redirect(
               reverse('mainPage', 
                       args=[request.user.id]))

