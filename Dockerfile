FROM python:3.9-alpine
COPY requirements.txt /requirements.txt
#install dependencies
RUN pip install -r requirements.txt
#copy everything from source
COPY redeploy.py /redeploy.py
#run the app
CMD ["python", "/redeploy.py"]