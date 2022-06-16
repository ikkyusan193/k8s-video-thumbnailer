# P2 – Video Thumbnailer
## Milestone 1: The Basic Sequential Thumbnail Pipeline.

```
cd worker/scripts/
docker build -f Dockerfile -t <container-name> .
docker run -v /path/to/video/:/path/to/working_dir <container-name> <inputFile> <outputFile>
```

## Mileston 2 & 3: Web controllers (Flask API & Vue/Vuetify)

### Frontend is mapped to http://localhost/frotnend/ using Ingress

#### Features

- Send job individually & all at once
- Delete gif individually & all at once
- Progress logs
- Video list
- Gif's Display room

#### Future features

- upload & delete video

### API is mapped to http://localhost/backend using Ingress

#### Retrieved video list from MinIO

```
  GET /backend/videos
```

#### List all gifs

```
  GET /backend/all
```

#### Retrieved all the job progress

```
  GET /backend/jobs
```

#### Creates multiple jobs for all videos in the bucket and submits them to the queue

```
  GET /backend/submit-bucket/${name}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. name of the bucket containing video |

#### Submit a task

```
  POST /backend/submit/${name}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. name of the video |


### Kubernetes deployment & commands

This may take long depending on your pc

```
kubectl create -f .
```

To delete pod uses

```
kubectl delete -f .
```

Display the pod's log

```
kubectl logs pods/<pod-name>
```
Restart the pod
```
kubectl rollout restart <deployment-kind> <deployment-name>
```
Display the description of all the pod runnig
```
kubectl describe pods
```
Port foward pods/deployment to local machine
```
kubectl port-forward <deployment-name> <port:port>
e.x. kubectl port-forward minio-675b67db56-mfk5z 9090:9090
```

