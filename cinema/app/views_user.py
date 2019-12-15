import json
from datetime import datetime, timedelta

from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import *
from .forms_user import *

def index(request):
    queryParams = request.GET    
    
    categoryId = queryParams.get('category_id')
    name = queryParams.get('name')
    categories = Category.objects.all()
    
    movies = Movie.objects.all()

    if categoryId:
        movies = movies.filter(category=Category.objects.get(id=categoryId))

    if name:
        movies = movies.filter(name__contains=name)

    context = {
        'queryParams': queryParams,
        'movies': movies,
        'categories': categories
    }

    return render(request, 'user/index.html', context)

def upcomingMovies(request):
    return render(request, 'user/upcoming_movies.html', {'page': 1})    

def contact(request):
    return render(request, 'user/contact.html', {'page': 2})

def viewMovie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    return render(request, 'user/view_movie.html', {'movie': movie})

def getNextShowDate(movieShow):
    date = datetime.now() + timedelta(days=1)
    
    while (date.weekday() + 2) % 7 !=  movieShow.dayOfWeek % 7:
        date += timedelta(days=1)

    time = movieShow.time
    return date.replace(hour=time.hour, minute=time.minute, second=time.second)

def getNextShows(movie):
    movie_shows = MovieShow.objects.filter(movie=movie)
    shows = []

    for movie_show in movie_shows:
        date = getNextShowDate(movie_show)
        shows.append({'date': date.strftime('%d/%m/%Y %H:%M'), 'room': movie_show.room.code })

    return shows

def getSeatsInfo(request):
    movieId = int(request.GET.get('movie_id', 0))
    roomCode = request.GET.get('room_code', 0)
    showDate = datetime.strptime(request.GET.get('show_date'), '%d/%m/%Y %H:%M')    
    
    movie = get_object_or_404(Movie, pk=movieId)
    room = get_object_or_404(Room, code=roomCode)    
    rows = room.numberOfRows
    cols = room.numberOfCols
    seats = [[{'row': i, 'col': j, 'available': True} for j in range(cols)] for i in range(rows)]

    tickets = BookingTicket.objects.filter(booking__movie=movie, booking__showDate=showDate)

    for ticket in tickets:
        row = ticket.seatRow
        col = ticket.seatCol
        seats[row][col]['available'] = False    
    
    return HttpResponse(json.dumps(seats), content_type='application/json')

def booking(request, id):
    form = BookingForm()
    movie = get_object_or_404(Movie, pk=id)
    shows = getNextShows(movie)
        
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            print('data=', data)
            request.session['booking_form'] = data
            return redirect('booking-confirm', id)

    return render(request, 'user/booking.html', {'movie': movie, 'form' : form, 'shows': shows})

def bookingConfirm(request, id):
    movie = get_object_or_404(Movie, pk=id)
    form = request.session.get('booking_form')
    
    seats = []
    for seat in form['selectedSeats'].split(';'):
        row, col = seat.split(',')
        seats.append(f'{chr(int(row)+65)}{int(col)+1}')

    total = movie.price * len(seats)
    return render(request, 'user/booking_confirmation.html', 
                    {'movie': movie, 'form': form, 'total': total, 'seats': seats})    

def thankYou(request, id):
    movie = get_object_or_404(Movie, pk=id)
    form = request.session.get('booking_form')
    
    booking = Booking.objects.create(
        fullname=form['fullname'],
        phone=form['phone'],
        movie = movie,
        room = Room.objects.get(code=form['room']),
        bookingDate=datetime.now(),
        showDate=datetime.strptime(form['date'], '%d/%m/%Y %H:%M'),
        status=Booking.Status.BOOKED
    )

    seats = []
    for seat in form['selectedSeats'].split(';'):
        row, col = seat.split(',')
        BookingTicket.objects.create(
            booking=booking,
            seatRow=row,
            seatCol=col
        )

    return render(request, 'user/thank_you.html', { 'movie': movie, 'date': form['date']})
