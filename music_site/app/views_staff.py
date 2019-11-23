from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms_staff import *

#================================== Manage songs ========================================

@login_required
def listSong(request):
    songs = Song.objects.all()
    return render(request, 'staff/song/list.html', {'songs': songs})

@login_required
def createSong(request):
    form = SongForm()

    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('song-list')

    return render(request, 'staff/song/form.html', {'form': form})

@login_required
def updateSong(request, id):
    song = get_object_or_404(Song, pk=id)
    form = SongForm(instance=song)

    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song-list')
            
    return render(request, 'staff/song/form.html', {'form': form})

@login_required
def deleteSong(request, id):
    song = get_object_or_404(Song, pk=id)
    song.delete()
    return redirect('song-list')


#================================== Manage languages ========================================

@login_required
def listLanguage(request):
    languages = Language.objects.all()
    return render(request, 'staff/language/list.html', {'languages': languages})

@login_required
def createLanguage(request):
    form = LanguageForm()

    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('language-list')

    return render(request, 'staff/language/form.html', {'form': form})

@login_required
def updateLanguage(request, id):
    language = get_object_or_404(Language, pk=id)
    form = LanguageForm(instance=language)

    if request.method == 'POST':
        form = LanguageForm(request.POST, instance=language)
        if form.is_valid():
            form.save()
            return redirect('language-list')
            
    return render(request, 'staff/language/form.html', {'form': form})

@login_required
def deleteLanguage(request, id):
    language = get_object_or_404(Language, pk=id)
    language.delete()
    return redirect('language-list')

#================================== Manage categories ========================================

@login_required
def listCategory(request):
    categories = Category.objects.all()
    return render(request, 'staff/category/list.html', {'categories': categories})

@login_required
def createCategory(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category-list')

    return render(request, 'staff/category/form.html', {'form': form})

@login_required
def updateCategory(request, id):
    category = get_object_or_404(Category, pk=id)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category-list')
            
    return render(request, 'staff/category/form.html', {'form': form})

@login_required
def deleteCategory(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return redirect('category-list')

#================================== Manage artists ========================================

@login_required
def listArtist(request):
    artists = Artist.objects.all()
    return render(request, 'staff/artist/list.html', {'artists': artists})

@login_required
def createArtist(request):
    form = ArtistForm()

    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artist-list')

    return render(request, 'staff/artist/form.html', {'form': form})

@login_required
def updateArtist(request, id):
    artist = get_object_or_404(Artist, pk=id)
    form = ArtistForm(instance=artist)

    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('artist-list')
            
    return render(request, 'staff/artist/form.html', {'form': form})

@login_required
def deleteArtist(request, id):
    artist = get_object_or_404(Artist, pk=id)
    artist.delete()
    return redirect('artist-list')    

#================================== Manage authors ========================================

@login_required
def listAuthor(request):
    authors = Author.objects.all()
    return render(request, 'staff/author/list.html', {'authors': authors})

@login_required
def createAuthor(request):
    form = AuthorForm()

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author-list')

    return render(request, 'staff/author/form.html', {'form': form})

@login_required
def updateAuthor(request, id):
    author = get_object_or_404(Author, pk=id)
    form = AuthorForm(instance=author)

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author-list')
            
    return render(request, 'staff/author/form.html', {'form': form})

@login_required
def deleteAuthor(request, id):
    author = get_object_or_404(Author, pk=id)
    author.delete()
    return redirect('author-list')    