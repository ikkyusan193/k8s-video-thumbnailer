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
def extract(input, output):
    LOG.info("Task received:%s %s", input, output)

    MinioHelper.download_video(input)
    LOG.info("Video %s downloaded", input)

    process = subprocess.Popen(f'sh ./scripts/extract.sh {input}', shell=True, stdout=subprocess.PIPE)
    process.wait()
    LOG.info("Frame extracted")

    MinioHelper.upload_frames(input)
    LOG.info("Frames uploaded to Minio")

    RedisHelper.COMPOSE_QUEUE.enqueue(compose, input, output)
    # TODO: UPDATE status 
    # job = RedisHelper.LOG_QUEUE.enqueue(update_job, "status")


def compose(input, output):

    MinioHelper.download_frames(input)
    LOG.info("Frames %s downloaded", input)

    process = subprocess.Popen(f'sh ./scripts/compose.sh {input} {output}', shell=True, stdout=subprocess.PIPE)
    process.wait()
    LOG.info("Gif Composed")

    MinioHelper.upload_gif(output)
    LOG.info("Gif uploaded to Minio")

    # TODO: UPDATE status 
    # job = RedisHelper.LOG_QUEUE.enqueue(update_job, "status")

def update_job(jobID, status):
    print("yoyoyo")

# 
