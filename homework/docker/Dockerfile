FROM Python:3.93
WORKDIR /docker
COPY requirements.txt /docker
RUN pip install --upgrade pip -r requirements.txt
COPY . /docker
