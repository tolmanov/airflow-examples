FROM airflow-ml-base:latest

COPY predict.py /predict.py

ENTRYPOINT ["python", "predict.py"]
CMD ["/data/processed/", "/data/predicted/"]