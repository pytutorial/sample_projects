from django.urls import path, include
from . import views, views_user, views_staff

urlpatterns = [
    # ================================= Log in ============================================
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup), 

    # ================================User pages =========================================
    path('', views_user.index, name='home'),
    path('song/<int:id>', views_user.viewSong, name='view-song'),
    path('my_playlist', views_user.myPlaylist, name='my-playlist'),

    # ================================Staff pages =========================================
    # Manage songs
    path('staff', views_staff.listSong, name='song-list'),
    path('staff/song_create', views_staff.createSong, name='song-create'),  
    path('staff/song_update/<int:id>', views_staff.updateSong, name='song-update'),  
    path('staff/song_delete/<int:id>', views_staff.deleteSong, name='song-delete'),  

    # Manage languages
    path('staff/laguage_list', views_staff.listLanguage, name='language-list'),
    path('staff/language_create', views_staff.createLanguage, name='language-create'),  
    path('staff/language_update/<int:id>', views_staff.updateLanguage, name='language-update'),  
    path('staff/language_delete/<int:id>', views_staff.deleteLanguage, name='language-delete'),  

    # Manage categories
    path('staff/category_list', views_staff.listCategory, name='category-list'),
    path('staff/category_create', views_staff.createCategory, name='category-create'),  
    path('staff/category_update/<int:id>', views_staff.updateCategory, name='category-update'),  
    path('staff/category_delete/<int:id>', views_staff.deleteCategory, name='category-delete'),  

    # Manage artists
    path('staff/artist_list', views_staff.listArtist, name='artist-list'),
    path('staff/artist_create', views_staff.createArtist, name='artist-create'),  
    path('staff/artist_update/<int:id>', views_staff.updateArtist, name='artist-update'),  
    path('staff/artist_delete/<int:id>', views_staff.deleteArtist, name='artist-delete'),  

    # Manage authors
    path('staff/author_list', views_staff.listAuthor, name='author-list'),
    path('staff/author_create', views_staff.createAuthor, name='author-create'),  
    path('staff/author_update/<int:id>', views_staff.updateAuthor, name='author-update'),  
    path('staff/author_delete/<int:id>', views_staff.deleteAuthor, name='author-delete'),  
]