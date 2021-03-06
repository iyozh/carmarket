from django.db.models import Q
from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from applications.api.impl.v1.serializers.utm_serializer import UtmSerializer
from applications.statistics.models import UTM
from project.utils import _get_utm_string
from project.utils.object_utils import _update_utm


class UtmViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UtmSerializer
    http_method_names = ["patch", "get"]

    def get_queryset(self):
        queryset = UTM.objects.filter(
            Q(link__user_id=self.request.user.id) & Q(link_id=self.kwargs["pk"])
        )

        return queryset

    def partial_update(self, request, *args, **kwargs):
        redirect_response = super().partial_update(request, *args, **kwargs)

        link_id = kwargs["pk"]

        instance = self.get_object()

        utm_string = _get_utm_string(instance)
        _update_utm(utm_string, link_id)

        return redirect_response
