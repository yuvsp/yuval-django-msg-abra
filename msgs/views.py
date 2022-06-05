from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Msg
from .permissions import IsOwnerOrReadOnly, UserView
from .serializers import MsgSerializer
from .pagination import CustomPagination


# from .filters import MovieFilter


class ListCreateMsgAPIView(ListCreateAPIView):
    serializer_class = MsgSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly] #[UserView] #
    queryset = Msg.objects.filter(unread=1).values()
    # queryset = Msg.objects.all()
    # queryset = Msg.objects.filter(receiver=request.user).values()
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)


    # filterset_class = MovieFilter

    def perform_create(self, serializer):
        # Assign the user who created the msg
        serializer.save(creator=self.request.user)


class MsgsViewSet(ListCreateAPIView):
    queryset = Msg.objects.all()
    serializer_class = MsgSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Msg.objects.filter(receiver=user,unread = 1)

class ListCreateMsgAPIView(ListCreateAPIView):
    serializer_class = MsgSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly] #[UserView] #
    queryset = Msg.objects.filter(unread=1).values()
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)

    def perform_create(self, serializer):
        # Assign the user who created the msg
        serializer.save(creator=self.request.user)

class RetrieveUpdateDestroyMsgAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MsgSerializer
    queryset = Msg.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly] #[UserView]#


class RetrieveUpdateDestroyMsgUnreadAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MsgSerializer
    queryset = Msg.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly] #[UserView]#
