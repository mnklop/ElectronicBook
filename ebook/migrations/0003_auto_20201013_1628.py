# Generated by Django 3.1.2 on 2020-10-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0002_book_inf_bookimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_inf',
            name='bookimage',
            field=models.ImageField(blank=True, default='books_photo/default.png', upload_to='books_photo', verbose_name='Фотография книги'),
        ),
    ]
