from rest_framework.response import Response
from rest_framework.decorators import api_view
from movies.services import search_movies_service


@api_view(['GET'])
def search_movies(request):
    """Django View: Handle movie search requests"""

    title = request.GET.get('title', '')
    site = request.GET.get('site', '')

    # 调用 services.py 里的方法
    data = search_movies_service(title, site)

    return Response(data)
