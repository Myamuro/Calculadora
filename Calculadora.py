from os import system
from Função import *
from Função2 import *
system('clear')
bem()
pula(2)
escreve()
pula(2)
while True:
  while True:
    op = opcao('\033[4;35mDigite opção》\033[m ')
    if op >= 1 and op <= 5:
      break
    else:
      erro()
  if op == 1:
    pula(2)
    a = opcao('\033[4;35mDigite opção》\033[m')
    print('n terminei')
    pula(2)
  if op == 2:
    escrevea()
    pula(2)
    while True:
      a = opcao('\033[4;37mDigite opção》\033[m')
      if a >= 1 and a <= 7:
        break
      else:
        erro()
    if a == 1:
     b = medida('\033[32mDigite a Lagura》\033[32m')
     c = medida('\033[32mDigite o Cumprimento》\033[32m')
     areaq(b, c)
    if a == 2:
      b = medida('\033[32mDigite a Largura》\033[32m')
      c = medida('\033[32mDigite o Cumprimento》\033[32m')
      d = medida('\033[32mDigite a Altura》\033[m')
      cubico(b, c, d)
    if a == 3:
      b = medida('\033[32mDigite a Base》\033[32m')
      c = medida('\033[32mDigite a Altura》\033[32m')
      tria(b, c)
    if a == 4:
      b = medida('\033[32mDigite o Raio》\033[32m')
      circu(b)
    if a == 5:
      b = medida('\033[32mDigite a Base》\033[32m')
      c = medida('\033[32mDigite a Altura》\033[32m')
      reta(b, c)
    if a == 6:
      b = medida('\033[32mDigite a Base Maior》\033[32m')
      c = medida('\033[32mDigite a Base Menor》\033[32m')
      d = medida('\033[32mDigite a Altura》\033[32m')
      trap(b, c, d)
    if a == 7:
      b = medida('\033[32mDigite a Diagonal Maior》\033[32m')
      c = medida('\033[32mDigite a Diagonal Menor》\033[32m')
      losa(b, c)
  if op == 3:
    a = medida('\033[32mDigite o Número》\033[32m')
    b = medida('\033[32mDigite a potenciação》\033[32m')
    poten(a, b)
    pula(2)
  if op == 4:
    a = medida('\033[32mDigite a Porcentagem》\033[32m')
    b = medida('\033[32mDigite o Valor》\033[32m')
    porcen(a, b)
    pula(2)
  if op == 5:
    calcu('\033[1;37m=======》\033[m')
  print('\033[m[0]\033[m', end='')
  impri("Sair", "\033[1;33m", 0.03)
  print('[1]', end='')
  impri("Continuar", "\033[1;33m", 0.03)
  print('[9]', end='')
  impri("Limpar Tela", "\033[1;33m")
  pula(1)
  while True:
    op = opcao('\033[1;37m====》\033[m')
    if op != 1 and op != 0 and op != 9 and op != 17394:
      erro()
    else:
      break
  if op == 1:
    continue
  if op == 0:
    break
  if op == 9:
    system('python calculadora.py')
    break
  break
