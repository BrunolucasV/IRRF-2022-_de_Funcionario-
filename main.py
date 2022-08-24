from mimetypes import init
teste= "ir irrf"

salario=(input("digite o salario do funcionário: "))
filhos=int(input("quantos filho(s) o funcinário possui: "))
salario=float(salario.replace(",","."))

if salario < 1212.00 :
    inss =round( salario / 7.5, 2)
elif salario > 1212.00 and salario < 2427.79:
    inss = round( salario / 9, 2)
elif salario > 2427.79 and salario < 3641.69:
    inss = round( salario / 12, 2)
else:
    inss = round( salario / 14, 2)

print(inss)
temp= salario - inss

if temp > 1903.98 and temp < 2826.65:
    ir=round( filhos * 142.80 , 2)
    irrf=round(  (salario - ir) / 7.5  )
elif temp > 2826.65 and temp < 3751.06:
    ir=round(  filhos  * 354.80, 2)
    irrf=round(  (salario - ir) / 15, 2)
elif temp > 3751.06 and temp < 4664.68:
    ir=round(  filhos * 636.13, 2)
    irrf=round(  (salario - ir) / 22.50, 2)
else:
    ir=round(  filhos * 869.36, 2)
    irrf=round(  (salario - ir) / 27.50, 2)

liquido = (salario - inss)-irrf  
print(f"o salario liquido foi de: R${liquido:,.2f}, seu inss e irrf foi de: {inss, irrf}")
