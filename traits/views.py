from rest_framework.views import APIView, Request, Response, status
from .models import Trait
from .serializers import TraitSerializer


class TraitView(APIView):
    def post(self, request: Request) -> Response:
        serializer = TraitSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        new_trait = Trait.objects.create(**serializer.validated_data)
        serializer = TraitSerializer(new_trait)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, _: Request) -> Response:
        traits = Trait.objects.all()
        serializer = TraitSerializer(traits, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
