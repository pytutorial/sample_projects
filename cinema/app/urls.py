from django.urls import path, include

from .import views, views_user, views_staff

urlpatterns = [
    # ================================= Log in ============================================
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup), 

    # ================================User pages =========================================
    path('', views_user.index, name='home'),
    path('upcoming_movies', views_user.upcomingMovies, name='upcoming-movies'),
    path('contact', views_user.contact, name='contact'),
    path('movie_detail/<int:id>', views_user.viewMovie, name='view-movie'),
    path('booking/<int:id>', views_user.booking, name='booking'),
    path('booking_confirm/<int:id>', views_user.bookingConfirm, name='booking-confirm'),
    path('thank_you', views_user.thankYou, name='thank-you'), 

    # ================================Staff pages =========================================
    # Manage movies
    path('staff', views_staff.listMovie, name='movie-list'),
    path('staff/movie_create', views_staff.createMovie, name='movie-create'),  
    path('staff/movie_update/<int:id>', views_staff.updateMovie, name='movie-update'),  
    path('staff/movie_delete/<int:id>', views_staff.deleteMovie, name='movie-delete'),  

    # Manage movie shows
    path('staff/movie_show_list', views_staff.listMovieShow, name='movie-show-list'),
    path('staff/movie_show_create', views_staff.createMovieShow, name='movie-show-create'),  
    path('staff/movie_show_update/<int:id>', views_staff.updateMovieShow, name='movie-show-update'),  
    path('staff/movie_show_delete/<int:id>', views_staff.deleteMovieShow, name='movie-show-delete'),  

    # Manage language
    path('staff/language_list', views_staff.listLanguage, name='language-list'),
    path('staff/language_create', views_staff.createLanguage, name='language-create'),  
    path('staff/language_update/<int:id>', views_staff.updateLanguage, name='language-update'),  
    path('staff/language_delete/<int:id>', views_staff.deleteLanguage, name='language-delete'),  

    # Manage Category
    path('staff/category_list', views_staff.listCategory, name='category-list'),
    path('staff/category_create', views_staff.createCategory, name='category-create'),  
    path('staff/category_update/<int:id>', views_staff.updateCategory, name='category-update'),  
    path('staff/category_delete/<int:id>', views_staff.deleteCategory, name='category-delete'),
]