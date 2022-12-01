from rest_framework.views import APIView, Request, Response, status
from .models import Group
from .serializers import GroupSerializer


class GroupView(APIView):
    def post(self, request: Request) -> Response:
        serializer = GroupSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        new_group = Group.objects.create(**serializer.validated_data)
        serializer = GroupSerializer(new_group)

        return Response(serializer.data, status.HTTP_200_OK)

    def get(self, _: Request) -> Response:
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
