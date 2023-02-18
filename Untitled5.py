#!/usr/bin/env python
# coding: utf-8

# In[3]:


#КАЛЬКУЛЯТОР
print('Добро пожаловать в мой мир под названием КАЛЬКУЛЯТОР где я бог а вы не очень')
a=int(input(''))
b=int(input(''))
v=int(input('Какую операция вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение'))
if v==1:
    r=a+b
    q='Сложение'
    t=q
if v==2:
    r=a-b
    p='Вычитание'
    t=p
if v==3:
    r=float(a/b)
    o='Деление'
    t=o
if v==5:
    r=a*b
    m='Сложение'
    t=m
print(t,'=', r)


# In[5]:


x=4
if (x>0):
    X=x*10
else:
    X=x*8
print(X)


# In[ ]:




