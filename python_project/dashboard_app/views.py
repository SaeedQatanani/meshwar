from django.shortcuts import render

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
    return render(request, 'new_activity.html')

#function for 'show/<int:activity_id>/' route - Imas
def show_activity(request, activity_id):
    return render(request, 'show_activity.html', activity_id)

#function for 'edit/<int:activity_id>/' route - Reina
def edit_activity(request, activity_id):
    return render(request, 'edit_activity.html', activity_id)

def about_us(request):
    return render(request, 'about_us.html')