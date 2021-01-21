# development build
FROM python:3.8-alpine as dev

# env
WORKDIR /app
ENV PYTHONPATH=/app

# copy requirements
COPY src/requirements ./requirements

# system installs
RUN apk update && \
    apk add docker alpine-sdk && \
    # python installs
    pip install -r requirements/dev.txt -r requirements/prod.txt

# copy src
COPY src/luna ./luna

# docker mount
VOLUME /var/run/docker.sock

# cmd set up
CMD ["python3", "-u", "-m", "luna"]

# production build
FROM python:3.8-alpine as prod

# env
WORKDIR /app
ENV PYTHONPATH=/app

# copy requirements
COPY src/requirements ./requirements

# system installs
RUN apk update && \
    apk add docker alpine-sdk && \
    # python installs
    pip install -r requirements/prod.txt && \
    # clean up
    apk del alpine-sdk && \
    rm -rf requirements

# copy src
COPY --from=dev /app/luna ./luna

# docker mount
VOLUME /var/run/docker.sock

# cmd set up
CMD ["python3", "-u", "-m", "luna"]
