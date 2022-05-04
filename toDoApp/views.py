from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import toDoTable

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'


def mainPage(request):
    all_to_do = toDoTable.objects.all()
    return render(request, "home.html",{
        "all_items": all_to_do})


def toAddItems(request):
    add_content = toDoTable(content = request.POST['content'])
    add_content.save()
    return redirect('/main/')


def toDeleteItems(request, pk):
    delete_content = toDoTable.objects.get(id=pk)
    toDoTable.delete(delete_content)
    return redirect('/main/')