FROM python:3.4.3

COPY *.py ./src/
RUN pip install requests flask
CMD python3 ./src/app.py
