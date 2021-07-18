from customer.models import Customer

from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    is_company = serializers.BooleanField(default=False)
    related_company = serializers.IntegerField(allow_null=True)
    salary = serializers.DecimalField(decimal_places=2, max_digits=20)
    phone = serializers.CharField(max_length=20)
    mobile = serializers.CharField(max_length = 20)

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)