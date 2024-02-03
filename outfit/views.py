from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from closet.models import ClosetClothes
from .models import Outfit, OutfitClothes,AllOutfits
import random

def choose_random_item(category_queryset):
    if category_queryset.exists():
        eligible_items = category_queryset.filter(worn_count__lte=3)
        if eligible_items:
            return random.choice(category_queryset)
        else:
            return None
    else:
        return None
@login_required    
def increment_worn_count(request):
    if request.method == 'POST':
        user_selection = request.POST.get('selection')
        if user_selection == "yes":
            try:
                outfit = Outfit.objects.filter(user_id=request.user.id).last()
            except Outfit.DoesNotExist:
                return HttpResponse("Outfit not found")

            # Get all clothes associated with the outfit
            outfit_clothes = OutfitClothes.objects.filter(outfit=outfit)
            clothes_to_increment = [oc.clothes for oc in outfit_clothes]

            # Check if any clothes exist in the queryset
            if clothes_to_increment:
                id_of_outfit = outfit.outfit_id
                all_outfit = AllOutfits.objects.create(outfit_id = id_of_outfit,user_id = request.user.id)
                for clothes in clothes_to_increment:
                    clothes.worn_count += 1
                    clothes.save()
                return redirect("home")
            else:
                return redirect("home")
        else:
            return redirect("home")
    else:
        return redirect("home")
    
def count(request):
    return render(request, "increment.html")


@login_required
def suggest_outfit(request):
    # Simulated weather data (replace with actual data retrieval)
    weather_data = {"temperature": 0, "humidity": 80, "wind_speed": 10, "rain_chance": "heavy"}

    suggested_items = []

    if weather_data["temperature"] < 10:
        suggested_items.extend([
            choose_random_item(ClosetClothes.objects.filter(user=request.user, subcategory__in=['jacket', 'hoodie'])),
            choose_random_item(ClosetClothes.objects.filter(user=request.user, subcategory__in=['t-shirt'])),
            choose_random_item(ClosetClothes.objects.filter(user=request.user, subcategory__in=['joggers', 'jeans'])),
            choose_random_item(ClosetClothes.objects.filter(user=request.user, subcategory__in=['boots', 'trainers']))
        ])
    elif 10 <= weather_data["temperature"] < 20:
        suggested_items.extend([
            choose_random_item(ClosetClothes.objects.filter(user=request.user, subcategory__in=['jacket', 'hoodie', 'coat'])),
            choose_random_item(ClosetClothes.objects.filter(user=request.user, subcategory__in=['t-shirt'])),
            choose_random_item(ClosetClothes.objects.filter(user=request.user, subcategory__in=['joggers', 'jeans'])),
            choose_random_item(ClosetClothes.objects.filter(user=request.user, subcategory__in=['boots', 'trainers', 'sneakers']))
        ])
    elif 20 <= weather_data["temperature"] < 30:
        suggested_items.extend([
            choose_random_item(ClosetClothes.objects.filter(user=request.user, subcategory__in=['t-shirt', 'shirt', 'hoodie'])),
            choose_random_item(ClosetClothes.objects.filter(user=request.user, subcategory__in=['jeans', 'shorts', 'pants'])),
            choose_random_item(ClosetClothes.objects.filter(user=request.user, subcategory__in=['trainers', 'sneakers']))
        ])

    user_id = request.user.id
    outfit = Outfit.objects.create(name= "user",user_id = user_id)
    for item in suggested_items:
         if item is not None:
            OutfitClothes.objects.create(clothes = item, outfit = outfit)
    return render(request, 'home.html', {'suggested_items': suggested_items, "user":user_id})
