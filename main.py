print("Bem-vindo ao nosso sistema!\n")

usuario = "Joao"
senha = "Joao123@"

VerifUsuario = input("Digite o seu nome de usuário:\n")
VerifSenha = input("Digite a sua senha:\n")

if VerifUsuario == usuario and VerifSenha == senha:
  print("Logado com sucesso!")
else:
  print("Usuario e/ou senha incorreto(s)!")