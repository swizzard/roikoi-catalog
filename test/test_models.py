from django.test import TestCase
from catalog import models

class TestCategory(TestCase):
    def setUp(self):
        top = models.Category.objects.create(name='top')
        child = models.Category.objects.create(name='child', parent=top)
        grandchild = models.Category.objects.create(name='grandchild', parent=child)
        item = models.Item.objects.create(title='item', category=grandchild)

    def test_ancestors(self):
        top = models.Category.objects.get(name='top')
        self.assertEqual(top.ancestors, [top])

        child = models.Category.objects.get(name='child')
        self.assertEqual(child.ancestors, [top, child])

        grandchild = models.Category.objects.get(name='grandchild')
        self.assertEqual(grandchild.ancestors, [top, child, grandchild])

    def test_items(self):
        cat = models.Category.objects.get(name='grandchild')
        cat_items = list(cat.items.all())
        item = models.Item.objects.get(title='item')
        self.assertEqual(cat_items, [item])

