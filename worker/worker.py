import os
import logging
import redis
from rq import Worker, Queue, Connection

LOG = logging
LOG.basicConfig(
    level=LOG.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Initialize redis client
REDIS_HOST = os.getenv('REDIS-HOST')
REDIS_PORT = int(os.getenv('REDIS-PORT'))
REDIS_PASSWORD = os.getenv('REDIS-ROOT-PASSWORD')

client = redis.Redis(REDIS_HOST, REDIS_PORT, password=REDIS_PASSWORD)
listen = [os.getenv('LISTEN-QUEUE')]

# Worker/Listen is being started here!
if __name__ == '__main__':
    with Connection(client):
        worker = Worker(map(Queue, listen))
        LOG.info('Workers created')
        worker.work()
