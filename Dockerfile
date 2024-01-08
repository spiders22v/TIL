FROM tensorflow/tensorflow
WORKDIR /app
COPY . /app .
CMD ["python3", "app.py"]