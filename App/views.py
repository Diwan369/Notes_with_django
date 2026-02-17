from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Note
from django.utils import timezone
from datetime import timedelta

# Update home view to exclude deleted notes
def home(request):
    # Optional: Run cleanup (you might want to do this in a management command instead)
    # Note.delete_old_notes()
    
    query = request.GET.get('q', '')
    if query:
        notes = Note.objects.filter(
            title__icontains=query, 
            is_deleted=False
        ) | Note.objects.filter(
            content__icontains=query, 
            is_deleted=False
        )
    else:
        notes = Note.objects.filter(is_deleted=False)
    return render(request, 'base.html', {'notes': notes, 'query': query})

# Update note_create (no changes needed)
def note_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(title=title, content=content)
        return redirect('home')
    return render(request, 'note_create.html')

# Update note_update (no changes needed, but ensure it only shows non-deleted notes)
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk, is_deleted=False)  # Added is_deleted=False
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('home')
    return render(request, 'note_update.html', {'note': note})

# Update note_delete to use soft delete
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, is_deleted=False)
    if request.method == 'POST':  # Change to POST for security
        note.soft_delete()  # Use soft delete instead of permanent delete
    return redirect('home')

# Add new view for recycle bin
def recycle_bin(request):
    deleted_notes = Note.objects.filter(is_deleted=True).order_by('-deleted_at')
    return render(request, 'recycle_bin.html', {'notes': deleted_notes})

# Add new view to restore notes
def note_restore(request, pk):
    note = get_object_or_404(Note, pk=pk, is_deleted=True)
    if request.method == 'POST':
        note.restore()
    return redirect('recycle_bin')

# Add new view for permanent deletion
def note_permanent_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, is_deleted=True)
    if request.method == 'POST':
        note.delete()  # Permanent delete
    return redirect('recycle_bin')