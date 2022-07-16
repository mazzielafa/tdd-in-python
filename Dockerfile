FROM ubuntu
RUN apt-get update && apt-get install -y python3 python3-pip
COPY . /
RUN cd TDD-Python-Test && pip3 install -r requirements.>WORKDIR python-package-flask-test
CMD ["python3", "runserver.py"]
EXPOSE 5000