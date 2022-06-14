# start from base
FROM python:3.9

# copy our application code
ADD ./backend /app
ADD ./worker/worker.py ./app
# ADD ./worker/scripts/compose.sh ./app
# ADD ./worker/scripts/extract.sh ./app

WORKDIR /app
# COPY /run.sh ./

RUN pip install -r requirements.txt

# expose port
EXPOSE 5000

# start app
CMD [ "python", "./app.py"]