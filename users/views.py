from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from users.models import User
from users.serializers import CustomUserSerializer,CustomUserCreateSerializer
from drf_yasg.utils import swagger_auto_schema

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