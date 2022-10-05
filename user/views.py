import traceback
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from loguru import logger
from user.serializers import *
from user.models import Customer
from rest_framework_simplejwt.tokens import RefreshToken



class CustomersApiView(GenericAPIView):

    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    serializer_class = RegisterCustomerSerializer

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)

            customer = Customer.objects.create_customer(serializer.data['email'], serializer.data['password'])
            refresh = RefreshToken.for_user(customer)

            return Response({
                'success': True,
                'refresh': str(refresh),
                'data': customer.email
            })

        except BaseException as e:
            print(traceback.format_exc())
            return Response({
                'success': False,
                'exception': f"{traceback.format_exc()}"
            })
