from django.db import models
# Create your models here.
class RestaurantType(models.Model):
    restaurant_type = models.CharField(max_length=20)
    def __str__(self):
        return (self.restaurant_type)
    
    class Meta:
        db_table = 'restaurant_type'

class RestaurantStyle(models.Model):
    restaurant_type = models.ForeignKey(RestaurantType, null=True, on_delete=models.SET_NULL)
    restaurant_style = models.CharField(max_length=30)
    def __str__(self):
        return (self.restaurant_specs)

    @property
    def restaurant_specs(self):
        return '%s - %s' % (self.restaurant_style, self.restaurant_type)

    class Meta:
        db_table = 'restaurant_style'

class Restaurant(models.Model):
    restaurant_type_style = models.ForeignKey(RestaurantStyle, null=True, on_delete=models.SET_NULL)
    restaurant_name = models.CharField(max_length=30)
    restaurant_street = models.CharField(max_length=30)
    def __str__(self):
        return (self.restaurant_info)
    
    @property
    def restaurant_info(self):
        return '%s - %s' % (self.restaurant_name, self.restaurant_street)

    class Meta:
        db_table = 'restaurant'