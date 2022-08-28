from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from ads.models import User
from ads.serializers.users import UserSerializer, UserCreateSerializer, UserUpdateSerializer, UserDeleteSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # model = User
    # queryset = User.objects.all()
    #
    # def get(self, request, *args, **kwargs):
    #     super().get(request, *args, **kwargs)
    #     self.object_list = self.object_list.prefetch_related("locations").annotate(
    #         total_ads=Count('ad__is_published', filter=Q(ad__is_published=True))
    #     ).order_by('username')
    #
    #     paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGES)
    #     page_number = request.GET.get('page')
    #     page_obj = paginator.get_page(page_number)
    #
    #     users = []
    #     for user in page_obj:
    #         users.append({
    #             'id': user.id,
    #             'username': user.username,
    #             'first_name': user.first_name,
    #             'last_name': user.last_name,
    #             'role': user.role,
    #             'age': user.age,
    #             'locations': list(user.locations.all().values_list('name', flat=True)),
    #             'total_ads': user.total_ads,
    #         })
    #
    #     response = [{
    #         'items': users,
    #         'num_pages': paginator.num_pages,
    #         'total': paginator.count,
    #     }]
    #     return JsonResponse(response, safe=False)


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer
