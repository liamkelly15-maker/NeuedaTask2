FROM python:3
WORKDIR /shared
RUN pip install cryptography
COPY ./json_file.json ./json_file.json
COPY ./requirements.txt ./requirements.txt
RUN python -m pip install -r ./requirements.txt
COPY . .
CMD [ "python", "./encryptfile.py" ]