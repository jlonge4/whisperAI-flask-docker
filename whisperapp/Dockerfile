FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /whisperapp

RUN apt-get -y update && apt-get install -y python3 \
ffmpeg \
python3-pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install -U openai-whisper
RUN echo "All packages installed successfully"

COPY . .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]