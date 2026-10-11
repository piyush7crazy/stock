from django.db import models

class Stock(models.Model):
    stock_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200 , choices = [('I' , 'IT') , ('Phar' , 'Pharma') , ('B' , 'Bank') , ('C' , 'Cements')])
    quantity = models.IntegerField()
    buy_price = models.DecimalField(max_digits=12 , decimal_places=2)
    current_price = models.DecimalField(max_digits=12 , decimal_places =2)
    date_time = models.DateTimeField(auto_now_add=True)



