FROM ubuntu:18.04

ADD ./ /app
WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg
RUN apt install imagemagick -y
RUN chmod +x makegif.sh

ENTRYPOINT ["./makegif.sh"]
CMD ["test.mp4", "output.gif"]