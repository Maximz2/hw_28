from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    ing = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Mecтo"
        verbose_name_plural = "Mecтa"

    def __str__(self):
        return self.name


class User(models.Model):
    ROLES = [
        ("member", "Пользователь"),
        ("moderator", "Mодератор"),
        ("admin", "AдмиH"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=58)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=ROLES, default="member")
    age = models.PositiveIntegerField()
    locations = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["user_name"]

    def __str__(self):
        return self.name
