from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['stock_name' , 'category' , 'quantity' , 'buy_price' , 'current_price' , 'date_time' , 'id']