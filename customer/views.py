from django.shortcuts import render
from django.http import JsonResponse
from customer.models import Customer, HistoryKeyword,Order,MatQuantity
from food.models import Dish, Material, DishMat, WeightInterval

# Create your views here.


def top_search_dish(request):
    if request.method == 'GET':
        search = HistoryKeyword.objects.order_by('-search_count')[:5]
            #filter(name__contains=keywords)
        search_list = []
        for asearch in search:
            search_dict = {
                'keyword': asearch.keyword
            }
            search_list.append(search_dict)
        result = {
            'search_keywords': search_list
        }
        return JsonResponse(result)


def recommend_dish(request):
    if request.method == 'GET':
        dish = Dish.objects.order_by('-discount')[:3]
        dish_list = []
        for a_dish in dish:
            dish_dict = {
                'id':a_dish.id,
                'name': a_dish.name,
                'est_price': a_dish.estPrice,
                'order_count': a_dish.discount
            }
            dish_list.append(dish_dict)
        result = {
            'dishes': dish_list
        }
        return JsonResponse(result)


