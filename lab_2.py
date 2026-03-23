import numpy as np
import matplotlib.pyplot as plt
time=np.arange(0,10,0.02)
func = np.zeros ((3 , 500) )

for i in range(500):
    func[0,i]=2*np.sin(time[i])
    func[1,i]=2*np.cos(time[i])
    func[2,i]=0.5*time[i]
x=func[0,:]
y=func[1,:]
z=func[2,:]

plt.subplot(3,1,1)
plt.plot(time,x)
plt.grid(True)
plt.title('funcion sen(x)')

plt.subplot(3,1,2)
plt.plot (time,y)
plt.grid(True)
plt.title('funcion cos(x)')

plt.subplot(3,1,3)
plt.plot(time,z)
plt.grid(True)
plt.title('funcion exponencial')
plt . tight_layout () 
plt.show()



