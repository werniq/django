from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название новости")
    content = models.TextField(verbose_name="Контент новости", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания новости")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления новости")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Фото новости", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано?")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=25, verbose_name='Название категории', db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"
        ordering = ['title']
