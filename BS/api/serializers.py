from rest_framework import serializers
from api.models import Employee , CustomUser




class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    Employee_id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role') 
        )
        return user