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
def extract(id, input, output):
    LOG.info("Task received:%s %s", id, input, output)

    MinioHelper.download_video(input)
    LOG.info("Video %s downloaded", input)

    process = subprocess.Popen(f'sh ./scripts/extract.sh {id} {input}', shell=True, stdout=subprocess.PIPE)
    process.wait()
    LOG.info("Frame extracted")

    MinioHelper.upload_frames(id, input)
    LOG.info("Frames uploaded to Minio")

    RedisHelper.COMPOSE_QUEUE.enqueue(compose, id, input)
    # TODO: UPDATE status 
    # job = RedisHelper.LOG_QUEUE.enqueue(update_job, "status")


def compose(id, input):

    MinioHelper.download_frames(id)
    LOG.info("Frames %s downloaded", id)

    process = subprocess.Popen(f'sh ./scripts/compose.sh {id} {input}', shell=True, stdout=subprocess.PIPE)
    process.wait()
    LOG.info("Gif Composed")

    MinioHelper.upload_gif(id)
    LOG.info("Gif uploaded to Minio")

    # TODO: UPDATE status 
    # job = RedisHelper.LOG_QUEUE.enqueue(update_job, "status")

def update_job(jobID, status):
    print("yoyoyo")

# 
