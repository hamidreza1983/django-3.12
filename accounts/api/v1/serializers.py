from rest_framework import serializers
from ...models import UserModel
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField()

    class Meta:
        model = UserModel
        fields = ["email", "password", "password1"]

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password1"):
            raise serializers.ValidationError({"detail": "pass1 and pass2 must be same"})
        try:
            validate_password(attrs.get("password"))
        except:
            raise serializers.ValidationError(
                {"detail": "password bayad 8 char bashad\npass bayad yeki az sim hara dashte bashad\npass sade nabashe"}
            )

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password1", None)
        print(validated_data)
        return UserModel.objects.create_user(**validated_data)


class LoginTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    token = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(request=self.context.get("request"), username=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_pass = serializers.CharField()
    new_pass = serializers.CharField()
    conf_pass = serializers.CharField()

    def validate(self, attrs):
        pass1 = attrs["new_pass"]
        pass2 = attrs["conf_pass"]
        if pass1 != pass2:
            raise serializers.ValidationError({"detail": "new pass and confirmation pass must be same"})
        return super().validate(attrs)

    def check_old_password(self, request, attrs):
        old_pass = attrs["old_pass"]
        user = request.user
        if not user.check_password(old_pass):
            raise serializers.ValidationError({"detail": "old password is not correct"})
        return attrs

    def check_new_password(self, request, attrs):
        pass1 = attrs["new_pass"]
        user = request.user
        try:
            validate_password(pass1)
        except:
            raise serializers.ValidationError("pass be lahaz sakhtar ok nist")
        user.set_password(pass1)
        return attrs
