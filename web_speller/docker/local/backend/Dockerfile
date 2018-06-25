FROM python:3.6-slim

ENV PYTHONUNBUFFERED 1


RUN apt-get -qq update \
    && apt-get -qq -y install libpq-dev gcc vim \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -qq -y clean


COPY ./docker/production/backend/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh \
    && chmod +x /entrypoint.sh

COPY ./docker/local/backend/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh \
    && chmod +x /start.sh


#COPY ./docker/local/backend/celery/worker/start.sh /start-celeryworker.sh
#RUN sed -i 's/\r//' /start-celeryworker.sh \
#    && chmod +x /start-celeryworker.sh

#COPY ./docker/local/backend/celery/beat/start.sh /start-celerybeat.sh
#RUN sed -i 's/\r//' /start-celerybeat.sh \
#    && chmod +x /start-celerybeat.sh


COPY ./backend/requirements /requirements/
RUN pip install --no-cache-dir -r /requirements/local.txt \
    && rm -rf /requirements

COPY ./shared/ /app/shared/
COPY ./backend /app

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/start.sh"]
