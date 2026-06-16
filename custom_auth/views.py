from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password #обязательный содуль для расшифровки хешированных паролей

from .models import Users

def login(request):
    if request.method == 'GET': #если полльзователь открыл страницу,  то возвращаем рендеренную страниццу входа
        return render(request, 'login.html')
    
    if request.method == 'POST':
        received_username = request.POST.get('username')
        received_password = request.POST.get('password')

        try:
            found_user = Users.objects.get(username=received_username) #проверяем юз

            if check_password(received_password, found_user.password): #если введенный пароль совпадает
                request.session['logged_user_id'] = found_user.id #создаем сессию
                return redirect('home') #переводим юзера на главную
            
            else: #пароль не подошел
                return render(request, 'login.html', {'error': 'Неверный пароль!'})  
            
        except Users.DoesNotExist: #не найдено поле с таким username
            return render(request, 'login.html', {'error': 'Неверный логин!'})





