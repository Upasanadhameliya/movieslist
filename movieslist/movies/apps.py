from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MoviesConfig(AppConfig):
    name = "movieslist.movies"
    verbose_name = _("Movies")

    def ready(self):
        try:
            import movieslist.movies.signals  # noqa F401
        except ImportError:
            pass