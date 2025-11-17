from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for the Meal Planner App."""
    return render(request, 'meal_plans/index.html')
