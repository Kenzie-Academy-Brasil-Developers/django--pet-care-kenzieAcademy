from rest_framework.views import APIView, Request, Response, status
from .models import Trait


class TraitView(APIView):
    def post(self, request: Request) -> Response:
        new_trait: Trait = Trait.objects.create(**request.data)
        return Response(new_trait.to_dict(), status.HTTP_201_CREATED)

    def get(self, _: Request) -> Response:
        return Response(Trait.to_list_dict(), status.HTTP_200_OK)
