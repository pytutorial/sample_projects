from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms_staff import *

#================================== Manage movies ========================================

@login_required
def listMovie(request):
    movies = Movie.objects.all()
    return render(request, 'staff/movie/list.html', {'movies': movies})

@login_required
def createMovie(request):
    form = MovieForm()

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie-list')

    return render(request, 'staff/movie/form.html', {'form': form})

@login_required
def updateMovie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    form = MovieForm(instance=movie)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie-list')
            
    return render(request, 'staff/movie/form.html', {'form': form})

@login_required
def deleteMovie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    movie.delete()
    return redirect('movie-list')

#================================== Manage languages ========================================    

@login_required
def listLanguage(request):
    languages = Language.objects.all()
    return render(request, 'staff/language/list.html', {'languages': languages})

@login_required
def createLanguage(request):
    form = LanguageForm()

    if request.method == 'POST':
        form = LanguageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('language-list')

    return render(request, 'staff/language/form.html', {'form': form})

@login_required
def updateLanguage(request, id):
    language = get_object_or_404(Language, pk=id)
    form = LanguageForm(instance=language)

    if request.method == 'POST':
        form = LanguageForm(request.POST, request.FILES, instance=language)
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
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category-list')

    return render(request, 'staff/category/form.html', {'form': form})

@login_required
def updateCategory(request, id):
    category = get_object_or_404(Category, pk=id)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category-list')
            
    return render(request, 'staff/category/form.html', {'form': form})

@login_required
def deleteCategory(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return redirect('category-list')

#================================== Manage rooms ========================================        

@login_required
def listRoom(request):
    rooms = Room.objects.all()
    return render(request, 'staff/room/list.html', {'rooms': rooms})

@login_required
def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('room-list')

    return render(request, 'staff/room/form.html', {'form': form})

@login_required
def updateRoom(request, id):
    room = get_object_or_404(Room, pk=id)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room-list')
            
    return render(request, 'staff/room/form.html', {'form': form})

@login_required
def deleteRoom(request, id):
    room = get_object_or_404(Room, pk=id)
    room.delete()
    return redirect('room-list')

#================================== Manage movie shows ========================================

@login_required
def listMovieShow(request):
    movie_shows = MovieShow.objects.all()
    return render(request, 'staff/movie_show/list.html', {'movie_shows': movie_shows})

@login_required
def createMovieShow(request):
    form = MovieShowForm()

    if request.method == 'POST':
        form = MovieShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie-show-list')

    return render(request, 'staff/movie_show/form.html', {'form': form})

@login_required
def updateMovieShow(request, id):
    movie_show = get_object_or_404(MovieShow, pk=id)
    form = MovieShowForm(instance=movie_show)

    if request.method == 'POST':
        form = MovieShowForm(request.POST,  instance=movie_show)
        if form.is_valid():
            form.save()
            return redirect('movie-show-list')
            
    return render(request, 'staff/movie/form.html', {'form': form})

@login_required
def deleteMovieShow(request, id):
    movie_show = get_object_or_404(MovieShow, pk=id)
    movie_show.delete()
    return redirect('movie-show-list')

#================================== Manage movie shows ========================================
@login_required
def listBooking(request):
    keyword = request.GET .get('keyword', '')
    bookings = Booking.objects.all().order_by('status')
    
    if keyword:
        bookings = bookings.filter(phone__contains=keyword)

    return render(request, 'staff/booking/list.html', {'keyword': keyword, 'bookings' : bookings})

@login_required
def bookingDetail(request, id):
    booking = get_object_or_404(Booking, pk=id)
    tickets = BookingTicket.objects.filter(booking=booking)
    
    seats = []
    for ticket in tickets:
        seats.append(f'{chr(ticket.seatRow+65)}{ticket.seatCol+1}')

    return render(request, 'staff/booking/detail.html', {'booking' : booking, 'seats': seats})    

@login_required
def ticketConfirm(request, id):
    booking = get_object_or_404(Booking, pk=id)
    booking.status = Booking.Status.CHECKED_IN
    booking.save()
    return redirect('booking-list')