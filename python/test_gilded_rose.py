# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose,BaseItem,AgedBrie


class TestBaseItem(unittest.TestCase):
    
    def test_base_item(self):
        items = [Item("foo",quality= 0,sell_in=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEquals("foo", items[0].name)
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(0, items[0].quality)

    def test_decreases_quality_by_normal_rate(self):
        items = [Item("Base",quality= 2,sell_in=1)]
        GildedRose(items).update_quality()
        
        self.assertEquals(1, items[0].quality)

    def test_decreases_quality_by_double_past_sell_in(self):
        items = [Item("Base",quality= 2,sell_in=-1)]
        GildedRose(items).update_quality()
        
        self.assertEquals(0, items[0].quality)
        
class TestAgedBrie(unittest.TestCase):
        
 

    def test_increases_quality_by_normal_rate(self):

        items = [Item("Aged Brie",quality= 2,sell_in=1)]
        GildedRose(items).update_quality()
        self.assertEquals(3, items[0].quality)
        
    def test_increases_quality_by_double_past_sell_in(self):
    
        items = [Item("Aged Brie",quality= 2,sell_in=-1)]
        GildedRose(items).update_quality()
        self.assertEquals(4, items[0].quality)
  
class TestAgedBrie(unittest.TestCase):
        

    def test_quality_no_change(self):

        items = [Item("Sulfuras, Hand of Ragnaros",quality= 2,sell_in=1)]
        GildedRose(items).update_quality()
        self.assertEquals(80, items[0].quality)
        
    def test_sell_in_no_change(self):
    
        items = [Item("Sulfuras, Hand of Ragnaros",quality= 2,sell_in=0)]
        GildedRose(items).update_quality()
        self.assertEquals(0, items[0].sell_in)
        
        
class TestBackStage(unittest.TestCase):     
    def test_increases_quality_by_normal_rate(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert",quality= 2,sell_in=100)]
        GildedRose(items).update_quality()
        self.assertEquals(3, items[0].quality)           
        
    def test_increases_quality_by_double_rate(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert",quality= 2,sell_in=10)]
        GildedRose(items).update_quality()
        self.assertEquals(4, items[0].quality)      
        
    def test_increases_quality_by_triple_rate(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert",quality= 2,sell_in=4)]
        GildedRose(items).update_quality()
        self.assertEquals(5, items[0].quality)   
class TestConjured(unittest.TestCase):     

    def test_increases_quality_by_double_rate(self):
        items = [Item("Conjured Mana Cake",quality= 2,sell_in=10)]
        GildedRose(items).update_quality()
        self.assertEquals(0, items[0].quality)      
            
    def test_decreases_quality_by_quadruple_past_sell_in(self):
        items = [Item("Conjured Mana Cake",quality= 4,sell_in=0)]
        GildedRose(items).update_quality()
        
        self.assertEquals(0, items[0].quality)
           
if __name__ == '__main__':

    unittest.main()
