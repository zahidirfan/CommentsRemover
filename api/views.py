from api.models import Snippet
from api.serializers import SnippetSerializer
from rest_framework import generics
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


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
        # Record the last accessed date

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
        object = super(SnippetComments, self).get_object()
        # Record the last accessed date
        object.save()
        # Return the object
        return object
