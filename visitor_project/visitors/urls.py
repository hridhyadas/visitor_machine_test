from django.urls import path
from .views import *

urlpatterns = [
    path('check-in/', CheckInVisitor.as_view()),
    path('check-out/', CheckOutVisitor.as_view()),
    path('inside/', InsideVisitors.as_view()),
    path('by-date/', VisitorsByDate.as_view()),
]
