from django.shortcuts import render
from django.views.generic import TemplateView, FormView

# for email form onfiguration

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import reverse
from .forms import ContactForm


# for email config
class SuccessView(TemplateView):
    template_name = "success.html"


class ContactView(FormView):
    form_class = ContactForm
    template_name = "contact.html"

    def get_success_url(self):
        return reverse("success")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        full_message = f"""
        Received message below from {email}, {subject}
        ________________________

        {message}
        """

        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )

        return super().form_valid(form)


# for home.html
def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "THAnk you FOR visitING.",
    }

    return render(request, "home.html", context)


class AboutPageView(TemplateView):  # new
    template_name = "about.html"

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "Warszawa"
        context["phone_number"] = "phone number"
        return context
