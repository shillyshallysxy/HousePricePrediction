from haystack import indexes
from .models import House


class HouseIndex(indexes.SearchIndex, indexes.Indexable):
    '''搜索类'''
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return House

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

