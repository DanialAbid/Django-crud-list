from django.db import models

# Create your models here.
class category(models.Model):
    categoryname = models.CharField(max_length=100)
    is_featured = models.BooleanField()

    def __str__(self):
        return f"{self.categoryname}"


class product(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    pname = models.CharField(max_length=200)
    pprice = models.IntegerField()
    pimage = models.ImageField(upload_to='products')
    quantity = models.IntegerField()


    def __str__(self):
        return f"{self.pname}"




