FROM ubuntu:latest
WORKDIR /data
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./encryptfile.py /encryptfile.py
CMD [ "python", "/encryptfile.py" ]