from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Stock
from .serializers import StockSerializer


@api_view(['POST'])
def create_stock_api(request):
    serializer = StockSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=201)
    return Response(serializer.errors  ,status=400)


@api_view(['GET'])
def list_stock_api(request):
    s = Stock.objects.all()
    serializer = StockSerializer(s , many=True)
    return Response(serializer.data , status=200)


@api_view(['GET'])
def detail_stock_api(request , id):
    try:
        s = Stock.objects.get(id=id)
    except Stock.DoesNotExist:
        return Response({"error": "Stock not found"} , status=404)
    serializer = StockSerializer(s)
    return Response(serializer.data , status=200)


@api_view(['PATCH'])
def update_stock_api(request,id):
    try:
        s = Stock.objects.get(id=id)
    except Stock.DoesNotExist:
        return Response({"error": "Stock Not Found"} , status = 404)
    serializer = StockSerializer(s , data=request.data , partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=200)
    return Response(serializer.errors  , status=400)


@api_view(['DELETE'])
def delete_stock_api(request,id):
    try:
        s = Stock.objects.get(id=id)
    except Stock.DoesNotExist:
        return Response({"error": "Stock Not Found"}, status=404)
    s.delete()
    return Response(status=204)        



@api_view(['GET'])
def summary_stock_api(request):
    s=Stock.objects.all()
    total_invested = 0
    total_current_value = 0
    for i in s :
        total_invested = total_invested + i.quantity * i.buy_price
        total_current_value = total_current_value + i.quantity * i.current_price
    overall_profit_loss = total_current_value - total_invested
    return Response({"invested" : total_invested , "current" : total_current_value ,"pl" : overall_profit_loss})
