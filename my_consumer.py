from confluent_kafka import Consumer

# check https://github.com/confluentinc/examples/blob/6.2.0-post/clients/cloud/python/consumer.py for examples

conf = {'bootstrap.servers': 'kafka-1:9092', 'group.id': 'foo', 'auto.offset.reset': 'earliest'}

consumer = Consumer(conf)
consumer.subscribe(['Test3'])
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            #print("Waiting for message or error in poll()")
            continue
        elif msg.error():
            print('error: {}'.format(msg.error()))
        else:
            record_key = msg.key()
            record_value = msg.value()
            print(record_key, record_value)

except KeyboardInterrupt:
    pass
finally:
    consumer.close()


