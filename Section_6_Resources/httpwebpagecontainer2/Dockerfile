FROM centos:latest
RUN yum -y install httpd curl telnet
COPY ./index.html /var/www/html/
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
EXPOSE 80

