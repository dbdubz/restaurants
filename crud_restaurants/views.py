from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def add_form(req):
    if (req.method == 'POST'):
        restaurant = Restaurant()
        restaurant.restaurant_name = req.POST.get('restaurant_name')
        restaurant.restaurant_street = req.POST.get('restaurant_street')
        restaurant.restaurant_type_style = RestaurantStyle.objects.get(id = req.POST.get('restaurant_style'))
        
        restaurant.save()
    styles = RestaurantStyle.objects.all().order_by('restaurant_style', 'restaurant_type')
    context = {
        'styles': styles
    }
    return render(req, 'restaurants/add.html', context)  

def delete_form(req):
    if (req.method == 'POST'):
        if (req.POST.get('to_delete') == 'individual'):
            rest_id = req.POST.get('rest_id')

            restaurant = Restaurant.objects.get(id=rest_id)
        else:
            restaurant = Restaurant.objects.filter(restaurant_name=req.POST.get('rest_name'))
            
        restaurant.delete()

    distinct_restaurants = Restaurant.objects.distinct('restaurant_name')
    restaurants = Restaurant.objects.all()

    context = {
        'distinct_restaurants': distinct_restaurants,
        'restaurants': restaurants
    }
                
    return render(req, 'restaurants/delete.html', context)   

def restaurants_index(req):
    if (req.method == "POST"):
        if (req.POST.get('to_do') == 'delete'):
            rest_del = Restaurant.objects.get(id=req.POST.get('rest_id'))
            rest_del.delete()
            
            try:
                rest_ts = req.POST.get['restaurant_type_style']
                if (rest_ts != 'all'):
                    filter_style = RestaurantStyle.objects.filter(id=rest_ts)
                    restaurants = Restaurant.objects.filter(restaurant_type_style = rest_ts)
                else:
                    filter_style = {'all'}
                    restaurants = Restaurant.objects.all()
            except:
                filter_style = {'all'}
                restaurants = Restaurant.objects.all()
            
            restaurants = restaurants.order_by('restaurant_name', 'restaurant_street')
        else:
            rest_del = Restaurant.objects.get(id=req.POST.get('rest_id'))
            rest_del.delete()
            try:
                rest_ts = req.POST.get['restaurant_type_style']
                if (rest_ts != 'all'):
                    filter_style = RestaurantStyle.objects.filter(id=rest_ts)
                    restaurants = Restaurant.objects.filter(restaurant_type_style = rest_ts)
                else:
                    filter_style = {'all'}
                    restaurants = Restaurant.objects.all()
            except:
                filter_style = {'all'}
                restaurants = Restaurant.objects.all()
            
            restaurants = restaurants.order_by('restaurant_name', 'restaurant_street')
    else:
        try:
            rest_ts = req.GET['restaurant_type_style']
            if (rest_ts != 'all'):
                filter_style = RestaurantStyle.objects.filter(id=rest_ts)
                restaurants = Restaurant.objects.filter(restaurant_type_style = rest_ts)
            else:
                filter_style = {'all'}
                restaurants = Restaurant.objects.all()
        except:
            filter_style = {'all'}
            restaurants = Restaurant.objects.all()

        restaurants = restaurants.order_by('restaurant_name', 'restaurant_street')
    
    styles = RestaurantStyle.objects.all().order_by('restaurant_style', 'restaurant_type')

    context = {
        'restaurants': restaurants,
        'type_styles': styles,
        'selected': filter_style
    }
    return render(req, 'restaurants/restaurants.html', context)

def update_form(req):
    if (req.method == 'POST'):
        rest_id = req.POST.get('rest_id')

        restaurant = Restaurant.objects.get(id=rest_id)
        
        if (req.POST.get('restaurant_name') != "1234567890"):
            restaurant.restaurant_name = req.POST.get('restaurant_name')
        else:
            restaurant.restaurant_street = req.POST.get('restaurant_street')

        
        restaurant.save()

    restaurants = Restaurant.objects.all().order_by('restaurant_name', 'restaurant_street')

    context = {
        'restaurants': restaurants
    }
    
    return render(req, 'restaurants/update.html', context)

def edit_index(req):
    if (req.method == 'POST'):
        return_path = req.path.replace('edit', "")

        rest_id = req.POST.get('rest_id')

        restaurant = Restaurant.objects.get(id=rest_id)
        
        if (req.POST.get('restaurant_name') != "1234567890"):
            restaurant.restaurant_name = req.POST.get('restaurant_name')
        else:
            restaurant.restaurant_street = req.POST.get('restaurant_street')

        restaurant.save()

        context = {
            'restaurant': restaurant
        }
        send = redirect(return_path)
    else:
        rest_id = req.GET['rest_id']
        #return_path = req.path.replace('edit', "")

        restaurant = Restaurant.objects.get(id=rest_id)

        context = {
            'restaurant': restaurant
        }

        send = render(req, 'restaurants/edit.html', context)

    return send

def landing_page(req):
    return render(req, 'restaurants/index.html')

def about_page(req):
    return render(req, 'restaurants/about.html')