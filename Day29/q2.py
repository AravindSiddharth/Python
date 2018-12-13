#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

fobj=plt.figure(figsize=(8,8))
spobj=fobj.add_subplot(1,1,1)

Party='INC BJP Independent Others'.split()
win=[114,15,4,3]
colrs='r y c g b'.split()

patches,texts=spobj.pie(win,colors=colrs,shadow=True,startangle=120)

plt.title('Madhya Pradesh')
plt.legend(patches,Party,loc='best')

plt.show()


#-----------------------------------------------


fobj=plt.figure(figsize=(8,8))
spobj=fobj.add_subplot(1,1,1)

Party='INC BJP Independent Others'.split()
win=[99,73,3,14]
colrs='r y c g b'.split()

patches,texts=spobj.pie(win,colors=colrs,shadow=True,startangle=120)

plt.title('Rajstan')
plt.legend(patches,Party,loc='best')

plt.show()


#--------------------------------------------


fobj=plt.figure(figsize=(8,8))
spobj=fobj.add_subplot(1,1,1)

Party='INC BJP BSP+ Others'.split()
win=[68,15,9,7]
colrs='r y c g b'.split()

patches,texts=spobj.pie(win,colors=colrs,shadow=True,startangle=120)

plt.title('chhattisgarh')
plt.legend(patches,Party,loc='best')

plt.show()


#---------------------------------------------------------

fobj=plt.figure(figsize=(8,8))
spobj=fobj.add_subplot(1,1,1)

Party='TRS INC BJP Others'.split()
win=[88,19,1,11]
colrs='r y c g b'.split()

patches,texts=spobj.pie(win,colors=colrs,shadow=True,startangle=120)

plt.title('Telangana')
plt.legend(patches,Party,loc='best')

plt.show()


#-----------------------------------------------------------

fobj=plt.figure(figsize=(8,8))
spobj=fobj.add_subplot(1,1,1)

Party='MNF INC BJP Others'.split()
win=[26,5,1,8]
colrs='r y c g b'.split()

patches,texts=spobj.pie(win,colors=colrs,shadow=True,startangle=120)

plt.title('Mizoram')
plt.legend(patches,Party,loc='best')

plt.show()


