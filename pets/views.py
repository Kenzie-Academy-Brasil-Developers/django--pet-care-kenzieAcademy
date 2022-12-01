from rest_framework.views import APIView, Request, Response, status
from .models import Pet


class PetView(APIView):
    def post(self, request: Request) -> Response:
        new_pet: Pet = Pet.objects.create(**request.data)
        return Response(new_pet.to_dict(), status.HTTP_201_CREATED)

    def get(self, _: Request) -> Response:
        return Response(Pet.to_list_dict(), status.HTTP_200_OK)
