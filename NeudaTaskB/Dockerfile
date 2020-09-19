FROM python:3
WORKDIR /data
RUN pip install cryptography
COPY ./requirements.txt ./requirements.txt
RUN python -m pip install -r ./requirements.txt
COPY . .
CMD [ "python", "./decryptfile.py" ]