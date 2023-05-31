from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import F, Q


class UserRoles:
    GUEST = 'guest'
    USER = 'user'
    ADMIN = 'admin'
    choices = (
        (GUEST, GUEST),
        (USER, USER),
        (ADMIN, ADMIN),
    )


class UserFoodgram(AbstractUser):
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Email',
        blank=False
        )
    username = models.CharField(
        max_length=150,
        null=False,
        unique=True,
        verbose_name='Никнейм',
        blank=False
        )
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя',
        )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия',
        )
    confirmation_code = models.CharField(
        max_length=150,
        editable=False,
        verbose_name='Код подтверждения',
        null=False,
        blank=False
        )
    role = models.CharField(
        max_length=10,
        choices=UserRoles.choices,
        default=UserRoles.USER,
        verbose_name='Роль'
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    @property
    def is_admin(self):
        return self.is_superuser or self.role == UserRoles.ADMIN

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscription(models.Model):
    user = models.ForeignKey(
        UserFoodgram,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
        null=True
    )
    author = models.ForeignKey(
        UserFoodgram,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Отслеживаемый автор',
        null=True
    )

    def email(self):
        return self.author.email

    @property
    def username(self):
        return self.author.username

    @property
    def first_name(self):
        return self.author.first_name

    @property
    def last_name(self):
        return self.author.last_name

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='unique_following'
            ),
            models.CheckConstraint(
                check=~Q(author=F('user')),
                name='prevent_self_subscription'
            )
        )
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('author',)

    def __str__(self):
        return f'{self.user} теперь подписан на {self.author}'
