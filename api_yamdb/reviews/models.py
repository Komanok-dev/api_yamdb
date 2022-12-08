from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User

from .validators import validate_custom_year


class CreatedModel(models.Model):
    """Абстрактная модель. Добавляет дату создания."""
    pub_date = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        abstract = True


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=200)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['-name']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('Название категории', max_length=200)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['-name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField('Название произведения',
                            null=False, max_length=200)
    year = models.PositiveIntegerField(
        'Год', validators=[validate_custom_year]
    )
    description = models.TextField('Описание')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles',
        verbose_name='Категория',
    )

    class Meta:
        ordering = ['-name']
        verbose_name = 'Произведние'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class Review(CreatedModel):
    text = models.TextField()
    score = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews'
    )

    class Meta:
        unique_together = (
            "author",
            "title",
        )
        ordering = ('-pub_date',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.title


class Comment(CreatedModel):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-pub_date']

    def __str__(self):
        return self.text
