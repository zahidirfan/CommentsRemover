from api.models import Snippet
from api.serializers import SnippetSerializer
from rest_framework import generics
from pygments import highlight
import pygments
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from bs4 import BeautifulSoup


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


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
            pygments.token.Comment.Special
        ]
        object = super(SnippetComments, self).get_object()
        lexer = get_lexer_by_name(object.language, stripall=True)
        formatter = HtmlFormatter(linenos=True, cssclass="source")
        comments = ""
        for token_type, token_text in lexer.get_tokens(object.code):
            # Check for keywords and convert them to lower case.
            if token_type in pygment_comments:
                comments = comments + token_text + '\n'

        result = highlight(comments, lexer, formatter)

        object.code = result
        return object
