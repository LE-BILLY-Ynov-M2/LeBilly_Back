from django.urls import path
from . import views
#from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
from .views import AccountListView
#from .views import EventsListView
from .views import DeleteUserView
from .views import GetUserView
from .views import upload_photo_user, delete_photo_user,get_all_photos,GetEventById, GetAllEvents, StripePayment
#schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('create-account/', views.create_account, name='create-account'),
    path('verify-token/<uuid:token>/', views.verify_token, name='verify-token'),
    path('login/', views.login_view, name='connect-account'),
    path('password-reset-request/', views.password_reset_request, name='password_reset_request'),
    path('reset-password/<uuid:token>/', views.password_reset, name='password_reset'),
    path('delete/<int:id>/', DeleteUserView.as_view(), name='delete_user'),
    path('update/<int:id>/', views.update_account, name='update_account'),
    path('user/<int:id>/', GetUserView.as_view(), name='get_user'),
    path('create-admin/<int:id>/', views.create_admin_user, name='create_admin_user'),
    path('update-user-admin/', views.update_account, name='update_user_admin'),
    path('activate-account/<int:temp_account_id>/', views.activate_account, name='activate_account'),
    path('accounts/', AccountListView.as_view(), name='account-list'),
    #path('events/', EventsListView.as_view(), name='events-list'),    
    path('upload_photo/', upload_photo_user, name="upload_photo"),
    path('delete_photo/<str:user_id>/', delete_photo_user, name="delete_photo"),
    path('get_photos/', get_all_photos, name="get_photos"),
    #path('reserve_event/', views.reserve_event, name='reserve_event'),
    path('images/', views.get_images, name='get_images'),    
    path('events/<int:pk>/', GetEventById.as_view(), name='get_event_by_id'),
    path('events/', GetAllEvents.as_view(), name='get_all_events'),
    #path('events/<int:event_id>/payment/', StripePayment.as_view(), name='stripe_payment'),
    path('events/payment/', StripePayment.as_view(), name='stripe_payment'),
    #path('update/', views.update_account, name='update_account'),

]


