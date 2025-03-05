from rest_framework import serializers

from net.models import Contact, NetMember, Product


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class NetMemberSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = NetMember
        fields = "__all__"
        read_only_fields = ("debt",)

    def create(self, validated_data):
        """
        Функция создания объекта
        :param validated_data:
        :return:
        """
        # выдёргиваем из данных инфо о контакте и продуктах
        contacts_data = validated_data.pop("contacts")
        products_data = validated_data.pop("products")

        # создаём контакт и присваеваем его при создании сети
        contacts = Contact.objects.create(**contacts_data)
        net = NetMember.objects.create(contacts=contacts, **validated_data)

        # перебором добавляем продукты сети
        for product_data in products_data:
            product, _ = Product.objects.get_or_create(**product_data)
            net.products.add(product)

        return net
