from rest_framework import serializers
from .models import Banks

class BanksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banks
        fields=('id','ifsc','bank_id','branch','address','city','district','state','bank_name')

