# Imports library/tools
import os
import logging
import json
from flask import Flask, jsonify, request
import base64

# Imports Interface & Worker functions 
import interface
from task import extract, initialize_job

LOG = logging
LOG.basicConfig(
    level=LOG.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

RedisHelper = interface.RedisHelper()
MinioHelper = interface.MinioHelper()

RedisHelper.client.set("job_count", 0) # JOB ID

app = Flask(__name__)

@app.route('/backend/submit', methods=['POST'])
def submit_job():
    RedisHelper.client.incr("job_count", 1)
    id = RedisHelper.client.get("job_count").decode("utf-8")
    task = json.loads(json.dumps(request.json))
    input = task.get('input')
    RedisHelper.EXTRACT_QUEUE.enqueue(extract, id, input) # Send extract job
    RedisHelper.LOG_QUEUE.enqueue(initialize_job, id, input) # Create job status in REDIS
    return jsonify({'status': 'OK', 'id': id})

@app.route('/backend/submit-bucket', methods=["POST"])
# backend that, given a bucket, creates multiple jobs for all videos in the bucket and submits them to the queue
def submit_bucket():
    task = json.loads(json.dumps(request.json))
    bucket_name = task.get('bucket')
    videos = MinioHelper.client.list_objects(bucket_name, recursive=True)
    for video in videos:
        RedisHelper.client.incr("job_count", 1)
        id = RedisHelper.client.get("job_count").decode("utf-8")
        input = video.object_name # input.mp4
        RedisHelper.EXTRACT_QUEUE.enqueue(extract, id, input)
    return jsonify({'status': 'OK'})


@app.route('/backend/all', methods=["GET"])
def all_gifs():
    urls = []
    gifs = MinioHelper.client.list_objects("gifs", recursive=True)
    for gif in gifs:
        url = str(MinioHelper.client.get_presigned_url("GET","gifs", gif.object_name))
        key = url.split('?')[-1]
        urls.append({'name': gif.object_name, 'link' :f'http://localhost/minio/gifs/{gif.object_name}?{key}'})   
    return jsonify(urls), 200

@app.route('/backend/gifs', methods=["GET"])
def gifs():
    urls = {}
    gifs = MinioHelper.client.list_objects("gifs", recursive=True)
    for gif in gifs:    
        item = MinioHelper.client.get_object("gifs", gif.object_name).read()
        urls[gif.object_name] = base64.b64encode(item).decode("utf8")
    return jsonify(urls), 200

@app.route('/backend/videos', methods=["GET"])
def vids():
    vids = [{'name': vid.object_name} for vid in MinioHelper.client.list_objects("videos", recursive=True)]
    return jsonify(vids), 200    

@app.route('/backend/jobs', methods=['GET'])
def all_jobs():
    jobs = []
    job_count = int(RedisHelper.client.get("job_count").decode("utf-8"))
    for i in range(1,job_count+1):
        jobs.append(RedisHelper.get_status(i))
    return jsonify(jobs), 200    

@app.route('/backend/progress/', methods=["GET"])
def progress(id):
    task = json.loads(json.dumps(request.json))
    id = task.get('id')
    progess = RedisHelper.client.get(id)
    if progess != None:
        return jsonify({'id': id ,'progress': progess})    
    else:
        return jsonify({'id': id, 'progress': f'job {id} does not exist' })    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)