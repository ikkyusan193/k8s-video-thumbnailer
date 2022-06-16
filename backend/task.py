import os
import logging
import subprocess
import interface

LOG = logging
LOG.basicConfig(
    level=LOG.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

RedisHelper = interface.RedisHelper()
MinioHelper = interface.MinioHelper()

# CURRENT DIRECTORY == ./APP
def extract(id, input):
    LOG.info("Task received:%s %s %s", id, input)
    
    MinioHelper.download_video(input)
    RedisHelper.LOG_QUEUE.enqueue(update_job, id, "Video downloaded")
    LOG.info("Video %s downloaded", input)

    process = subprocess.Popen(f'sh ./scripts/extract.sh {id} {input}', shell=True, stdout=subprocess.PIPE)
    process.wait()
    RedisHelper.LOG_QUEUE.enqueue(update_job, id, "Frames Extracted")
    LOG.info("Frame extracted")

    MinioHelper.upload_frames(id, input)
    RedisHelper.LOG_QUEUE.enqueue(update_job, id, "Frames uploaded to Minio")
    LOG.info("Frames uploaded to Minio")

    RedisHelper.COMPOSE_QUEUE.enqueue(compose, id, input)
    RedisHelper.LOG_QUEUE.enqueue(update_job, id, "Frames send to compose")


def compose(id, input):

    MinioHelper.download_frames(id)
    RedisHelper.LOG_QUEUE.enqueue(update_job, id, "Frames downloaded")
    LOG.info("Frames %s downloaded", id)

    process = subprocess.Popen(f'sh ./scripts/compose.sh {id} {input}', shell=True, stdout=subprocess.PIPE)
    process.wait()
    RedisHelper.LOG_QUEUE.enqueue(update_job, id, "Gif composed")
    LOG.info("Gif Composed")

    MinioHelper.upload_gif(id)
    RedisHelper.LOG_QUEUE.enqueue(update_job, id, "Gif uploaded to Minio")
    LOG.info("Gif uploaded to Minio")


def update_job(id, status):
    RedisHelper.update_status(id,status)

def initialize_job(id, name):
    RedisHelper.create_status(id, name)


# 
