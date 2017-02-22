import logging

from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce

from ..models import Ubigeo

#from backend_utils.logs import log_params
#from backend_utils.permissions import ModelPermission
#from backend_utils.pagination import ModelPagination

#from rest_framework import permissions
# from django.utils.translation import ugettext as _  # , ungettext

log = logging.getLogger(__name__)


class UbigeoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ubigeo
        fields = '__all__'

#from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
#from rest_framework.permissions import IsAuthenticated


class UbigeoViewSet(viewsets.ModelViewSet):
    queryset = Ubigeo.objects.all()
    serializer_class = UbigeoSerializer
    #permission_classes = [IsAuthenticated, ModelPermission, TokenHasScope]
    # required_scopes = ['catalogo', ]  # , 'write'

    def get_queryset(self):
        queryset = Ubigeo.objects.all()
        return queryset
