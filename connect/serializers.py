from rest_framework import serializers
from connect.models import User
from connect.validators import validate_password, validate_phone_number, validate_email


class GetUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'phone_number', 'fix', 'is_active',)

# post user serializer ...


class PostUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        min_length=8, allow_null=True, required=False)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'phone_number',
            'first_name',
            'last_name',
        ]

    def validate(self, value):
        email = value['email']
        phone_number = value['phone_number']
        password = value['password']

        if email is None or phone_number is None or password is None:
            raise serializers.ValidationError(
                {"Details": "Email and phone_number and Password are required"})
        else:
            mail_v = validate_email(email)
            phone_v = validate_phone_number(phone_number)
            password_v = validate_password(password)

            if mail_v == False:
                raise serializers.ValidationError(
                    {"Details ": "Email is not valid."})
            if phone_v == False:
                raise serializers.ValidationError(
                    {"Details ": "Phone number is not valid."})
            if password_v == False:
                raise serializers.ValidationError(
                    {"Details ": "Password is not valid."})

        return value

    def create(self, validated_data):

        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        phone = validated_data['phone_number']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']

        if email == "" and phone == "":  # cheking if the both field are blank
            raise serializers.ValidationError(
                {"Details ": "email or phone required."})

        if password != None:
            user = User.objects.create_user(username=username,
                                            password=password,
                                            email=email,
                                            phone_number=phone,
                                            first_name=first_name,
                                            last_name=last_name)

        return user
