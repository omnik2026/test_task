from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Car, Comment
from .serializers import CarSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

# View для создания и отображения списка автомобилей
class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()  # Запрос для получения всех автомобилей
    serializer_class = CarSerializer  # Сериализатор для автомобилей
    permission_classes = [IsAuthenticatedOrReadOnly]  # Права доступа: только аутентифицированные пользователи могут создавать, остальные могут только читать

    def perform_create(self, serializer):
        # Метод для сохранения владельца автомобиля как текущего пользователя
        serializer.save(owner=self.request.user)

# View для просмотра, обновления и удаления конкретного автомобиля
class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()  # Запрос для получения всех автомобилей
    serializer_class = CarSerializer  # Сериализатор для автомобилей
    permission_classes = [IsOwnerOrReadOnly]  # Права доступа: только владелец может обновлять или удалять, остальные могут только читать

# View для создания и отображения списка комментариев к конкретному автомобилю
class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer  # Сериализатор для комментариев
    permission_classes = [IsAuthenticatedOrReadOnly]  # Права доступа: только аутентифицированные пользователи могут создавать, остальные могут только читать

    def get_queryset(self):
        # Метод для получения всех комментариев, связанных с конкретным автомобилем
        return Comment.objects.filter(car_id=self.kwargs['car_pk'])

    def perform_create(self, serializer):
        # Метод для сохранения автора комментария как текущего пользователя и связывания комментария с конкретным автомобилем
        serializer.save(author=self.request.user, car_id=self.kwargs['car_pk'])