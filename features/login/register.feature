# language: pt
@register
Funcionalidade: Registro no Automation Exercise
  Como um usuário não registrado
  Eu desejo criar um registro
  Para poder acessar o site logado

  Cenário: Registro Bem-Sucedido
    Dado que estou na página de registro
    E eu insiro o nome e o e-mail 
    E clico no botão "Signup"
    Quando eu preencho os detalhes da conta
    E clico no botão de criar conta
    Então a mensagem de confirmação "ACCOUNT CREATED" deve ser exibida
    E clico no botão "Continue"
    E  a mensagem de confirmação "Logged in as Renzo Tavares" deve ser exibida
    Quando eu clico no link "Delete Account"
    Então a mensagem de confirmação "ACCOUNT DELETED" deve ser exibida
    E clico no botão "Continue"
    E confirmo que estou deslogado
