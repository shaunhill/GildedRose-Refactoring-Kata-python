# -*- coding: utf-8 -*-

from re import L
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class BaseItem(Item):
    max_quality = 50


    def __init__(self, item):
        self.item = item
        
    def increase_quality(self):
        if self.item.quality < self.max_quality:
            self.item.quality = self.item.quality + 1

    def decrease_quality(self):
        if self.item.quality > 0:
            self.item.quality = self.item.quality - 1

    def decrease_sell_in(self):
        self.item.sell_in = self.item.sell_in - 1

    def update_quality(self):
        self.decrease_quality()
    
        if self.item.sell_in <= 0:
            self.decrease_quality()
                   
class AgedBrie(BaseItem):
    def update_quality(self):
        self.increase_quality()

        if self.item.sell_in <= 0:
            self.increase_quality()

class Sulfuras(BaseItem):
    
    def update_quality(self):
        self.item.quality = 80
    
    def decrease_sell_in(self):
        pass


class BackStage(BaseItem):
    days_threshold_min = 10
    days_threshold_max = 5

    def reset_quality(self):
        self.item.quality = 0

    def update_quality(self):
        self.increase_quality()
        if self.item.sell_in <= self.days_threshold_min:
            self.increase_quality()
        if self.item.sell_in <= self.days_threshold_max:
            self.increase_quality()
        if self.item.sell_in <= 0:
            self.reset_quality()
            
class Conjured(BaseItem):
    def update_quality(self):
        BaseItem.update_quality(self)
        BaseItem.update_quality(self)
        
         
class ItemFactory:
    class_mapping = {
        "Aged Brie": AgedBrie,
        "Sulfuras, Hand of Ragnaros": Sulfuras,
        "Backstage passes to a TAFKAL80ETC concert" :BackStage,
        "Conjured Mana Cake": Conjured
        }

    @classmethod
    def create(cls, item):
        if item.name in cls.class_mapping:
            return cls.class_mapping[item.name](item)
        return BaseItem(item)


class GildedRose:
    
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            gr_item = ItemFactory.create(item)
            gr_item.update_quality()
            gr_item.decrease_sell_in()
