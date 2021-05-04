from django.db import models


class Products(models.Model):
    name = models.CharField('Название товара', max_length=300)
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)
    text = models.TextField('Текст', null=True)
    category = models.ForeignKey('product.Category', models.CASCADE, related_name='stuff_category', null=True)
    rating = models.PositiveSmallIntegerField('Рейтинг', default=0, null=True)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    category = models.CharField('Категория', max_length=100)

    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продуктов'

    def __str__(self):
        return f'{self.category}'


class ProductImage(models.Model):
    product = models.ForeignKey(Products, models.CASCADE, 'product_images')
    image = models.ImageField('Фото продукта', upload_to='product_image')


class ProductMark(models.Model):
    product = models.ForeignKey('Products', models.CASCADE, related_name='product_marks', null=True)
    user = models.ForeignKey('user.Profile', models.CASCADE, 'user_marks', null=True)
    mark = models.PositiveSmallIntegerField('Оценка', default=5)
    comment = models.TextField('Комментарий')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.comment}'
