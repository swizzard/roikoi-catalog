from django.db import models, IntegrityError


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True)

    @property
    def ancestors(self):
        ancestors = [self]
        curr = self
        while curr.parent is not None:
            ancestors.append(curr.parent)
            curr = curr.parent
        return list(reversed(ancestors))

    @property
    def children(self):
        return self.category_set.all()

    @property
    def items(self):
        return self.items.all()

    def __str__(self):
        return '<Category: {}>'.format(self.name)


class Item(models.Model):
    title = models.TextField(unique=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='items',
                                 related_query_name='item')

    def __str__(self):
        return '<Item: {t} ({c})>'.format(t=self.title, c=self.category.name)

