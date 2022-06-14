# Imports library/tools
import os
import logging
import json
from flask import Flask, jsonify, request

# Imports Interface & Worker functions 
import interface
from task import extract

LOG = logging
LOG.basicConfig(
    level=LOG.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

RedisHelper = interface.RedisHelper()
MinioHelper = interface.MinioHelper()

RedisHelper.client.set("job_count", 0) # JOB ID

app = Flask(__name__)

@app.route('/api/submit', methods=['POST'])
def submit_job():
    RedisHelper.client.incr("job_count", 1)
    id = RedisHelper.client.get("job_count").decode("utf-8")
    task = json.loads(json.dumps(request.json))
    input = task.get('input')
    output = task.get('output')
    RedisHelper.EXTRACT_QUEUE.enqueue(extract, id, input, output)
    return jsonify({'status': 'OK', 'id': id})

@app.route('/api/bucket/', methods=["POST"])
# TODO: API that, given a bucket, creates multiple jobs for all videos in the bucket and submits them to the queue
def submit_bucket():
    task = json.loads(json.dumps(request.json))
    bucket_name = task.get('bucket')
    videos = MinioHelper.client.list_objects(bucket_name, recursive=True)
    for video in videos:
        input = video.object_name # input.mp4
        output = f'{os.path.splitext(input)[0]}.gif' # output.gif
        RedisHelper.EXTRACT_QUEUE.enqueue(extract, input, output)
    return jsonify({'status': 'OK'})


@app.route('/api/all', methods=["GET"])
def all_gifs():
    urls = {}
    gifs = MinioHelper.client.list_objects("gifs", recursive=True)
    for gif in gifs:
        urls[gif.object_name] = MinioHelper.client.get_presigned_url("GET","gifs", gif.object_name)
    return jsonify(urls)
    
@app.route('/api/progress/', methods=["GET"])
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