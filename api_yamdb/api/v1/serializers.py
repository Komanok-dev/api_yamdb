from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from rest_framework_simplejwt.tokens import AccessToken
from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User

class ReviewSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review

    def validate(self, data):
        author = self.context.get('request').user
        title_id = self.context.get('view').kwargs.get('title_id')

        if (
            self.context.get('request').method == 'POST'
            and Review.objects.filter(
                title_id=title_id, author_id=author.id
            ).exists()
        ):
            raise serializers.ValidationError(
                'Вы уже оставляли свой отзыв на данное произведение'
            )
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    review = serializers.SlugRelatedField(slug_field='text', read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id',)
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id',)
        model = Genre


class TitleGetSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title


class TitlePostSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug', many=True, queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Title


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )
        model = User
        lookup_field = 'username'


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=('email'),
                message='This email is already taken',
            )
        ]

    def validate_username(self, value):
        if User.objects.get(username=value).exists():
            raise serializers.ValidationError('This username is already in use')
        if value.lower() == 'me':
            raise serializers.ValidationError('You cant use "me" as username')
        return value


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    confirmation_code = serializers.CharField(max_length=254)
    
    def get_token(request):
        email = request.data.get('email')
        user = get_object_or_404(User, email=email)
        confirmation_code = request.data.get('confirmation_code')
        if default_token_generator.check_token(user, confirmation_code):
            return AccessToken.for_user(user)
        return 'Incorrect confirmation code'