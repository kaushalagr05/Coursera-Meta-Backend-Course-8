from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer


def index(request):
    """Render the home page for Little Lemon restaurant."""
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    """
    Handles GET (list all menu items) and POST (create a new menu item)
    at /restaurant/menu/
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET (retrieve single item), PUT (update single item),
    and DELETE (remove single item) at /restaurant/menu/<int:pk>
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for table bookings at /restaurant/booking/tables/
    Protected by IsAuthenticated permission class.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
