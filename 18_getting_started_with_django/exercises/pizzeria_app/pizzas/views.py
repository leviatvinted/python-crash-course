from django.shortcuts import render
from .models import Pizza

# Create your views here.

def index(request):
    """The home page for the pizzeria app."""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Show all pizzas."""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """Show a single pizza and its toppings."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')  # type: ignore
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)
