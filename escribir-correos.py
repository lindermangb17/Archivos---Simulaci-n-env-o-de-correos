ruta="C:/Users/Lenovo/OneDrive/Documentos/Linderman Personal/Campuslands/Visual/Linderman/Python I/archivos/"

with open(ruta+"mbox.txt", "r") as arch:
    emails=[]
    for lineas in arch:
        if lineas.startswith("From:"):
            email=lineas.split(" ")[1].strip()
            emails.append(email)

with open(ruta + "correos.txt", "w") as arch:
    enviados=[]
    for i in range(len(emails)-1,-1,-1):
        if emails[i] not in enviados:
            mensaje = emails[i] + " enviado [ok]\n"
            print(mensaje, end="")
            arch.write(mensaje)
            enviados.append(emails[i])
