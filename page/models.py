from django.db import models


class Teams(models.Model):
    team_name = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Название')
    team_description = models.TextField(null=True, blank=True, verbose_name='Описание')

    class Meta:
        ordering = ['team_name']
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return self.team_name


hand_categories = (
    (1, 'Неизвестно'),
    (2, 'Правша'),
    (3, 'Левша'),
    (4, 'Обе руки')
)


class Players(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='ФИО')
    birthday = models.DateField(null=True, blank=True, db_index=True, verbose_name='Дата рождения')
    number = models.DecimalField(max_digits=3, decimal_places=0, unique=True, null=True, blank=True, db_index=True, verbose_name='Номер')
    height = models.DecimalField(max_digits=3, decimal_places=0, null=True, blank=True, verbose_name='Рост')
    weight = models.DecimalField(max_digits=3, decimal_places=0, null=True, blank=True, verbose_name='Вес')
    hand = models.SmallIntegerField(choices=hand_categories, default=1, verbose_name='Рука')
    vk_id = models.URLField(max_length=200, unique=True, null=True, blank=True, verbose_name='Страница VK')
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name='Email')
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True, verbose_name='Телефон')
    comment = models.TextField(null=True, blank=True, verbose_name='Комментарий')
    team = models.ForeignKey(Teams, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['name', 'team', 'number']
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

    def __str__(self):
        return self.name
