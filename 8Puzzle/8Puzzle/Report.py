def WriteReport(NewTime):
    lines = GetLines()
    sum = 0

    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", '')
        if i > 0:
            sum+=float(lines[i])
    sum+=NewTime
    average = sum/len(lines)
    
    lines.append(NewTime)
    lines[0] = average
    WriteLines(lines)
    print("El tiempo promedio es " + str(average))

def GetLines():
    archivo = open("report.txt", "r")
    contenido = archivo.readlines()
    archivo.seek(0)
    archivo.close()
    return contenido

def WriteLines(lineas):
    archivo = open("report.txt", "w")
    output = list(map(str,lineas))
    for i in range(len(output)):
        output[i] = output[i] +"\n"
    output[len(output)-1].replace("\n", '')
    archivo.writelines(output)
    archivo.close()

            