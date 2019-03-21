from drf_haystack.serializers import HaystackSerializer
from rest_framework import serializers
from .models import House
from .search_indexes import HouseIndex
from rest_framework.pagination import PageNumberPagination


class HouseSerializer(serializers.ModelSerializer):
    '''
    House 结果的序列化器
    @:param:
        model: 指定去哪个数据库找
        fields: 返回哪些字段
    '''
    class Meta:
        model = House
        fields = ('id', 'district', 'zone', 'garden')


class HouseIndexSerializer(HaystackSerializer):
    '''
    House 索引的序列化器
    '''
    object = HouseSerializer(read_only=True)

    class Meta:
        index_classes = [HouseIndex]
        fields = ('text', 'object')


class StandardResultSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = "page_size"
    max_page_size = 20
