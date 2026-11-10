# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"

MAX_QUALITY = 50
MIN_QUALITY = 0


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
            self._update_aged_brie(item)
        elif item.name == BACKSTAGE_PASSES:
            self._update_backstage_passes(item)
        else:
            self._update_normal_item(item)

    def _update_aged_brie(self, item):
        self._increase_quality(item)
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            self._increase_quality(item)

    def _update_backstage_passes(self, item):
        self._increase_quality(item)
        if item.sell_in < 11:
            self._increase_quality(item)
        if item.sell_in < 6:
            self._increase_quality(item)
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = MIN_QUALITY

    def _update_normal_item(self, item):
        self._decrease_quality(item)
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            self._decrease_quality(item)

    @staticmethod
    def _increase_quality(item):
        if item.quality < MAX_QUALITY:
            item.quality = item.quality + 1

    @staticmethod
    def _decrease_quality(item):
        if item.quality > MIN_QUALITY:
            item.quality = item.quality - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
