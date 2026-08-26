from abc import abstractmethod
from infrastructure.rabbit_connection import RabbitConnection

class RabbitConsumer:

    topic = None

    def __init__(self):
        self.channel = RabbitConnection.get_channel()
        # Declaramos la cola propia antes de consumir (idempotente en RabbitMQ).
        # Elimina la carrera: si el productor aún no declaró la cola, este
        # consumer la crea y ya no crashea con ChannelClosed 404.
        if self.topic:
            self.channel.queue_declare(queue=self.topic, durable=False)
        self.channel.basic_consume(queue=self.topic, on_message_callback=self.process_message, auto_ack=True)
        self.channel.start_consuming()

    @abstractmethod
    def process_message(self, channel, method, properties, body):
        pass
