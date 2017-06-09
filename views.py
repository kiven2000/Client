from django.shortcuts import render
from django.http import JsonResponse
from food.models import Dish, Material, DishMat, WeightInterval
from supplier.models import Supplier, MatSellInfo

# Create your views here.


def search(request):
    # 判断来自客户的请求是否通过GET发送
    if request.method == 'GET':
        #获取GET请求中附带的查询关键字字符串,也就是search_str
        search_str = request.GET['search_str']
        #通过查询字符串在数据库查找相关的菜品，例如用户查找的的关键字为’番茄‘，将会根据数据库name字段查询到
        #相关的菜品，如’番茄炒蛋‘，’番茄XXX','XXX番茄XXX‘等，下面语句中的'name__contains= search_str’
        #意思是‘名字（name)包含（contains）’，为英文相应单词的直译.
        dishes = Dish.objects.filter(name__contains= search_str)
        #下句的意思同上，查询食材
        materials = Material.objects.filter(name__contains= search_str)
        #初始化一个空的菜品列表，用于保存需要的菜品信息
        dishes_list = []
        #遍历查询到的dishes
        for adish in dishes:
            #生成一个dish的字典
            dish_dict = {
                'id': adish.id,
                'name': adish.name,
                'estPrice': adish.estPrice,
                'discount': adish.discount,
                'like': adish.like
            }
            #把上面生成的单个菜品的字典加入菜品列表中
            dishes_list.append(dish_dict)
        # 初始化一个空的食材列表，用于保存需要的食材信息，原理同查询菜品
        material_list = []
        for amaterial in materials:
            material_dict = {
                'id': amaterial.id,
                'name': amaterial.name,
                'breed': amaterial.breed
            }
            material_list.append(material_dict)
        #把上述生成的菜品、食材列表整合成字典形式的结果，用于返回请求所需的JSON
        result = {
            'dishes': dishes_list,
            'materials': material_list
        }
        #返回
        return JsonResponse(result)


def get_dish_detail(request):
    if request.method == 'GET':
        a_dish = Dish.objects.get(id__exact=request.GET['id'])
        materials = a_dish.material_set.all()
        material_list = []
        for a_material in materials:
            a_dish_mat = DishMat.objects.get(dish__id=a_dish.id, material__id=a_material.id)
            a_weight_interval = WeightInterval.objects.get(dishmat=a_dish_mat)
            material_dict = {
                'id': a_material.id,
                'name': a_material.name,
                'breed': a_material.breed,
                'mean_weight': round(a_dish_mat.quantity * (
                    a_weight_interval.intervalMaxWeight +
                    a_weight_interval.intervalMinWeight
                )/2, 2),
                'unit': a_weight_interval.unit,
                'amount': a_dish_mat.quantity,
                'size': a_weight_interval.intervalNote,
                'supplier': DishMat.objects.get(dish=a_dish, material=a_material).supplier.name
            }
            material_list.append(material_dict)
        result = {
            'id': a_dish.id,
            'name': a_dish.name,
            'estPrice': a_dish.estPrice,
            'discount': a_dish.discount,
            'like': a_dish.like,
            'materials': material_list
        }
        return JsonResponse(result)


def search_material(request):
    if request.method == 'GET':
        search_str = request.GET['search_str']
        materials = Material.objects.filter(name__contains=search_str)
        material_list = []
        for a_material in materials:
            suppliers = a_material.supplier_set.all()
            for a_supplier in suppliers:
                a_mat_sell_info = MatSellInfo.objects.get(
                    supplier=a_supplier,
                    material=a_material
                )
                material_dict = {
                    'id': a_material.id,
                    'name': a_material.name,
                    'breed': a_material.breed,
                    'unit_price': round(a_mat_sell_info.unit_price, 2),
                    'unit': a_mat_sell_info.unit,
                    'supplier': a_supplier.name
                }
                material_list.append(material_dict)
        result = {
            'materials': material_list
        }
        return JsonResponse(result)
