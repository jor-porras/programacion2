voltajes = [12.6 , 12.4 , 12.3 , 12.1 , 11.9 , 11.8 , 11.6 , 11.4]
def check_volt(lista):
 volt_max=max(lista)
 volt_min=min  (lista)
 suma=0
 volt_12=[]
 for i in range (len(lista)):
  suma=suma+lista[i]
  if lista[i]<12:
   volt_12.append(lista[i])
 prom_volt=suma/len(lista) 
 return prom_volt,volt_12,volt_max,volt_min

prom_volt, volt_12, volt_max, volt_min = check_volt(voltajes)

print(f"el voltaje maximo es:{volt_max}")
print(f"el voltaje menor es: {volt_min}  ")
print(f"el voltaje  promedio es: {prom_volt}")
print("los voltajes menores a 12 volt son:")
print(volt_12)