from django.contrib.auth.views import LoginView

#Criacao de caminhos para abertura de views

class LoginUsuario(LoginView):
    template_name = 'usuarios/entrar.html'



