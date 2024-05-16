from abc import abstractmethod
from infrastructure.rabbit_connection import RabbitConnection

class RabbitConsumer:

    topic = None

    def __init__(self):
        self.channel = RabbitConnection.get_channel()
        self.channel.basic_consume(queue=self.topic, on_message_callback=self.process_message, auto_ack=True)
        self.channel.start_consuming()

    @abstractmethod
    def process_message(self, channel, method, properties, body):
        pass
