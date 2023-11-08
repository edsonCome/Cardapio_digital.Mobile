# Generated by Django 4.2.7 on 2023-11-08 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
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
                ("nome", models.CharField(max_length=55)),
                ("descricao", models.TextField(blank=True)),
                ("ordem", models.IntegerField(blank=True, default=0)),
            ],
            options={
                "ordering": ("ordem", "nome"),
            },
        ),
        migrations.CreateModel(
            name="Comanda",
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
                ("codigo", models.SlugField(blank=True, max_length=8, unique=True)),
                ("abertura", models.DateTimeField(auto_now_add=True)),
                ("fechamento", models.DateTimeField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("aberta", "Aberta"), ("fechada", "Fechada")],
                        default="aberta",
                        max_length=7,
                    ),
                ),
                (
                    "valor_total",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ItemCardapio",
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
                ("item", models.CharField(max_length=100)),
                ("preco", models.DecimalField(decimal_places=2, max_digits=5)),
                ("activo", models.BooleanField(default=True)),
                ("necessita_preparo", models.BooleanField(default=True)),
                ("descricao", models.TextField(blank=True)),
                (
                    "categoria",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="restaurante.categoria",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Mesa",
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
                ("numero", models.CharField(max_length=3, unique=True)),
                ("slug", models.SlugField(blank=True, max_length=8, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="ItemPedido",
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
                ("preco", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("preparo", "Em preparo"),
                            ("pronto", "Pronto"),
                            ("entregue", "Entregue"),
                        ],
                        default="preparo",
                        max_length=10,
                    ),
                ),
                ("obs", models.TextField(blank=True)),
                ("hr_pedido", models.DateField(auto_now_add=True)),
                ("hr_entregue", models.DateTimeField(blank=True, null=True)),
                (
                    "comanda",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="restaurante.comanda",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="restaurante.itemcardapio",
                    ),
                ),
            ],
            options={
                "ordering": ("hr_pedido", "item"),
            },
        ),
        migrations.AddField(
            model_name="comanda",
            name="mesa",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="restaurante.mesa",
            ),
        ),
    ]
