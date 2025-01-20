import numpy as np
import matplotlib.pyplot as plt
import sys

if(len(sys.argv)<6):
    raise Exception("Za malo argumentow")

A=np.float64(sys.argv[1])
B=np.float64(sys.argv[2])
a=np.float64(sys.argv[3])
b=np.float64(sys.argv[4])
o=np.float64(sys.argv[5])

t=np.linspace(0,2*np.pi,num=200)

x=A*np.sin(B*t+o)
y=B*np.sin(b*t)

plt.plot(x,y)
plt.axis("square")
plt.xlabel("Os X")
plt.ylabel("Os Y")
plt.title("Wykres")
plt.grid()
plt.show()

