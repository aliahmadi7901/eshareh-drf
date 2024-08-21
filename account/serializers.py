from rest_framework import serializers

from account.models import User


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('phone_number', 'username', 'password', 'confirm_password')

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        phone_number = self.validated_data['phone_number']

        if password != confirm_password:
            raise serializers.ValidationError({'error': 'رمز عبور و تایید رمز عبور یکی نیست'})

        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError({'error': 'این شماره دارای حساب کاربری می باشد!'})

        account = User(phone_number=phone_number, username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account
