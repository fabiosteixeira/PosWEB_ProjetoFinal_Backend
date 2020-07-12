from django.urls import path

from .views import indexView as iv
from .views import despesaView as dv
from .views import receitaView as rv
from .views import relatorioView as relv
from .views import loginView as lg
from .views import userView as us

urlpatterns = [
    path('', iv.index, name="index"),

    path('despesa/', dv.despesa, name="despesa"),
    path('despesa/<int:id_despesa>/', dv.despesaOp, name="despesaOp"),

    path('receita/', rv.receita, name="receita"),
    path('receita/<int:id_receita>/', rv.receitaOp, name="receitaOp"),

    path('relatorio/despesas', relv.despesas, name="relatorio_despesas"),
    path('relatorio/despesas/filtro', relv.despesasFiltro, name="relatorio_despesas_filtro"),
    path('relatorio/receitas', relv.receitas, name="relatorio_receitas"),
    path('relatorio/receitas/filtro', relv.receitasFiltro, name="relatorio_receitas_filtro"),

    path('login/', lg.login, name="login"),

    path('user/', us.user, name="user"),
    path('user/create/', us.userCreateExterno, name="userCreateExterno"),
    path('user/<int:id_user>/', us.userOp, name="userOp"),

]