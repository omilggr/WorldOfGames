FROM python:3.7-alpine
ADD ./*.py ./ 	
ADD ./*.txt ./
WORKDIR .
RUN pip install flask
RUN pip install selenium


CMD ["python", "MainScore.py"]
