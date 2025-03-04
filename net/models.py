from django.db import models


class NetMember(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='название сети'
    )
    contacts = models.ForeignKey(
        to='net.Contact',
        related_name='netmember',
        on_delete=models.CASCADE,
        verbose_name='контакт'
    )
    suplier = models.ForeignKey(
        to='self',
        verbose_name='поставщик',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    debt = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00,
        verbose_name='задолженность перед поставщиком'
    )
    created_at = models.DateTimeField(
        verbose_name='время создания',
        auto_now_add=True,
    )


class Contact(models.Model):
    email = models.EmailField(
        verbose_name='почта',
    )
    country = models.CharField(
        max_length=30,
        verbose_name='страна',
    )
    city = models.CharField(
        max_length=50,
        verbose_name='город',
    )
    street = models.CharField(
        max_length=100,
        verbose_name='улица',
    )
    # номер дома оставить CharField для случаев если номер дома имеет буквы
    # (напр. Ул. Ленина 12Б)
    home_number = models.CharField(
        max_length=10,
        verbose_name='номер дома',
    )


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='название'
    )
    model = models.CharField(
        max_length=100,
        verbose_name='модель'
    )
    release_date = models.DateField(
        verbose_name='дата выхода продукта на рынок'
    )
    suplier = models.ForeignKey(
        NetMember,
        on_delete=models.CASCADE,
        verbose_name='поставщик'
    )



