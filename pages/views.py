from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView): #Class-based view
    #Object Oriented Programming - Inheritance
    template_name = "pages/home.html" #Link our view to the HTML.

class AboutPageView(TemplateView):
    template_name = "pages/about.html"
    