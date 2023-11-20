from django.contrib import messages


class MessageMixin:
    msg_type = messages.SUCCESS
    msg_desc = "Ejecutado con éxito"

    def form_valid(self, form):
        messages.add_message(self.request, self.msg_type, self.msg_desc)
        return super().form_valid(form)
