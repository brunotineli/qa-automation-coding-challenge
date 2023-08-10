FROM python:3.10

WORKDIR /usr/src/app
ENV PYTHONPATH=":/usr/src/app"

# Copy the dependencies
ADD requirements.txt ./

# Install dependencies
RUN pip3 install -r requirements.txt

# Adds remaining files to container
ADD . /usr/src/app

CMD ["pytest"]