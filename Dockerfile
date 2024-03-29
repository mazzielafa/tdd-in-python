FROM ubuntu
RUN apt-get update && apt-get install -y python3 python3-pip
COPY . /
RUN pip3 install -r requirements.txt
# RUN python3 test_tdd/init_db.py
CMD ["python3", "runserver.py"]
EXPOSE 5000