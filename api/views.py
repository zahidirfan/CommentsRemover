from api.models import Snippet
from api.serializers import SnippetSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from pygments import highlight
import pygments
from pygments.lexers import guess_lexer
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from bs4 import BeautifulSoup


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetAnalysis(APIView):

    def post(self, request):
        # print request.data['code']
        code = request.data['code']
        language = guess_lexer(code).name
        return Response(language)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetHighlight(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get_object(self):
        # Call the superclass
        object = super(SnippetHighlight, self).get_object()

        lexer = get_lexer_by_name(object.language, stripall=True)
        formatter = HtmlFormatter(linenos=True, cssclass="source")
        result = highlight(object.code, lexer, formatter)

        object.code = result
        # Return the object

        return object


class SnippetComments(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get_object(self):
        # Call the superclass
        pygment_comments = [
            pygments.token.Comment,
            pygments.token.Comment.Hashbang,
            pygments.token.Comment.Multiline,
            pygments.token.Comment.Preproc,
            pygments.token.Comment.Single,
            pygments.token.Comment.Special,
            pygments.token.Literal.String.Doc
        ]
        object = super(SnippetComments, self).get_object()
        lexer = get_lexer_by_name(object.language, stripall=True)
        formatter = HtmlFormatter(linenos=True, cssclass="source")
        comments = ""
        for token_type, token_text in lexer.get_tokens(object.code):
            if token_type in pygment_comments:
                comments = comments + token_text + '\n'

        result = highlight(comments, lexer, formatter)

        object.code = result
        return object
