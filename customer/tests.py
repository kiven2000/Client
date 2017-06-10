from django.test import TestCase, Client
from random import randint
from customer.models import Customer, HistoryKeyword
from food.models import Dish, Material, DishMat, WeightInterval
from supplier.models import Supplier, MatSellInfo

# Create your tests here.


class CustomerTestCase(TestCase):
    def setUp(self):
        self.maxDiff = None
        a_customer0 = Customer.objects.create(
            password='123456',
            user_name='sysuye'
        )
        a_customer1 = Customer.objects.create(
            password='123456',
            user_name='weiqing'
        )
        a_customer2 = Customer.objects.create(
            password='123456',
            user_name='zouhy'
        )
        a_customer3 = Customer.objects.create(
            password='123456',
            user_name='wzc'
        )
        a_customer4 = Customer.objects.create(
            password='123456',
            user_name='wfy'
        )
        fan_qie_chao_dan = Dish.objects.create(
            estPrice=6.5,
            name="番茄炒蛋",
            discount=1.5,
            like=5,
            customer=a_customer0
        )
        fan_qie_tu_dou_pian = Dish.objects.create(
            estPrice=9,
            name="番茄土豆片",
            discount=2.5,
            like=3,
            customer=a_customer1
        )
        fan_qie_da_lu_mian = Dish.objects.create(
            estPrice=9,
            name="(外婆真传)番茄打卤面",
            discount=2.5,
            like=3,
            customer=a_customer2
        )
        hong_shao_niu_rou = Dish.objects.create(
            estPrice=19,
            name="红烧牛肉",
            discount=2.5,
            like=3,
            customer=a_customer3
        )
        suan_la_tu_dou_si = Dish.objects.create(
            estPrice=8,
            name="酸辣土豆丝",
            discount=1.5,
            like=4,
            customer=a_customer4
        )
        tang_cu_pai_gu = Dish.objects.create(
            estPrice=17,
            name="糖醋排骨",
            discount=2.5,
            like=5,
            customer=a_customer2
        )
        da_hong_fan_qie = Material.objects.create(
            name="番茄",
            breed="大红番茄"
        )
        fen_hong_fan_qie = Material.objects.create(
            name="番茄",
            breed="粉红番茄"
        )
        fan_hong_qie = Material.objects.create(
            name="番红茄",
            breed="粉红番红茄"
        )
        ji_dan = Material.objects.create(
            name="鸡蛋",
            breed="农家蛋"
        )
        ji_dan = Material.objects.create(
            name="鸡蛋",
            breed="农家蛋"
        )
        sha_jiang = Material.objects.create(
            name="姜",
            breed="沙姜"
        )
        zi_jiang = Material.objects.create(
            name="姜",
            breed="子姜"
        )
        lao_jiang = Material.objects.create(
            name="姜",
            breed="老姜"
        )
        pin_tai = Supplier.objects.create(
            name="品泰贸易有限公司"
        )
        lian_gui = Supplier.objects.create(
            name="连贵-蔬菜档"
        )
        MatSellInfo.objects.create(
            unit_price=8,
            in_stock=True,
            supplier=lian_gui,
            material=ji_dan,
            unit="元/kg"
        )
        MatSellInfo.objects.create(
            unit_price=3,
            in_stock=True,
            supplier=pin_tai,
            material=da_hong_fan_qie,
            unit="元/kg"
        )
        MatSellInfo.objects.create(
            unit_price=20,
            in_stock=True,
            supplier=lian_gui,
            material=sha_jiang,
            unit="元/kg"
        )
        MatSellInfo.objects.create(
            unit_price=25,
            in_stock=True,
            supplier=pin_tai,
            material=zi_jiang,
            unit="元/kg"
        )
        MatSellInfo.objects.create(
            unit_price=16,
            in_stock=True,
            supplier=lian_gui,
            material=lao_jiang,
            unit="元/kg"
        )
        da_hong_fan_qie_wei_int0 = WeightInterval.objects.create(
            intervalMaxWeight=0.15,
            intervalMinWeight=0.1,
            material=da_hong_fan_qie,
            intervalNote="小",
            unit="kg/个"
        )
        da_hong_fan_qie_wei_int1 = WeightInterval.objects.create(
            intervalMaxWeight=0.2,
            intervalMinWeight=0.15,
            material=da_hong_fan_qie,
            intervalNote="中",
            unit="kg/个"
        )
        da_hong_fan_qie_wei_int2 = WeightInterval.objects.create(
            intervalMaxWeight=0.25,
            intervalMinWeight=0.2,
            material=da_hong_fan_qie,
            intervalNote="大",
            unit="kg/个"
        )
        ji_dan_wei_int = WeightInterval.objects.create(
            intervalMaxWeight=0.1,
            intervalMinWeight=0.05,
            material=ji_dan,
            intervalNote="",
            unit="kg/个"
        )
        DishMat.objects.create(
            dish=fan_qie_chao_dan,
            material=da_hong_fan_qie,
            unit="个",
            quantity=2,
            weightInterval=da_hong_fan_qie_wei_int1,
            supplier=lian_gui
        )
        DishMat.objects.create(
            dish=fan_qie_chao_dan,
            material=ji_dan,
            unit="个",
            quantity=4,
            weightInterval=ji_dan_wei_int,
            supplier=pin_tai
        )
        customer_list = [a_customer0, a_customer1, a_customer2, a_customer3, a_customer4]
        keywords = [
            '番茄炒蛋',
            '酸辣土豆丝',
            '土豆烧牛肉',
            '黑椒牛肉',
            '回锅肉',
            '青瓜炒肉',
            '苦瓜炒蛋',
            '黑椒牛肉',
            '番茄鸡蛋汤',
            '青椒炒鱿鱼',
            '苦瓜',
            '牛肉',
            '番茄',
            '青椒'
        ]
        keyword_types = [
            [True, False],
            [True, False],
            [True, False],
            [True, False],
            [True, False],
            [True, False],
            [True, False],
            [True, False],
            [True, False],
            [True, False],
            [True, True],
            [True, True],
            [True, True],
            [True, True]
        ]
        counter = 0
        for a_keyword in keywords:
            HistoryKeyword.objects.create(
                keyword=a_keyword,
                search_count=25-counter,
                dish_type=keyword_types[counter][0],
                mat_type=keyword_types[counter][1]
            ).customers.add(customer_list[randint(0,2)], customer_list[randint(3,4)])
            counter += 1

    def test_return_five_top_search_dish(self):
        c = Client()
        resp = c.get('/top_search_dish/')
        exp_json = {
            'search_keywords': [
                {
                    'keyword': '番茄炒蛋'
                },
                {
                    'keyword': '酸辣土豆丝'
                },
                {
                    'keyword': '土豆烧牛肉'
                },
                {
                    'keyword': '黑椒牛肉'
                },
                {
                    'keyword': '回锅肉'
                }
            ]
        }
        self.assertJSONEqual(str(resp.content, encoding='utf8'), exp_json)
        self.fail('完成测试！')




    def test_recommend_three_dishes(self):
        c = Client()
        resp = c.get('/recommend_dish/')
        resp_json = resp.json()
        self.assertIn('dishes', resp_json)
        dish_list = resp_json['dishes']
        self.assertEqual(len(dish_list), 3)
        for a_dish in dish_list:
            self.assertIn('id', a_dish)
            self.assertIn('name', a_dish)
            self.assertIn('est_price', a_dish)
            self.assertIn('order_count', a_dish)
        self.fail('完成测试！')



