FROM python:3.8.3-slim
RUN apt-get update; apt-get install -y build-essential libsasl2-dev python-dev libldap2-dev libssl-dev
COPY ./ /opt/e_commerce
WORKDIR /opt/e_commerce
RUN pip install pipenv && pipenv install
CMD ["sh", "entrypoint.sh"]