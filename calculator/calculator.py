#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import math
import cmath

senha = raw_input("Digite a senha para iniciar o programa: ")
os.system('cls')
while senha <> "aluno123":
    print "Digite a senha para iniciar o programa: "
    senha = raw_input("Senha incorreta. Tente novamente: ")
    os.system("cls")
else:
    os.system('cls')
    print 'TWO NUMBERS CALCULATOR BY LUCAS SANTOS DA SILVA \n'
    print 'Para usar essa calculadora, primeiro defina o primeiro e segundo números.\nEntão pressione o botão \"ENTER\"\n'
    print 'O segundo numero deve ser diferente de \"0\" \n'

def calculator(a, b):
  if b == 0:
    print 'Acho que deverias usar um segundo numero diferente...'
    b = input('Segundo numero: ')
    calculator(a, b)
  
  print '-------------------------------------------------------------'
  print a,'+',b, '=', a+b
  print '-------------------------------------------------------------'
  print a,'-',b, '=', a-b
  print '-------------------------------------------------------------'
  print a,'*',b, '=', a*b
  print '-------------------------------------------------------------'
  print a,'/',b, '=', a/b
  print '-------------------------------------------------------------'
  print a,'^','2', '=', a**2
  print '-------------------------------------------------------------'
  print a,'^','3', '=', a**3
  print '-------------------------------------------------------------'
  print b,'^','2', '=', b**2
  print '-------------------------------------------------------------'
  print b,'^','3', '=', b**3
  print '-------------------------------------------------------------'
  if a < 0:
    print 'The squareroot of ',a,'=', cmath.sqrt(a)
    print '-------------------------------------------------------------'
  else:
    print 'The squareroot of ',a,'=', math.sqrt(a)
    print '-------------------------------------------------------------'
  if b < 0:
    print 'The squareroot of ',b,'=', cmath.sqrt(b)
    print '-------------------------------------------------------------'
  else:
    print 'The squareroot of ',b,'=', math.sqrt(b)
    print '-------------------------------------------------------------'
  print 'The sin of',a,'=', '%.2f' %(math.sin(a))
  print '-------------------------------------------------------------'
  print 'The cos of',a,'=', '%.2f' %(math.cos(a))
  print '-------------------------------------------------------------'
  print 'The tan of',a,'=', '%.2f' %(math.tan(a))
  print '-------------------------------------------------------------'
  print 'The sin of',b,'=', '%.2f' %(math.sin(b))
  print '-------------------------------------------------------------'
  print 'The cos of',b,'=', '%.2f' %(math.cos(b))
  print '-------------------------------------------------------------'
  print 'The tan of',b,'=', '%.2f' %(math.tan(b))
  print '-------------------------------------------------------------'
  if a > 0:
    print 'The factorial of',a,'=', math.factorial(a)
    print '-------------------------------------------------------------'
  if b > 0:
    print 'The factorial of',b,'=', math.factorial(b)
    print '-------------------------------------------------------------'
  print 'The inverse value of',a,'=', -a
  print '-------------------------------------------------------------'
  print 'The inverse value of',b,'=', -b
  print '-------------------------------------------------------------'
  if a < 0:
    print 'The module of',a,'=',-a
    print '-------------------------------------------------------------'
  else:
    print 'The module of',a,'=',a
    print '-------------------------------------------------------------'
  if b < 0:
    print 'The module of',b,'=',-b
    print '-------------------------------------------------------------'
  else:
    print 'The module of',b,'=',b
    print '-------------------------------------------------------------'
  r = raw_input('Gostaria de reiniciar? (y/n): ')
  if r == 'y':
    os.system('cls')
    print 'TWO NUMBERS CALCULATOR BY LUCAS SANTOS DA SILVA \n'
    print 'Para usar essa calculadora, primeiro defina o primeiro e segundo números.\nEntão pressione o botão \"ENTER\"\n'
    print 'O segundo numero deve ser diferente de \"0\" \n'
    a = input('Primeiro numero: ')
    b = input('Segundo numero: ')
    calculator(a, b)
  else:
    print 'Ate logo! :)'
    print '-------------------------------------------------------------'
    print 'This is experimental Python program created by Lucas Santos da Silva \nfor learning purposes \n'
    print 'February 16, 2015 - Mogi das Cruzes, SÃ£o Paulo \n'

a = input('Primeiro numero: ')
b = input('Segundo numero: ')
if (type(a) or type(b) <> str):
  print "Tente novamente"
calculator(a, b)
