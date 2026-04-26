from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Faculty, Publication
from .forms import FacultyForm, PublicationForm

@login_required
def dashboard(request):
    publications = Publication.objects.all().select_related('faculty')
    
    # Filters
    faculty_id = request.GET.get('faculty')
    pub_type = request.GET.get('pub_type')
    year = request.GET.get('year')
    search_query = request.GET.get('search')
    
    if faculty_id:
        publications = publications.filter(faculty_id=faculty_id)
    if pub_type:
        publications = publications.filter(pub_type=pub_type)
    if year:
        publications = publications.filter(year=year)
    if search_query:
        publications = publications.filter(
            Q(title__icontains=search_query) | 
            Q(faculty__name__icontains=search_query)
        )
        
    publications = publications.order_by('-year', '-id')
    
    faculties = Faculty.objects.all().order_by('name')
    pub_types = Publication.PUB_TYPES
    
    # Stats
    total_faculty = faculties.count()
    total_pubs = Publication.objects.count()
    
    context = {
        'publications': publications,
        'faculties': faculties,
        'pub_types': pub_types,
        'total_faculty': total_faculty,
        'total_pubs': total_pubs,
    }
    return render(request, 'publications/dashboard.html', context)

@login_required
def add_publication(request):
    if request.method == 'POST':
        faculty_form = FacultyForm(request.POST)
        pub_form = PublicationForm(request.POST)
        if faculty_form.is_valid() and pub_form.is_valid():
            faculty = faculty_form.save()
            pub = pub_form.save(commit=False)
            pub.faculty = faculty
            pub.save()
            messages.success(request, 'Record added successfully.')
            return redirect('dashboard')
    else:
        faculty_form = FacultyForm()
        pub_form = PublicationForm()
    return render(request, 'publications/add_publication.html', {
        'faculty_form': faculty_form,
        'pub_form': pub_form
    })

@login_required
def edit_publication(request, pk):
    pub = get_object_or_404(Publication, pk=pk)
    if request.method == 'POST':
        form = PublicationForm(request.POST, instance=pub)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publication updated successfully.')
            return redirect('dashboard')
    else:
        form = PublicationForm(instance=pub)
    return render(request, 'publications/edit_publication.html', {'form': form, 'pub': pub})

@login_required
def delete_publication(request, pk):
    pub = get_object_or_404(Publication, pk=pk)
    if request.method == 'POST':
        pub.delete()
        messages.success(request, 'Publication deleted successfully.')
        return redirect('dashboard')
    return render(request, 'publications/delete_publication.html', {'pub': pub})
