from rest_framework.views import APIView, Request, Response, status
from .models import Group


class GroupView(APIView):
    def post(self, request: Request) -> Response:
        new_group: Group = Group.objects.create(**request.data)
        return Response(new_group.to_dict(), status.HTTP_201_CREATED)

    def get(self, _: Request) -> Response:
        return Response(Group.to_list_dict(), status.HTTP_200_OK)
