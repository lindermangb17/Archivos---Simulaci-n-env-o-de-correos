ruta="C:/Users/Lenovo/OneDrive/Documentos/Linderman Personal/Campuslands/Visual/Linderman/Python I/archivos/"

with open(ruta+"mbox.txt", "r") as arch:
    emails=[]
    for lineas in arch:
        if lineas.startswith("From:"):
            email=lineas.split(" ")[1].strip()
            emails.append(email)

with open(ruta + "correos.txt", "w") as arch:
    for i in range(len(emails)-1,-1,-1):
        mensaje = emails[i] + " enviado [ok]\n"
        print(mensaje)
        arch.write(mensaje)