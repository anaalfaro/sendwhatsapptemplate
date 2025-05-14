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

        # Configurar cliente de ACS
        connection_string = "endpoint=https://cccommunicationservices.europe.communication.azure.com/;accesskey=wP2oDfZlISmObpFv0ftwkTdozzR8nPGVwJ9zBs9sY9kLM0r46se4JQQJ99BCACULyCp7JkqPAAAAAZCSsuim"
        client = NotificationMessagesClient.from_connection_string(connection_string)

        # Configurar mensaje con plantilla
        template_message = TemplateNotificationContent(
            channel_registration_id="17c8e032-28bc-4cb8-8d45-1ed3f9d5d2a4",
            to="+34638675292",
            template_id="100d3169_fe7f_4327_bda1_8d30ebcc9906",
            parameters={"nombre": nombre, "fecha": fecha}
        )

        # Enviar mensaje
        response = client.send(template_message)

        return func.HttpResponse(f"Mensaje enviado correctamente a {phone_number}", status_code=200)

    except Exception as e:
        logging.error(f"Error al enviar mensaje: {str(e)}")
        return func.HttpResponse("Error al enviar mensaje", status_code=500)
