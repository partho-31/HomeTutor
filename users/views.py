from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from users.models import User
from users.serializers import CustomUserSerializer,CustomUserCreateSerializer
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from sslcommerz_lib import SSLCOMMERZ 
from rest_framework.response import Response



class StudentViewSet(ModelViewSet):
    """
    API endpoints for managing students in tuition media platfrom
    - Allows authenticated admin to create,delete and update students
    - Only addmin is allowed to access this API

    """
    queryset = User.objects.filter(role = 'Student')
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]

    
    @swagger_auto_schema(
        operation_summary= 'Retrive the list of Student'
        )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
            operation_summary= 'Create students by Admin',
            request_body= CustomUserCreateSerializer,
            responses= {
                201: CustomUserSerializer,
                400: 'Bad Request'
            }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
            operation_summary= 'Retrive a single Student'
            )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
            operation_summary= 'Update data of a Student by Admin',
            request_body= CustomUserCreateSerializer,
            responses= {
                201: CustomUserSerializer,
                400: 'Bad Request'
            }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
            operation_summary= 'Partially update data of a Student by Admin',
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
            operation_summary= 'Delete a single instance of Student by Admin'
            )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

@api_view(['POST',]) 
def PaymentInitiate(request):
    settings = { 'store_id': 'homet681c8efac4942', 'store_pass': 'homet681c8efac4942@ssl', 'issandbox': True }
    sslcz = SSLCOMMERZ(settings)
    post_body = {}
    post_body['total_amount'] = 100.26
    post_body['currency'] = "BDT"
    post_body['tran_id'] = "12345"
    post_body['success_url'] = "your success url"
    post_body['fail_url'] = "your fail url"
    post_body['cancel_url'] = "your cancel url"
    post_body['emi_option'] = 0
    post_body['cus_name'] = "test"
    post_body['cus_email'] = "test@test.com"
    post_body['cus_phone'] = "01700000000"
    post_body['cus_add1'] = "customer address"
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"


    response = sslcz.createSession(post_body) # API response
    print(response)
    # Need to redirect user to response['GatewayPageURL']
    return Response(response)
