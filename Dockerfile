FROM ubuntu
RUN apt-get update && apt-get install -y python3 python3-pip
COPY . /
RUN cd test_tdd && pip3 install -r requirements.txt
CMD ["python3", "runserver.py"]
EXPOSE 5000