#Questão 1 - Desvio padrão

#Função:
def Desvio_p(consumo):
  return variancia(consumo)**0.5 # Calculo para desvio padrão

consumo = [10, 13, 17, 9,  8, 11, 13, 7]
import statistics
print('f)Desvio padrão:', Desvio_p(consumo))
print('Desvio padrão biblioteca:', statistics.stdev(consumo))