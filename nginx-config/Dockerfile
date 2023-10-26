FROM nginx
RUN apt-get update
RUN rm -r /etc/nginx/conf.d
COPY nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /home/public/static/
COPY static/ /home/public/static/
