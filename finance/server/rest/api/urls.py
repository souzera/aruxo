from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categorias', views.results_categoria, name='categoria_results'),
    path('<int:categoria_id>/categoria-details', views.details_categoria, name='categoria_details'),
    path('cc-types', views.cc_types_results, name='cc_types_results'),
    path('<int:tipo_conta_id>/cc-type-details', views.detail_type_cc, name='cc_type_details'),
    path('contas', views.conta_results, name='conta_results'),
    path('<int:conta_id>/conta-details', views.detail_conta, name='conta_details'),
    path('instituicoes', views.instituicao_results, name='instituicao_results'),
    path('<int:instituicao_id>/instituicao-details', views.detail_instituicao, name='instituicao_details'),
    path('transacoes', views.transacao_results, name='transacao_results'),
    path('<int:transacao_id>/transacao-details', views.detail_transacao, name='transacao_details')

]
