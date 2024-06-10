FROM nginx

COPY ./nginx.conf /nginx.conf.template

COPY imgs/ /usr/share/nginx/html/imgs/
COPY Dashboard.html Upload.html /usr/share/nginx/html/

RUN sed 's|http://localhost:5000||g' /usr/share/nginx/html/Dashboard.html -i

# COPY ./nginx.conf /etc/nginx/conf.d/default.conf
CMD ["/bin/sh" , "-c" , "envsubst < /nginx.conf.template > /etc/nginx/conf.d/default.conf && exec nginx -g 'daemon off;'"]
