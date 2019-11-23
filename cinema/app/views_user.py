import random
import string
from datetime import datetime, timedelta

from django.shortcuts import render, redirect, get_object_or_404
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
    dates = []

    for movie_show in movie_shows:
        date = getNextShowDate(movie_show)
        dates.append(date.strftime('%d/%m/%Y %H:%M'))

    return dates


def booking(request, id):
    form = BookingForm()
    movie = get_object_or_404(Movie, pk=id)
    dates = getNextShows(movie)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            data['date'] = data['date'].strftime('%d/%m/%Y %H:%M')
            request.session['booking_form'] = data
            return redirect('booking-confirm', id)

    return render(request, 'user/booking.html', {'movie': movie, 'form' : form, 'dates': dates})

def bookingConfirm(request, id):
    movie = get_object_or_404(Movie, pk=id)
    form = request.session.get('booking_form')
    form['total'] = form['qty'] * movie.price
    return render(request, 'user/booking_confirmation.html', {'movie': movie, 'form': form})    

def randomString(stringLength=6):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

def thankYou(request):
    code = randomString()
    return render(request, 'user/thank_you.html', {'code': str(code)})
