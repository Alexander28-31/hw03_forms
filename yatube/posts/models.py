
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
Group = 'Group'


class Post(models.Model):
    """Модель для хранения постов"""

    text = models.TextField(verbose_name='Description')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Date of publication')
    author = models.TextField(verbose_name='Author')
    group = models.ForeignKey(
        Group,
        related_name='posts',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
    )

    class Meta:
        verbose_name = 'Alex Posting'
        verbose_name_plural = 'Alex Postings'
        ordering = ('-pub_date',)

    def __str__(self) -> str:
        return self.text


class Group(models.Model):
    """Модель для тематических сообществ пользователей """

    title = models.CharField(max_length=200, verbose_name='Title')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    description = models.TextField(verbose_name='Description')

    class Meta:
        verbose_name = 'Alex Group'
        verbose_name_plural = 'Alex Groups'

    def __str__(self) -> str:
        return self.title
