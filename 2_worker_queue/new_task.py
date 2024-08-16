
import pika
import sys

def main():
    credentials = pika.PlainCredentials("root", "password")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)

    for i, x in enumerate(['First', 'Second', 'Third', 'Fourth', 'Fifth']):
        dots = '.' * (i + 1)
        message = f" [x] Sent {x}{dots}"
        channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent
            ))
        print(f" [x] Sent {message}")

    connection.close()


if __name__ == '__main__':
    main()