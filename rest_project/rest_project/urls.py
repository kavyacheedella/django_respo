from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from base_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_pannel'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('signup/', SignupView, name='signup'),
    # path('logout/', LogoutView, name='logout'),
    # path('', HomeView, name='Home'),
    # path('book_table/', BookTableView, name='Book_Table'),
    # path('menu/', MenuView, name='Menu'),
    # path('about/', AboutView, name='About'),
    # path('feedback/', FeedbackView, name='Feedback_Form'),
    # path('add-to-cart/', add_to_cart, name='add_to_cart'),
    # path('get-cart-items/', get_cart_items, name='get_cart_items'),
    path('', include('base_app.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
