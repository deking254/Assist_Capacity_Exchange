from django.shortcuts import render, get_object_or_404
from .forms import BugForm
from .models import Bug 

# Create your views here.
def add_bug(request):
    """adds a bug to the database"""
    if request.method == 'POST':
        form = BugForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
    else:
        form = BugForm()
    return render(request, 'bug/add_bug.html', {'form': form})

def bug_list(request):
    """displays the bugs in the database"""
    bugs = Bug.objects.all()
    return render(request, 'bug/bug_list.html', {'bugs': bugs})

def bug_details(request, bug_id):
    """this function handles the bug details page"""
    bug = get_object_or_404(Bug, pk=bug_id)
    return render(request, 'bug/bug_details.html', {'bug': bug})
