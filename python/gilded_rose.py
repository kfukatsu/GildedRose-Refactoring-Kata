# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self._update_item(item)

    def _update_item(self, item):
        if item.name == SULFURAS:
            return
        if item.name == AGED_BRIE:
            if item.quality < 50:
                item.quality = item.quality + 1
            item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.quality < 50:
                    item.quality = item.quality + 1
        elif item.name == BACKSTAGE_PASSES:
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.sell_in < 11:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                if item.sell_in < 6:
                    if item.quality < 50:
                        item.quality = item.quality + 1
            item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                item.quality = item.quality - item.quality
        else:
            if item.quality > 0:
                item.quality = item.quality - 1
            item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.quality > 0:
                    item.quality = item.quality - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
