from rest_framework.views import APIView, Request, Response, status
from .models import Pet
from .serializers import PetSerializer


class PetView(APIView):
    def post(self, request: Request) -> Response:
        serializer = PetSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        new_pet = Pet.objects.create(**serializer.validated_data)
        serializer = PetSerializer(new_pet)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, _: Request) -> Response:
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
