from rest_framework import serializers
from api.v1.register.models import Register


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('id', 'first_name', 'phone_number')

    def validate(self, attrs):
        if len(attrs['phone_number']) != 13 or not attrs['phone_number'].startswith('+'):
            raise serializers.ValidationError('Phone number not valid')
        return attrs
