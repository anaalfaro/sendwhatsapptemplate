import logging
import azure.functions as func
from azure.communication.messages import NotificationMessagesClient
from azure.communication.messages.models import TemplateNotificationContent

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Procesando solicitud para enviar mensaje de WhatsApp.')

    try:
        req_body = req.get_json()
        phone_number = req_body.get('to')
        nombre = req_body.get('nombre')
        fecha = req_body.get('fecha')
        template_id = req_body.get('template_id')
        channel_registration_id = req_body.get('channel_registration_id')

        # Configurar cliente de ACS
        connection_string = "endpoint=https://cccommunicationservices.europe.communication.azure.com/;accesskey=TU_ACCESS_KEY"
        client = NotificationMessagesClient.from_connection_string(connection_string)

        # Configurar mensaje con plantilla
        template_message = TemplateNotificationContent(
            channel_registration_id=channel_registration_id,
            to=[phone_number],
            template_id=template_id,
            parameters={"nombre": nombre, "fecha": fecha}
        )

        # Enviar mensaje
        response = client.send_notification(template_message)

        return func.HttpResponse(f"Mensaje enviado correctamente a {phone_number}", status_code=200)

    except Exception as e:
        logging.error(f"Error al enviar mensaje: {str(e)}")
        return func.HttpResponse("Error al enviar mensaje", status_code=500)
