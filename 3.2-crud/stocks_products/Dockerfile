FROM python:3.9

COPY ./requirements.txt /src/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt


COPY . /src

ENV MY_ENV=netology
WORKDIR src
#ENV SECRET_KEY=FF433459KMPOLL;,SPDF''2L34[[3,4[L,M43MON#FDGNOZGZF
RUN ["python", "manage.py", "migrate"]
#WORKDIR src
EXPOSE 8000

#RUN python manage.py migrate


CMD python manage.py runserver 0.0.0.0:8000


