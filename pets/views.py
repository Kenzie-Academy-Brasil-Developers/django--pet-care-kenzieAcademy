from rest_framework.views import APIView, Request, Response, status


class PetView(APIView):
    def post(self, request: Request) -> Response:
        ...

    def get(self, request: Request) -> Response:
        ...
