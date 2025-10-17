from rest_framework import serializers
from .models import KitchenList

class KitchenListSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenList
        fields = '__all__'
        read_only_fields = ['user', 'added_on']

    def create(self, validated_data):
        # Automatically assign the logged-in user
        user = self.context['request'].user
        return KitchenList.objects.create(user=user, **validated_data)
