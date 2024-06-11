# Principio de Abierto/Cerrado (Open/Closed Principle - OCP): 
# Este principio establece que una clase debe estar abierta para su 
# extensión pero cerrada para su modificación. Es decir, se deben poder
#  añadir nuevas funcionalidades a una clase sin necesidad de modificar 
# su código existente. 


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