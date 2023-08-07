from django.views import generic

from core import models


class MenuView(generic.DetailView):
    model = models.Menu
    template_name = "core/menu_detail.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related("usuario")
        return queryset

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")

        user_agent = request.META.get("HTTP_USER_AGENT")
        models.Acceso.objects.create(menu=self.object, user_agent=user_agent, ip=ip)

        return self.render_to_response(context)
