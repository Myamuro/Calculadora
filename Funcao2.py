from Função import pula
def hipot(a, b):
  pula(1)
  print(f'''\033[1;36m  A2 = {a**2} + {b**2}
  A2 = {(a**2)+(b**2)}
  Hipotenusa = {((a**2) + (b**2))**(1/2):.2f}''')


def areaq(a, b):
  pula(1)
  print(f'\033[1;36mÁrea = {a} × {b} = {a * b:.2f}\033[m')
  pula(2)


def cubico(a, b, c):
  pula(1)
  print(f'\033[1;36mÁrea = {a} × {b} × {c} = {a * b * c:.2f}\033[m')
  pula(2)


def poten(a, b):
  pula(1)
  print(f'\033[1;36m{a} Elevado a {b} = {a ** b:.2f}\033[m')


def porcen(a, b):
  pula(1)
  print(f'\033[1;36m{a:.0f}% de {b} = {b * a/100:.2f}\033[m')


def tria(a, b):
  pula(1)
  print(f'''\033[1;36m
      {a} × {b}
A  = ---------------  = {(a * b)/2:.2f}
           2''')
  pula(2)


def circu(a):
  pula(1)
  print(f'\033[1;36mA = {3.14} × {a**2} = {3.14 * (a**2)}\033[m')
  pula(2)


def reta(a, b):
  pula(1)
  print(f'\033[1;36mA = {a} × {b} = {a*b:.2f}\033[m')
  pula(2)


def trap(a, b, c):
  print(f'''\033[1;36mA = ({a} + {b}) × {c}
------------------------------  = {((a + b)*c)/2:.2f}
            2\033[m''')
  pula(2)


def losa(a, b):
  print(f'''\033[1;36m
      {a} × {b}
A  = ---------------  = {(a * b)/2:.2f}
           2''')
  pula(2)


def calcu(a):
  soma = input(a).replace('×', '*').replace('÷', '/').replace(',', '.').replace('^', '**').replace('{', '(').replace('}', ')').replace('[', '(').replace(']', ')')
  conta = soma.replace('**', '^').replace('/', '÷').replace('.', ',').replace('*', '×')
  pula(1)
  print(f'\033[1;36m{conta} = ', end='')
  print (eval(f'{soma}'))
  pula(2)
