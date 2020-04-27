## not
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser

## 第2章で上記の代わりになるもの
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
## -----------------------------------------------
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

## not use
# @csrf_exempt
## ------------
@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        ## not use
        # return JsonResponse(serializer.data, safe=False)
        ## ------------------------------------------------
        return Response(serializer.data)

    elif request.method == 'POST':
        ## not use
        # data = JSONParser().parse(request)
        # serializer = SnippetSerializer(data=data)
        ## -------------------------------------------------
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            ## not use
            # return JsonResponse(serializer.data, status=201)
            ## -----------------------------------------------
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        ## not use
        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=sttaus.HTTP_400_BAD_REQUEST)

## not use
# @csrf_exempt
## ------------
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        ## not use
        # return HttpResponse(status=404)
        ## ----------------------------------------------
        return Response(status=status.HTTP_404_NOT_FOUND)
      
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        ## not use
        # return JsonResponse(serializer.data)
        ## -----------------------------------------------
        return Response(serializer.data)

    elif request.method == 'PUT':
        ## not use
        # data = JSONParser().parse(request)
        # serializer = SnippetSerializer(snippet, data=data)
        ## -------------------------------------------------
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            ## not use
            # return JsonResponse(serializer.data)
            ## -------------------------------------------
            return Response(serializer.data)
        ## not use
        # return JsonResponse(serializer.errors, status=400)
        ## -------------------------------------------------
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        ## not use
        # return HttpResponse(status=204)
        ## ------------------------------
        return Response(status=status.HTTP_204_NO_CONTENT)
