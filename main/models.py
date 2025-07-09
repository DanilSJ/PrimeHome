from django.db import models

class infomain(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    logo = models.ImageField(upload_to='logo/', verbose_name="Логотип", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk and infomain.objects.exists():
            raise Exception("Можно создать только одну запись infomain.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class CleaningAppliance(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=500, decimal_places=2, verbose_name="Цена")
    discount = models.DecimalField(max_digits=500, decimal_places=2, verbose_name="Скидка", blank=True, null=True)
    image = models.ImageField(upload_to='appliances/', verbose_name="Изображение", blank=True, null=True)
    features = models.TextField(verbose_name="Характеристики", blank=True, null=True)
    ozon_link = models.URLField(verbose_name="Ozon (ссылка)", blank=True, null=True)
    wildberries_link = models.URLField(verbose_name="Wildberries (ссылка)", blank=True, null=True)
    pdf = models.FileField(upload_to='appliances/pdfs/', verbose_name="PDF документ", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return self.name

class CookingAppliance(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Скидка", blank=True, null=True)
    image = models.ImageField(upload_to='appliances/', verbose_name="Изображение", blank=True, null=True)
    features = models.TextField(verbose_name="Характеристики", blank=True, null=True)
    ozon_link = models.URLField(verbose_name="Ozon (ссылка)", blank=True, null=True)
    wildberries_link = models.URLField(verbose_name="Wildberries (ссылка)", blank=True, null=True)
    pdf = models.FileField(upload_to='appliances/pdfs/', verbose_name="PDF документ", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return self.name

class Recipes(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='appliances/', verbose_name="Изображение", blank=True, null=True)
    download_link = models.URLField(verbose_name="Скачать (ссылка)", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return self.name

class Support(models.Model):
    working_time = models.CharField(max_length=255, verbose_name="Время работы")
    phone = models.CharField(max_length=255, verbose_name="Телефон")
    email = models.CharField(max_length=255, verbose_name="Email")
    
    whatsapp = models.CharField(max_length=255, verbose_name="WhatsApp")
    telegram = models.CharField(max_length=255, verbose_name="Telegram")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    
    def save(self, *args, **kwargs):
        if not self.pk and Support.objects.exists():
            raise Exception("Можно создать только одну запись Support.")
        super().save(*args, **kwargs)


class SupportFAQ(models.Model):
    name = models.CharField(max_length=255, verbose_name="Вопрос")
    description = models.TextField(verbose_name="Ответ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return self.name

class SupportQuestions(models.Model):
    name = models.CharField(max_length=255, verbose_name="Вопрос")
    email = models.CharField(max_length=255, verbose_name="Email")
    phone = models.CharField(max_length=255, verbose_name="Телефон")
    theme = models.CharField(max_length=255, verbose_name="Тема")
    description = models.TextField(verbose_name="Ответ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    
    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=255, verbose_name="Вопрос")
    email = models.CharField(max_length=255, verbose_name="Email")
    technic = models.CharField(max_length=255, verbose_name="Техника")
    description = models.TextField(verbose_name="Ответ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    
    def __str__(self):
        return self.name


