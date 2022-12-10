from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User
from .validators import validate_custom_year

FIRST_TEXT_SYM = 15


class CreatedModel(models.Model):
    """Абстрактная модель. Добавляет дату создания."""
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        abstract = True
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:FIRST_TEXT_SYM]


class GenreCategoryBase(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        abstract = True
        ordering = ('-name',)

    def __str__(self):
        return self.name


class Genre(GenreCategoryBase):

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Category(GenreCategoryBase):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Title(models.Model):
    name = models.CharField(
        'Название произведения', null=False, max_length=200
    )
    year = models.PositiveIntegerField(
        'Год', validators=(validate_custom_year,)
    )
    description = models.TextField('Описание')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles',
        verbose_name='Произведение',
    )

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Произведние'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class Review(CreatedModel):
    score = models.PositiveIntegerField(
        validators=(MinValueValidator(1), MaxValueValidator(10))
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews'
    )

    class Meta:
        unique_together = (
            "author",
            "title",
        )
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Comment(CreatedModel):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
