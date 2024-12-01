FROM python:3.10-slim AS python_image

RUN apt update && apt upgrade -y

COPY ./requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt

FROM python_image AS app_image

COPY . /opt/insurance-calculation
WORKDIR /opt/insurance-calculation
CMD ["sh", "entrypoint.sh"]
