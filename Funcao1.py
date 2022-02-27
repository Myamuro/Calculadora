from time import sleep
def escrever(msg):
  mg = input(msg)
  return mg


def temp(inter=0.02):
  while True:
    try:
      inte = float(input(inter))
    except:
      print('\033[1;31mErro digite um Intervalo Valido\033[m')
    else:
      break
  return inte
  

def impri(a, b, c=0.02):
  from time import sleep
  for l in a:
  	print(f'{b}{l}\033[m', end='', flush=True)
  	sleep(c)
  print()


def pula(a):
  if a == 1:
    print("")
  else:
    print("")
    print("")


def opcao(a):
  while True:
    try:
      op = int(input(a))
    except:
      print('\033[1;31mErro, Digite um Número Válido\033[m')
    else:
      break
  return op


def medida(a):
  while True:
    try:
      op = float(input(a))
    except:
      print('\033[1;31mErro, Digite um Valor válido\033[m')
    else:
      return op
      break


def bem():
  print ("""\033[1;36m   ▄▄▄▄▄▄                        ▄▄    ▄▄     ██                     ▄▄
   ██▀▀▀▀██                      ▀██  ██▀     ▀▀                     ██
   ██    ██   ▄████▄   ████▄██▄   ██  ██    ████     ██▄████▄   ▄███▄██   ▄████▄
   ███████   ██▄▄▄▄██  ██ ██ ██   ██  ██      ██     ██▀   ██  ██▀  ▀██  ██▀  ▀██
   ██    ██  ██▀▀▀▀▀▀  ██ ██ ██    ████       ██     ██    ██  ██    ██  ██    ██
   ██▄▄▄▄██  ▀██▄▄▄▄█  ██ ██ ██    ████    ▄▄▄██▄▄▄  ██    ██  ▀██▄▄███  ▀██▄▄██▀
   ▀▀▀▀▀▀▀     ▀▀▀▀▀   ▀▀ ▀▀ ▀▀    ▀▀▀▀    ▀▀▀▀▀▀▀▀  ▀▀    ▀▀    ▀▀▀ ▀▀    ▀▀▀▀"
  \033[m""")


def escreve():
  print('[1]', end='')
  impri("Triângulos", "\033[1;33m")
  print('[2]', end='')
  impri("Áreas", "\033[1;33m")
  print('[3]', end='')
  impri("Potenciação", "\033[1;33m")
  print('[4]', end='')
  impri("Porcentagem", "\033[1;33m")
  print('[5]', end='')
  impri("Calcular", "\033[1;33m")


def escrevea():
  pula(2)
  print('[1]', end='')
  impri("Quadrado", "\033[1;33m")
  print('[2]', end='')
  impri("Cubo", "\033[1;33m")
  print('[3]', end='')
  impri("Triangulo", "\033[1;33m")
  print('[4]', end='')
  impri("Circulo", "\033[1;33m")
  print('[5]', end='')
  impri("Retângulo", "\033[1;33m")
  print('[6]', end='')
  impri("Trapézio", "\033[1;33m")
  print('[7]', end='')
  impri("Losango", "\033[1;33m")


def erro():
  print('\033[1;31mErro, Digite uma Opção Válida\033[m')
