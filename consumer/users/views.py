from flask import request
import httpx

from django.shortcuts import render
from django.http import HttpResponse

async def index(request):
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/users/users/", auth=('admin', 'password'))
    users = response.json()
    return render(request, 'users/index.html', {'users': users})

async def list_of_users(request, pk):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/users/users/{pk}/?format=json", auth=('admin', 'password'))

    users = response.json()
    user_profile_link = f"http://localhost:7000/users/users/{pk}/"

    context = {
        "users": users, 
        "user_profile_link": user_profile_link}

    return render(request, 'users/users.html', context)


async def user_info_view(request, pk):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/users/users/{pk}/?format=json", auth=('admin', 'password'))
        
    user = response.json()
    user_profile_link = f"http://localhost:7000/users/users/{pk}/"
    
    context = {
        'user': user,
        'user_profile_link': user_profile_link
    }
    
    return render(request, 'users/user-info.html', context)

async def list_of_books(request):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/users/books/?format=json", auth=('admin', 'password'))

    books = response.json()
    # book_detail_link = f"http://localhost:7000/users/books/{pk}/"

    context = {
        "books": books, 
        # "book_profile_link": book_detail_link
        }

    return render(request, 'users/books.html', context)

async def list_of_cars(request):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/users/cars/?format=json", auth=('admin', 'password'))

    cars = response.json()
    # car_detail_link = f"http://localhost:7000/users/cars/{pk}/"

    context = {
        "cars": cars, 
        # "car_profile_link": car_detail_link
        }

    return render(request, 'users/cars.html', context)