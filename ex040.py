n1 = float(input("Digite a priemira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
if m < 5:
    print("Sua nota é {:.1f} \nVocê está \033[1:31mREPROVADO(A)".format(m))
elif 5 <= m < 7:
    print("Sua nota é {} \nVocê está em \033[1:33mRECUPERAÇÃO".format(m))
else:
    print("Sua nota é {} \nVocê está \033[1:32mAPROVADO(A)".format(m))
