import shutil
import sys
import os
import logging
import json
import redis
from redis.commands.json.path import Path
from minio import Minio
from minio.error import S3Error
from rq import Queue

LOG = logging
LOG.basicConfig(
    level=LOG.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


class RedisHelper:

    def __init__(self):

        REDIS_HOST = os.getenv('REDIS-HOST')
        REDIS_PORT = int(os.getenv('REDIS-PORT'))
        REDIS_PASSWORD = os.getenv('REDIS-ROOT-PASSWORD')

        self.client = redis.Redis(REDIS_HOST, REDIS_PORT, password=REDIS_PASSWORD)
        self.EXTRACT_QUEUE = Queue("Extract", connection=self.client)
        self.COMPOSE_QUEUE = Queue("Compose", connection=self.client)
        self.LOG_QUEUE = Queue("Log",connection=self.client) 

    def update_status(self, id, status):
        self.client.json().set(id, Path('status'), status)

    def create_status(self, id, name):
        status = {'id': id,'video': name, 'status': "Job received"}
        self.client.json().set(id, Path.root_path(), status)

    def get_status(self, id):
        return self.client.json().get(id)           

# MINIO
class MinioHelper:

    def __init__(self):
        MINIO_HOST = os.getenv('MINIO-HOST')
        self.client = Minio(MINIO_HOST, access_key= os.getenv('MINIO-ACCESS-KEY'), secret_key=os.getenv('MINIO-SECRET-KEY'), secure=False)
        
        # Initializing Minio buckets
        BUCKETS = ["videos","frames","gifs"]
        for bucket in BUCKETS:
            check = self.client.bucket_exists(bucket)
            if not check: self.client.make_bucket(bucket)
            else: print(f'Bucket {bucket} already exist')

    # TODO: Utils & Functions
    def download_video(self, name):
        self.client.fget_object('videos', name, f'./scripts/{name}')     
    
    def upload_frames(self, id, name):
        name = os.path.splitext(name)[0] # remove file extensions
        folder = f'./scripts/{id}/'
        files = [f for f in os.listdir(folder)]
        for file in files:
            self.client.fput_object('frames', os.path.join(id,file) , os.path.join(folder,file))
            # self.client.fput_object('frames', '/1/sample1.jpg', 'scripts/1/sample1.jpg')
        shutil.rmtree(folder, ignore_errors=True)   

    def download_frames(self, id):
        frames = self.client.list_objects('frames', prefix=f'{id}/', recursive= True)
        for frame in frames:
            LOG.info('%s', frame.object_name)
            self.client.fget_object('frames', frame.object_name, os.path.join('./scripts/',frame.object_name))

    def upload_gif(self, id):
        self.client.fput_object('gifs', f'{id}.gif', f'./scripts/gifs/{id}.gif')
        os.remove(f'./scripts/gifs/{id}.gif')  # remove local gifs
        
    def allGifs(self):
        gifs = self.client.list_objects("gifs", recursive=True)
        return gifs 

  
    def download_file(self, bucket, fileName, filePath):
        self.client.fget_object(bucket, fileName, filePath)