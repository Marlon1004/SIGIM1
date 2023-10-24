
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail


@receiver(post_save, sender=User)
def enviar_correo_nuevo_usuario(sender, instance, created, **kwargs):
    if created:
        subject = 'InnoSoft te hace entrega de tus Credenciales de acceso a la plataforma SIGIM'
        message = f'Hola {instance.username},\n\nTu usuario: {instance.username}\nTu contraseña: {instance.password}\n\n¡Bienvenido a nuestro sitio web!'
        from_email = 'noreply@tu_sitio.com'
        recipient_list = [instance.email]
        message_encoded = message.encode('utf-8')
        send_mail(subject, message, from_email, recipient_list)
