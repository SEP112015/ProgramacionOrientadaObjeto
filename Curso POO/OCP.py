class Notificacion:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotADirectoryError
    

class NotificadorEmail(Notificacion):
    def notificar(self):
        print(f"Enviando mensaje a {self.usuario.email}")
    

class NotificadorSMS(Notificacion):
    def notificar(self):
        print(f"Enviando SMS a  {self.usuario.sms}")

class NotificadorWhatsApp(Notificacion):
    def notificar(self):
        print(f"Enviando WhatsApp a  {self.usuario.whatsapp}")