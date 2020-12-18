from rest_framework import serializers

from .models import BankDetails

class BankDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BankDetails
        fields = ('ifsc', 'address')