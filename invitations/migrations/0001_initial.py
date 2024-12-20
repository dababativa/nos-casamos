# Generated by Django 5.1.2 on 2024-11-28 00:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Confirmation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("will_attend", models.BooleanField(verbose_name="Asistirá")),
                ("amount", models.IntegerField(verbose_name="Cantidad de asistentes")),
                (
                    "food_restrictions",
                    models.TextField(verbose_name="Restricciones alimenticias"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado el"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Actualizado el"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Invitation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, verbose_name="Nombre del invitado"
                    ),
                ),
                (
                    "message",
                    models.TextField(blank=True, null=True, verbose_name="Mensaje"),
                ),
                ("amount", models.IntegerField(verbose_name="Cupos")),
                (
                    "code",
                    models.CharField(max_length=10, unique=True, verbose_name="Código"),
                ),
                (
                    "expiration_date",
                    models.DateField(verbose_name="Fecha de expiración"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado el"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Actualizado el"),
                ),
                (
                    "is_honorary_invitation",
                    models.BooleanField(
                        default=False, verbose_name="Invitación honorífica"
                    ),
                ),
                (
                    "confirmation",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invitation",
                        to="invitations.confirmation",
                        verbose_name="Confirmación",
                    ),
                ),
            ],
        ),
    ]
