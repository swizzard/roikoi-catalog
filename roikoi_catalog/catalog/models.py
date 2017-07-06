from django.db import models, IntegrityError


class Category(models.Model):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True)

    def save(self, *args, **kwargs):
        """
        Custom save method to prevent loops in category hierarchy and Item/Category confusion.
        """
        if self.parent.name == self.name:
            # technically error should be raised `if self.parent is self`,
            # but why not also prevent duplicate names?
            raise IntegrityError('Circular category reference')
        elif Item.objects.filter(title=self.name).exists():
            # Category and Item names must be distinct
            raise IntegrityError('Category shares name with item')
        else:
            super(Category).save()

    def is_top_level(self):
        return self.parent is None

    def __repr__(self):
        return '<Category: {}>'.format(self.name)


class Item(models.Model):
    title = models.TextField()
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='items',
                                 related_query_name='item')

    def save(self, *args, **kwargs):
        """
        Custom save method to prevent Item/Category confusion
        """
        if Category.objects.filter(name=self.title).exists():
            # Item and Category names must be distinct
            raise IntegrityError('Item shares name with category')

    def __repr__(self):
        return '<Item: {t} ({c})>'.format(t=self.title, c=self.category.name)

