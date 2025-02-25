diaria = float(input("Diária: "))
taxa = float(input("Taxa: "))
mes = 32
dia = int(input("QUANTOS DIAS: "))


if dia >= 1 and dia <= 15:
    mes -= dia
    if dia == 1:
        n = mes * diaria
        print(n)
    elif dia == 2:
        n = taxa * (diaria + mes)
        print(n)
    elif dia >= 3 and dia <= 15:
        print(mes)
        imposto = dia - 1
        n = (diaria + imposto * taxa) * mes
        
        print(n)
        
if dia >= 16 and dia <= 31:
    mes -= dia
    imposto = dia - 2
    n = (diaria + imposto * taxa) * mes
    print(n)

