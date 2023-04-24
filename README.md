# whisperAI-flask-docker

I built this project because there was no user friendly way to upload a file to a dockerized flask web form and have whisper do its thing via CLI in the background. Now there is. Enjoy! *Note* I built this on a windows machine for use with docker desktop and WSL. Tweak as necessary.

**********************************

# How to use:

Configure docker desktop to use WSL

Run: git clone https://github.com/jlonge4/whisperAI-flask-docker.git

Add the .wslconfig file to C://Users/{your_name} and Path environmental variables

Run: docker build -t whisper-app -f Dockerfile .

Run: docker run -it -p 5000:5000 whisper-app

# Copy your .srt file:

Run: sudo docker cp whisper-app:/whisperapp/test.srt /mnt

