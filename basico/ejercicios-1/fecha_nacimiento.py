import calendar

fecha_nacimiento = input("Introduzca su fecha de nacimiento en formato dd/mm/aaaa: ")
partes_fecha = fecha_nacimiento.split("/")
if len(partes_fecha) == 3:
    dia,mes,año = partes_fecha

    if dia.isnumeric() and mes.isnumeric():
        dia = int(dia)
        mes = int(mes)

        if 1 <= dia <= 31 and 1 <= mes <= 12:
            dia = str(dia).lstrip('0')
            mes_nombre = calendar.month_name[mes]
            print(f"Naciste el día {dia} de {mes_nombre} en el año {año}")
        else:
            print("El día y el mes deben estar dentro de los rangos válidos.")
    else:
        print("El día y el mes deben ser números válidos.")
else:
    print("El formato de fecha no es válido. Asegúrese de usar dd/mm/aaaa.")




