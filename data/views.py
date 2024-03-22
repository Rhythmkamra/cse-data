# views.py
from django.shortcuts import render, redirect
from django.contrib import messages  # Import messages module
from .forms import StudentForm

def home_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data submitted successfully.')  # Add success message
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = StudentForm()
    return render(request, 'data/home.html', {'form': form})
