""" 1) Refaça o programa da aula passada de conversão em radianos de três
formas diferentes:

a) A primeira será respeitando a fórmula, porém recebendo o valor da pi
a partir da biblioteca math.

b) A segunda será simplesmente utilizando a função de conversão de
graus em radianos. Printe ambos os resultados para compará-los.

Radianos = Graus / 180 X pi

c) Por último, utilize o valor convertido para radianos e com a função de
conversão de radianos para graus, converta de volta os valores para
graus e printe-os! (Caso algum valor em graus não saia exatamente o
valor original, use a função de teto ou piso para arredondar o resultado
no print!)

Faça para os valores de 30o, 60o, 90o e 180o graus.
"""
import math as m

# Primeira forma: Alterando o valor de pi para a valor da função da blblioteca Math que retorna o valor de pi.
pi = m.pi

formularadiano30 = print('Resultado do Radiano de 30° usando a fómula:',(30/180)*pi) # radiano de 30°
formularadiano60 = print('Resultado do Radiano de 60° usando a fómula:',(60/180)*pi) # radiano de 60°
formularadiano90 = print('Resultado do Radiano de 90° usando a fómula:',(90/180)*pi) # radiano de 90°
formularadiano180 = print('Resultado do Radiano de 180° usando a fómula:',(180/180)*pi) # radiano de 180°
print('+' + 90*'='+'+')
# Segunda forma: Ultilizando a função da biblioteca Math.

radianomath30 = m.radians(30)
radianomath60 = m.radians(60)
radianomath90 = m.radians(90)
radianomath180 = m.radians(180)

print('Ultilizando a função radians() da biblioteca Math para achar o radiano de 30°:',radianomath30)
print('Ultilizando a função radians() da biblioteca Math para achar o radiano de 60°:',radianomath60)
print('Ultilizando a função radians() da biblioteca Math para achar o radiano de 90°:',radianomath90)
print('Ultilizando a função radians() da biblioteca Math para achar o radiano de 180°:',radianomath180)

print('+' + 90*'='+'+')

# Terceira forma: Converter radianos de volta para graus.

radianoparagrau30 = print('Convertendo radiano de 30° de volta para grau ultizando a função degrees() da blblioteca Math:',m.ceil(m.degrees(radianomath30)))
radianoparagrau60 = print('Convertendo radiano de 60° de volta para grau ultizando a função degrees() da blblioteca Math:',m.ceil(m.degrees(radianomath60)))
radianoparagrau90 = print('Convertendo radiano de 90° de volta para grau ultizando a função degrees() da blblioteca Math:',m.degrees(radianomath90))
radianoparagrau180 = print('Convertendo radiano de 180° de volta para grau ultizando a função degrees() da blblioteca Math:',m.degrees(radianomath180))

print('+' + 90*'='+'+')
#Bônus: Como converter sem precisar da função degrees()
# print(180*(radianomath30/pi))