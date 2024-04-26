from rest_framework import serializers

from .models import Salib, Theme

class SalibSerializer(serializers.ModelSerializer):
    salib_detail_url = serializers.SerializerMethodField(read_only=True, source = 'get_salib_detail_url')
    class Meta:    
        model = Salib
        fields = ['id','nomi', 'yil', 'salib_detail_url']


    def get_salib_detail_url(self, obj):
        return f'http://127.0.0.1:8000/api/v1/salib/{obj.id}'


class SalibDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salib
        fields = '__all__'

