from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='tables')

urlpatterns = [
    # Static home view: /restaurant/
    path('', views.index, name='index'),

    # Menu API endpoints: /restaurant/menu/ and /restaurant/menu/<pk>
    path('menu/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-item'),

    # Booking API router: /restaurant/booking/tables/
    path('booking/', include(router.urls)),

    # Token authentication endpoint: /restaurant/api-token-auth/
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
