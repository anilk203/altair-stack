FROM nginx:1.25.0

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/

RUN rm /etc/nginx/conf.d/default.conf
COPY project.conf /etc/nginx/conf.d/

RUN apt-get update -y
RUN apt-get install -y iputils-ping