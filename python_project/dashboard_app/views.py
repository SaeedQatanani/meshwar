from django.contrib import messages
from django.shortcuts import redirect, render
from .models import City, Activity
from login_app.models import User

#function for '' route - Imas
def dashboard(request):
    return render(request, 'dashboard.html')

#function for '<int:city_id>/' route - Reina
def city_dashboard(request, city_id):
    return render(request, 'city_dashboard.html', city_id)

#function for 'profile/<int:user_id>/' route - Karam
def show_profile(request, user_id):
    return render(request, 'profile.html', user_id)

#function for 'new/' route - Saeed
def new_activity(request):
    context = {
        'cities' : City.objects.all()
    }
    return render(request, 'new_activity.html', context)

#function for 'show/<int:activity_id>/' route - Imas
def show_activity(request, activity_id):
    context ={
        'activity' : Activity.objects.get(id = activity_id),
    }
    return render(request, 'show_activity.html', context)

#function for 'edit/<int:activity_id>/' route - Reina
def edit_activity(request, activity_id):
    return render(request, 'edit_activity.html')

def about_us(request):
    return render(request, 'about_us.html')

def create_activity(request):
    errors = Activity.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/dashboard/new')
    else:
        user = User.objects.filter(id = request.session['id'])
        if user: 
            logged_user = user[0]
            activity_city = City.objects.get(id = int(request.POST['city']))
            new_activity = Activity.objects.create(title = request.POST['title'],
                        location = request.POST['location'],
                        start_date = request.POST['start_date'],
                        end_date = request.POST['end_date'],
                        desc = request.POST['description'],
                        price = request.POST['price'],
                        added_by = logged_user,
                        city = activity_city,
                        )
        return redirect(f'/dashboard/show/{new_activity.id}')