from .models import Category, Material, User, UserReview
from rest_framework import serializers
from account.models import MyUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category_name"]


class UserReviewSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="user.email", required=False)
    material_name = serializers.CharField(source="material.material_name", required=False)

    class Meta:
        model = UserReview
        fields = ["id", "user", "material", "email", "material_name", "review"]


class MaterialSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.category_name", required=False)
    user = serializers.SerializerMethodField()

    class Meta:
        model = Material
        fields = ["id", "category", "category_name", "material_name", "user"]

    def get_user(self, obj):
        user_list = obj.userreview_set.all()

        return UserReviewSerializer(user_list, many=True).data


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=100, write_only=True)
    password = serializers.CharField(max_length=100, write_only=True)


    class Meta:
        model = MyUser
        fields = ["id", "email", "first_name", "last_name", "password", "confirm_password", "role"]

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError("password didn't match")
        return attrs

    def create(self, validated_data):
        user = MyUser.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
