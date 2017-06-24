from django.conf.urls import url
from demo.views import (Home, QuestionDetail)


urlpatterns = [
    
    
    url(r'^question/(?P<pk>[0-9]+)$', QuestionDetail.as_view(), name="questiondetail"),
    url(r'^$', Home.as_view(), name="home"),
]

from django.conf.urls.static import static, settings


urlpatterns = urlpatterns + [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
