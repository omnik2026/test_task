from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Car, Comment
from .forms import CarForm, CommentForm, SignUpForm

# View для выхода из системы
def logout_view(request):
    logout(request)  # Выход пользователя из системы
    return redirect('login')  # Перенаправление на страницу входа

# View для отображения списка автомобилей
def car_list(request):
    cars = Car.objects.all()  # Получение всех автомобилей из базы данных
    return render(request, 'cars/car_list.html', {'cars': cars})  # Отображение списка автомобилей

# View для отображения деталей конкретного автомобиля
def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)  # Получение автомобиля по первичному ключу или возврат ошибки 404
    comments = car.comments.all()  # Получение всех комментариев к этому автомобилю
    if request.method == 'POST':  # Обработка POST-запроса для добавления комментария
        form = CommentForm(request.POST)  # Создание формы комментария с данными из POST-запроса
        if form.is_valid():  # Проверка валидности формы
            comment = form.save(commit=False)  # Сохранение формы без коммита в базу данных
            comment.car = car  # Установка связи комментария с автомобилем
            comment.author = request.user  # Установка автора комментария
            comment.save()  # Сохранение комментария в базу данных
            return redirect('car_detail', pk=car.pk)  # Перенаправление на страницу деталей автомобиля
    else:
        form = CommentForm()  # Создание пустой формы комментария
    return render(request, 'cars/car_detail.html', {'car': car, 'comments': comments, 'form': form})  # Отображение страницы деталей автомобиля

# View для создания нового автомобиля (требует аутентификации)
@login_required
def car_create(request):
    if request.method == 'POST':  # Обработка POST-запроса для создания автомобиля
        form = CarForm(request.POST)  # Создание формы автомобиля с данными из POST-запроса
        if form.is_valid():  # Проверка валидности формы
            car = form.save(commit=False)  # Сохранение формы без коммита в базу данных
            car.owner = request.user  # Установка владельца автомобиля
            car.save()  # Сохранение автомобиля в базу данных
            return redirect('car_detail', pk=car.pk)  # Перенаправление на страницу деталей автомобиля
    else:
        form = CarForm()  # Создание пустой формы автомобиля
    return render(request, 'cars/car_form.html', {'form': form})  # Отображение страницы создания автомобиля

# View для обновления существующего автомобиля (требует аутентификации)
@login_required
def car_update(request, pk):
    car = get_object_or_404(Car, pk=pk, owner=request.user)  # Получение автомобиля по первичному ключу и владельцу или возврат ошибки 404
    if request.method == 'POST':  # Обработка POST-запроса для обновления автомобиля
        form = CarForm(request.POST, instance=car)  # Создание формы автомобиля с данными из POST-запроса и существующим экземпляром
        if form.is_valid():  # Проверка валидности формы
            form.save()  # Сохранение изменений в базу данных
            return redirect('car_detail', pk=car.pk)  # Перенаправление на страницу деталей автомобиля
    else:
        form = CarForm(instance=car)  # Создание формы автомобиля с существующим экземпляром
    return render(request, 'cars/car_form.html', {'form': form})  # Отображение страницы обновления автомобиля

# View для удаления автомобиля (требует аутентификации)
@login_required
def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk, owner=request.user)  # Получение автомобиля по первичному ключу и владельцу или возврат ошибки 404
    if request.method == 'POST':  # Обработка POST-запроса для удаления автомобиля
        car.delete()  # Удаление автомобиля из базы данных
        return redirect('car_list')  # Перенаправление на страницу списка автомобилей
    return render(request, 'cars/car_confirm_delete.html', {'car': car})  # Отображение страницы подтверждения удаления автомобиля

# View для регистрации нового пользователя
def signup(request):
    if request.method == 'POST':  # Обработка POST-запроса для регистрации пользователя
        form = SignUpForm(request.POST)  # Создание формы регистрации с данными из POST-запроса
        if form.is_valid():  # Проверка валидности формы
            form.save()  # Сохранение нового пользователя в базу данных
            username = form.cleaned_data.get('username')  # Получение имени пользователя из очищенных данных формы
            raw_password = form.cleaned_data.get('password1')  # Получение пароля из очищенных данных формы
            user = authenticate(username=username, password=raw_password)  # Аутентификация пользователя
            login(request, user)  # Вход пользователя в систему
            return redirect('car_list')  # Перенаправление на страницу списка автомобилей
    else:
        form = SignUpForm()  # Создание пустой формы регистрации
    return render(request, 'registration/signup.html', {'form': form})  # Отображение страницы регистрации