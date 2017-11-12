from django.shortcuts import get_object_or_404
from api.models import Snippet
from api.serializers import SnippetSerializer
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


class SnippetList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'snippet_list.html'

    def get(self, request):
        queryset = Snippet.objects.all()
        return Response({'snippets': queryset})


class SnippetDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'snippet_detail.html'

    def get(self, request, pk):
        snippet = get_object_or_404(Snippet, pk=pk)
        lexer = get_lexer_by_name(snippet.language, stripall=True)
        formatter = HtmlFormatter(linenos=True, cssclass="source")
        result = highlight(snippet.code, lexer, formatter)
        serializer = SnippetSerializer(snippet)
        return Response({'serializer': serializer, 'snippet': snippet, 'formatted_code': result})

    def post(self, request, pk):
        snippet = get_object_or_404(Snippet, pk=pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'snippet': snippet})
        serializer.save()
        return redirect('snippet-list')
