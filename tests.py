from django.test import TestCase, Client
from food.models import Dish, Material, DishMat, WeightInterval
from supplier.models import Supplier, MatSellInfo

# Create your tests here.


class DishMaterialTestCase(TestCase):
    def setUp(self):
        self.maxDiff = None
        fan_qie_chao_dan = Dish.objects.create(
            estPrice=6.5,
            name="番茄炒蛋",
            discount=1.5,
            like=5
        )
        fan_qie_tu_dou_pian = Dish.objects.create(
            estPrice=9,
            name="番茄土豆片",
            discount=2.5,
            like=3
        )
        fan_qie_da_lu_mian = Dish.objects.create(
            estPrice=9,
            name="(外婆真传)番茄打卤面",
            discount=2.5,
            like=3
        )
        hong_shao_niu_rou = Dish.objects.create(
            estPrice=19,
            name="红烧牛肉",
            discount=2.5,
            like=3
        )
        suan_la_tu_dou_si = Dish.objects.create(
            estPrice=8,
            name="酸辣土豆丝",
            discount=1.5,
            like=4
        )
        tang_cu_pai_gu = Dish.objects.create(
            estPrice=17,
            name="糖醋排骨",
            discount=2.5,
            like=5
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

    def test_search_fan_qie_return_corresponding_dish_material(self):
        c = Client()
        resp = c.get('/search/', {'search_str': '番茄'})
        resp_json = resp.json()
        dishes = resp_json['dishes']
        self.assertEqual(len(dishes), 3)
        self.assertIn('id', dishes[0])
        self.assertEqual(dishes[0]['name'], '番茄炒蛋')
        self.assertEqual(dishes[0]['estPrice'], 6.5)
        self.assertEqual(dishes[0]['discount'], 1.5)
        self.assertEqual(dishes[0]['like'], 5)
        self.assertIn('id', dishes[1])
        self.assertEqual(dishes[1]['name'], '番茄土豆片')
        self.assertEqual(dishes[1]['estPrice'], 9)
        self.assertEqual(dishes[1]['discount'], 2.5)
        self.assertEqual(dishes[1]['like'], 3)
        self.assertIn('id', dishes[2])
        self.assertEqual(dishes[2]['name'], '(外婆真传)番茄打卤面')
        self.assertEqual(dishes[2]['estPrice'], 9)
        self.assertEqual(dishes[2]['discount'], 2.5)
        self.assertEqual(dishes[2]['like'], 3)
        materials = resp_json['materials']
        self.assertEqual(len(materials), 2)
        self.assertIn('id', materials[0])
        self.assertEqual(materials[0]['name'], '番茄')
        self.assertEqual(materials[0]['breed'], '大红番茄')
        self.assertIn('id', materials[1])
        self.assertEqual(materials[1]['name'], '番茄')
        self.assertEqual(materials[1]['breed'], '粉红番茄')
        self.fail('测试完成!')

    def test_return_the_right_dish_detail_giving_dishid(self):
        a_dish = Dish.objects.get(name__exact='番茄炒蛋')
        c = Client()
        resp = c.get('/get_dish_detail/', {'id': a_dish.id})
        resp_json = resp.json()
        self.assertIn('materials', resp_json)
        self.assertEqual(len(resp_json['materials']), 2)
        exp_json = {
            'id': resp_json['id'],
            'name': '番茄炒蛋',
            'estPrice': 6.5,
            'discount': 1.5,
            'like': 5,
            'materials': [
                {
                    'id': resp_json['materials'][0]['id'],
                    'name': '番茄',
                    'breed': '大红番茄',
                    'mean_weight': 0.35,
                    'unit': 'kg/个',
                    'amount': 2,
                    'size': '中',
                    'supplier': '连贵-蔬菜档'
                },
                {
                    'id': resp_json['materials'][1]['id'],
                    'name': '鸡蛋',
                    'breed': '农家蛋',
                    'mean_weight': 0.3,
                    'unit': 'kg/个',
                    'amount': 4,
                    'size': '',
                    'supplier': '品泰贸易有限公司'
                }
            ]
        }
        self.assertJSONEqual(str(resp.content, encoding='utf8'), exp_json)
        self.fail('测试完成!')

    def test_search_jiang_can_return_corresponding_material(self):
        c = Client()
        resp = c.get('/search_material/', {'search_str': '姜'})
        resp_json = resp.json()
        self.assertEqual(len(resp_json['materials']), 3)
        exp_json = {
            'materials': [
                {
                    'id': resp_json['materials'][0]['id'],
                    'name': '姜',
                    'breed': '沙姜',
                    'unit_price': 20.00,
                    'unit': '元/kg',
                    'supplier': '连贵-蔬菜档'
                },
                {
                    'id': resp_json['materials'][1]['id'],
                    'name': '姜',
                    'breed': '子姜',
                    'unit_price': 25.00,
                    'unit': '元/kg',
                    'supplier': '品泰贸易有限公司'
                },
                {
                    'id': resp_json['materials'][2]['id'],
                    'name': '姜',
                    'breed': '老姜',
                    'unit_price': 16.00,
                    'unit': '元/kg',
                    'supplier': '连贵-蔬菜档'
                }
            ]
        }
        self.assertJSONEqual(str(resp.content, encoding='utf8'), exp_json)
        self.fail('测试完成!')

    def test_add_material_to_dish(self):
        lao_jiang = Material.objects.get(breed='老姜')
        fan_qie_chao_dan = Dish.objects.get(name='番茄炒蛋')
        c = Client()
        resp = c.post('/add_material_to_dish/', {
            'material_id': lao_jiang.id,
            'dish_id': fan_qie_chao_dan
        })
        resp_json = resp.json()
        exp_json = {
            'success': True,
            'str': '番茄炒蛋 食材+1'
        }
        self.assertJSONEqual(resp_json, exp_json)
        self.assertEqual(
            len(Dish.objects.get(id=fan_qie_chao_dan.id).material_set.filter(id=lao_jiang.id)),
            1
        )
        self.fail('测试完成!')

    def test_get_dish_material_info_opts(self):
        c = Client()
        resp = c.get('/get_dish_material_info_opts/')

    def  test_get_dish_detail_after_add_lao_jiang(self):
        a_dish = Dish.objects.get(name__exact='番茄炒蛋')
        c = Client()
        resp = c.get('/get_dish_detail/', {'id': a_dish.id})
        resp_json = resp.json()
        self.assertIn('materials', resp_json)
        self.assertEqual(len(resp_json['materials']), 2)
        exp_json = {
            'id': resp_json['id'],
            'name': '番茄炒蛋',
            'estPrice': 6.5,
            'discount': 1.5,
            'like': 5,
            'materials': [
                {
                    'id': resp_json['materials'][0]['id'],
                    'name': '番茄',
                    'breed': '大红番茄',
                    'mean_weight': 0.35,
                    'unit': 'kg/个',
                    'amount': 2,
                    'size': '中',
                    'supplier': '连贵-蔬菜档'
                },
                {
                    'id': resp_json['materials'][1]['id'],
                    'name': '鸡蛋',
                    'breed': '农家蛋',
                    'mean_weight': 0.3,
                    'unit': 'kg/个',
                    'amount': 4,
                    'size': '',
                    'supplier': '品泰贸易有限公司'
                },
                {
                    'id': resp_json['materials'][2]['id'],
                    'name': '姜',
                    'breed': '老姜',
                    'mean_weight': 0.3,
                    'unit': '',
                    'amount': -1,
                    'size': '',
                    'supplier': '品泰贸易有限公司'
                }
            ]
        }
        self.assertJSONEqual(str(resp.content, encoding='utf8'), exp_json)
        self.fail('测试完成!')
