FROM python:3.7-slim-buster
RUN pip3 install numpy pandas xgboost
# Make sure python doesn't buffer stdout so we get logs ASAP.
ENV PYTHONUNBUFFERED=TRUE
ENTRYPOINT ["python3"]