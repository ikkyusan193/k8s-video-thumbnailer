# start from base
FROM python:3.9

# copy our application code
ADD ./worker /app
ADD ./backend/task.py ./app
ADD ./backend/interface.py ./app

WORKDIR /app
# COPY /run.sh ./

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y ffmpeg
RUN apt install imagemagick -y

# expose port
EXPOSE 5000

# start app
CMD [ "python", "./worker.py"]
