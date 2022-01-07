import nsq
import json

def consume(message):
  print("ID: {}".format(message.id))
  print("BODY: {}".format(message.body))
  return True

r = nsq.Reader(message_handler=consume, lookupd_http_addresses=['http://127.0.0.1:4161'], topic='example', channel='sync', lookupd_poll_interval=15)

nsq.run()
