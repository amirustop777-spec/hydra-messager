from django.shortcuts import render

from custom_auth.models import Users
from .models import Quote

def welcome_index(request):
    users_count = Users.objects.count()
    random_quote = Quote.objects.order_by('?').first()
    context = {'users_count': users_count, 'random_quote': random_quote}
    return render(request, 'welcome.html', context)
