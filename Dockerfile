#use an official python runtime as a parent image
FROM --platform=arm64 python:3.12-slim

#set the working directory to /app
RUN mkdir -p /app

#copy file needed and setup work directory
COPY ./src /app
WORKDIR /app

#install pipenv
RUN pip install -U pipenv

#install dependencies using pipenv
RUN pipenv install --deploy

#expose port 5001 for gunicorn
EXPOSE 5001

#run gunicorn
CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:5001", "app:app"]