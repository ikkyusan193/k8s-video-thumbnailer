# P2 – Video Thumbnailer
## Milestone 1: The Basic Sequential Thumbnail Pipeline.

```
cd worker/scripts/
docker build -f Dockerfile -t <container-name> .
docker run -v /path/to/video/:/path/to/working_dir <container-name> <inputFile> <outputFile>
```