
import pika

def main():
    credentials = pika.PlainCredentials("root", "password")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials))

    channel = connection.channel()
    channel.queue_declare(queue='hello')

    for i in range(10):
        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body='Hello World!')
        print(" [x] Sent 'Hello World!'")

    connection.close()


if __name__ == '__main__':
    main()
