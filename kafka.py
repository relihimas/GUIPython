import sys
import os
from confluent_kafka import Producer

def delivery_callback(err, msg):
  if err:
    print('%% Message failed delivery: %s \n', err)
  else:
    print('%% Messge delivered to %s [%d]\n', (msg.topic(), msg.partition()))

def createTopic():
  print("init")
  topic = 'iltod0mr-default'

  conf = {
          'bootstrap.servers': 'dory-01.srvs.cloudkafka.com:9094,dory-02.srvs.cloudkafka.com:9094,dory-03.srvs.cloudkafka.com:9094',
          'session.timeout.ms': 6000,
          'default.topic.config': {'auto.offset.reset':'smallest'},
          'security.protocol': 'SASL_SSL',
          'sasl.mechanisms': 'SCRAM-SHA-256',
          'sasl.username': 'iltod0mr',
          'sasl.password': 'YyLl4X9wk-02NbtJcSskdsDy7eJg1AUC'
  }

  p = Producer(conf)

  try:
    p.produce(topic, 'hahai', callback = delivery_callback)
  except BufferError as e:
    print('%% Local producer queue is full (%d messages awaiting delivery): try again\n' % len(p))

  p.poll(0)

  print('%% Waiting for %d deliveries\n' % len(p))
  p.flush()

createTopic();

##################################################################################################################################################################
import sys
import os
from confluent_kafka import Consumer, KafkaError, KafkaException
import pandas as pd

def createConsumer():

  topics = ['iltod0mr-default']

  conf = {
          'bootstrap.servers': 'dory-01.srvs.cloudkafka.com:9094,dory-02.srvs.cloudkafka.com:9094,dory-03.srvs.cloudkafka.com:9094',
          'group.id': "%s-consumer" % "iltod0mr",
          'session.timeout.ms': 6000,
          'default.topic.config': {'auto.offset.reset':'smallest'},
          'security.protocol': 'SASL_SSL',
          'sasl.mechanisms': 'SCRAM-SHA-256',
          'sasl.username': 'iltod0mr',
          'sasl.password': 'YyLl4X9wk-02NbtJcSskdsDy7eJg1AUC'

  }
  
  c = Consumer(conf)
  c.subscribe(topics)
  try:
    while True:
      msg = c.poll(timeout=1.0)
      if msg is None:
        continue
      if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
          print('%% %s [%d] reached end at offset %d\n' % (msg.topic(), msg.partition(), msg.offset()))
        elif msg.error():
          raise KafkaException(msg.error())
      else:
        print('%% %s [%d] at offset %d with key %s:\n' % (msg.topic(), msg.partition(), msg.offset(), str(msg.key())))
        print(msg.value())
  except KeyboardInterrupt:
    print('%% Aborted by user\n')

  c.close()

createConsumer();
