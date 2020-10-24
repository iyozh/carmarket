from django.urls import reverse_lazy
from django.views.generic import RedirectView
from dynaconf import settings as _ds

from applications.homepage.models import Link
from applications.statistics.models import Hit
from project.utils.web_utils import get_hit_params


class RedirectToOriginalView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        absolute_url = self.request.build_absolute_uri()

        if _ds.ACCOUNT_DEFAULT_HTTP_PROTOCOL == "https":
            absolute_url = absolute_url.replace("http:", "https:")

        redirect_url = Link.objects.filter(shortcut=absolute_url).first()

        if redirect_url.confirm:
            if "confirmation" not in self.request.headers["Referer"]:
                return reverse_lazy(
                    "homepage:confirmation", kwargs={"pk": redirect_url.pk}
                )

        params = get_hit_params(self.request)
        hit = Hit(**params, url_id=redirect_url.id)
        hit.save()
        return redirect_url.original