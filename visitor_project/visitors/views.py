from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Visitor
from .serializers import VisitorSerializer



class CheckInVisitor(APIView):
    def post(self, request):
        phone = request.data.get('phone')

        # Rule: phone cannot be active twice
        if Visitor.objects.filter(phone=phone, check_out_time__isnull=True).exists():
            return Response(
                {"error": "Visitor already checked in"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = VisitorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

class CheckOutVisitor(APIView):
    def post(self, request):
        phone = request.data.get('phone')

        try:
            visitor = Visitor.objects.get(phone=phone, check_out_time__isnull=True)
            visitor.check_out_time = timezone.now()
            visitor.save()
            return Response({"message": "Checked out successfully"})
        except Visitor.DoesNotExist:
            return Response(
                {"error": "Active visitor not found"},
                status=404
            )

class InsideVisitors(APIView):
    def get(self, request):
        visitors = Visitor.objects.filter(check_out_time__isnull=True)
        serializer = VisitorSerializer(visitors, many=True)
        return Response(serializer.data)


class VisitorsByDate(APIView):
    def get(self, request):
        date = request.GET.get('date')  # YYYY-MM-DD

        visitors = Visitor.objects.filter(check_in_time__date=date)
        serializer = VisitorSerializer(visitors, many=True)
        return Response(serializer.data)


