##LABORATORIO 2 
#JORDAN PORRAS

import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0, 10, 500)
func = np.zeros((3, 500))

for i in range (500):
    func[0,i]= 2*np.sin(time[i])
    func[1,i]= 2*np.cos(time[i])
    func[2,i]= 0.5*(time[i])

x=func[0,:]
y=func[1,:]
z=func[2,:]

print(x)