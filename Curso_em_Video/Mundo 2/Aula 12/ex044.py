pn = float(input("Preço normal: "))
print("Selecione forma de pagamento: \n[1]à vista dinheiro/cheque \n[2]à vista cartão \n[3] 2x no cartão \n[4] 3x ou mais no cartão")
e = int(input(':'))
if e == 1:
    pn = pn * 0.9
elif e == 2:
    pn = pn *0.95
else:
    pn = pn * 1.2
print("Valor a pargar: ", pn)