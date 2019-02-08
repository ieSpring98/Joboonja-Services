from django.conf.urls import url

from Services.views import ServicesView

urlpatterns = [
    url(r'^skills/', ServicesView.as_view({'get': 'get_skills'}), name='get_skills'),
    # url(r'^projects/?', PollManagementView.as_view({'get': 'get_created_polls'}), name='get-created-polls'),
]
