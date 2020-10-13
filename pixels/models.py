from django.db import models


class Pixel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    Location=models.TextField(max_length=30,null=False,blank=False)
    Category=models.TextField(max_length=30)
    pud_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.summary

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news

class Category(models.Model):
    category = models.CharField(max_length=80, null= True)
    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()
    def update_category(self):
        self.update()
    def __str__(self):
        return self.category
