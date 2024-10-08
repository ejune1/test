FROM ubuntu:24.04
RUN apt update
RUN apt install vim sudo -y
#RUN apt install gnupg2 wget curl -y 
#RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
#RUN curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
#RUN apt update
RUN apt install postgresql-16 postgresql-contrib-16 -y
#RUN systemctl stop postgresql
COPY postgresql.conf /etc/postgresql/16/main/postgresql.conf
COPY pg_hba.conf /etc/postgresql/16/main/pg_hba.conf
RUN chown postgres:postgres /etc/postgresql/16/main/postgresql.conf
RUN chown postgres:postgres /etc/postgresql/16/main/pg_hba.conf
#RUN systemctl start postgresql
CMD ["/bin/bash", "-c" ,"sudo -H -u postgres /usr/lib/postgresql/16/bin/postgres -c config_file=/etc/postgresql/16/main/postgresql.conf"]

#psql -U postgres
