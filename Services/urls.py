from django.conf.urls import url

from Services.views import ServicesView

urlpatterns = [
    url(r'^skills/', ServicesView.as_view({'get': 'get_skills'}), name='get_skills'),
    url(r'^projects/?', ServicesView.as_view({'get': 'get_projects'}), name='get_projects')
]
