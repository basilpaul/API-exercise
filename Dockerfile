FROM python:3-slim
LABEL maintainer="paul.basil@gmail.com"
ENV PROJECT_ROOT /
WORKDIR $PROJECT_ROOT
COPY requirements.txt requirements.txt
COPY passenger.py passenger.py
COPY generate_db.py generate_db.py
COPY titanic.csv titanic.csv
COPY test_passengers.tavern.yaml test_passengers.tavern.yaml
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["passenger.py"]