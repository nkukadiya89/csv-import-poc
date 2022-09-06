# This API create using view set
from aifc import Error
import codecs
import csv
from xml.dom import ValidationErr

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Product
from rest_framework import status

fs = FileSystemStorage(location='tmp/')


# API's Serializer
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


# Here Viewset
class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['POST'])
    def upload_data_with_validation(self, request):
        """Upload data from CSV, with validation."""
        file_data = {}
        file = request.FILES.get("file")
        if not file.name.endswith('.csv'):
            file_data["success"] = False
            file_data["msg"] = "Please Upload Only CSV Format File."            
            return Response(data=file_data, status=status.HTTP_400_BAD_REQUEST)
        

        reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
        data = list(reader)

        serializer = self.serializer_class(data=data, many=True)
        serializer.is_valid(raise_exception=True)

        product_list = []
        for row in serializer.data:
            product_list.append(
                Product(
                    user_id=row["user"],
                    item_name=row["item_name"],
                )
            )

        Product.objects.bulk_create(product_list)

        return Response("Successfully upload the data")