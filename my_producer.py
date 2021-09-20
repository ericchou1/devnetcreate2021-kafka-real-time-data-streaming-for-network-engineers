from confluent_kafka import Producer
import socket
import json
from datetime import datetime

# check https://github.com/confluentinc/examples/blob/6.2.0-post/clients/cloud/python/producer.py for ack examples

conf = {'bootstrap.servers': "kafka-1:9092", 'client.id': socket.gethostname()}
producer = Producer(conf)

for n in range(5):
    record_key = "my_key"
    record_value = json.dumps(
              {
                  "Time": "blah",
                  "Value": str(datetime.now())
              }
            )
    topic = "Test3"
    producer.produce('Test3', key=record_key, value=record_value)

producer.flush()


