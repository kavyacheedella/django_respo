from django.urls import path
from .views import LoginView, SignupView, LogoutView, HomeView, BookTableView, MenuView, AboutView, FeedbackView, add_to_cart, get_cart_items, cart_view,checkout,place_order,order_success

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView, name='signup'),
    path('logout/', LogoutView, name='logout'),
    path('', HomeView, name='Home'),
    path('book_table/', BookTableView, name='Book_Table'),
    path('menu/', MenuView, name='Menu'),
    path('about/', AboutView, name='About'),
    path('feedback/', FeedbackView, name='Feedback_Form'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('get-cart-items/', get_cart_items, name='get_cart_items'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('place-order/', place_order, name='place_order'),
    path('order-success/', order_success, name='order_success')


]
