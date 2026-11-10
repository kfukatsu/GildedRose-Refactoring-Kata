# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"


def update(name, sell_in, quality):
    """アイテムを1つ作り、1日分更新したものを返す。"""
    item = Item(name, sell_in, quality)
    GildedRose([item]).update_quality()
    return item


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)


class NormalItemTest(unittest.TestCase):
    def test_販売期限と品質が1ずつ下がる(self):
        item = update("foo", 10, 20)
        self.assertEqual((9, 19), (item.sell_in, item.quality))

    def test_販売期限を過ぎると品質は2倍の速さで下がる(self):
        item = update("foo", 0, 20)
        self.assertEqual((-1, 18), (item.sell_in, item.quality))

    def test_品質は負にならない(self):
        item = update("foo", 5, 0)
        self.assertEqual(0, item.quality)

    def test_販売期限切れでも品質は負にならない(self):
        item = update("foo", 0, 1)
        self.assertEqual(0, item.quality)


class AgedBrieTest(unittest.TestCase):
    def test_品質が1上がる(self):
        item = update(AGED_BRIE, 10, 20)
        self.assertEqual((9, 21), (item.sell_in, item.quality))

    def test_販売期限を過ぎると品質は2上がる(self):
        item = update(AGED_BRIE, 0, 20)
        self.assertEqual((-1, 22), (item.sell_in, item.quality))

    def test_品質は50を超えない(self):
        item = update(AGED_BRIE, 10, 50)
        self.assertEqual(50, item.quality)

    def test_販売期限切れでも品質は50を超えない(self):
        item = update(AGED_BRIE, 0, 49)
        self.assertEqual(50, item.quality)


class SulfurasTest(unittest.TestCase):
    def test_販売期限も品質も変わらない(self):
        item = update(SULFURAS, 10, 80)
        self.assertEqual((10, 80), (item.sell_in, item.quality))

    def test_販売期限切れでも変わらない(self):
        item = update(SULFURAS, -1, 80)
        self.assertEqual((-1, 80), (item.sell_in, item.quality))


class BackstagePassesTest(unittest.TestCase):
    def test_残り11日以上なら品質が1上がる(self):
        item = update(BACKSTAGE, 11, 20)
        self.assertEqual((10, 21), (item.sell_in, item.quality))

    def test_残り10日なら品質が2上がる(self):
        item = update(BACKSTAGE, 10, 20)
        self.assertEqual(22, item.quality)

    def test_残り6日なら品質が2上がる(self):
        item = update(BACKSTAGE, 6, 20)
        self.assertEqual(22, item.quality)

    def test_残り5日なら品質が3上がる(self):
        item = update(BACKSTAGE, 5, 20)
        self.assertEqual(23, item.quality)

    def test_残り1日なら品質が3上がる(self):
        item = update(BACKSTAGE, 1, 20)
        self.assertEqual(23, item.quality)

    def test_コンサート後は品質が0になる(self):
        item = update(BACKSTAGE, 0, 20)
        self.assertEqual((-1, 0), (item.sell_in, item.quality))

    def test_品質は50を超えない(self):
        for sell_in in (15, 10, 5):
            with self.subTest(sell_in=sell_in):
                item = update(BACKSTAGE, sell_in, 49)
                self.assertEqual(50, item.quality)


if __name__ == '__main__':
    unittest.main()
