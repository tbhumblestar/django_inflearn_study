from django.urls import path,include
from django.contrib import admin
from django.views.generic import TemplateView,RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instagram/', include('instagram.urls')),

    # path('',TemplateView.as_view(template_name="root.html"),name='root'),
    path('',RedirectView.as_view(
        # url='/instagram/',
        pattern_name='instagram:post_list'),name='root'),
]
