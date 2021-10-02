# Derived from official mariadb image (our base image)
FROM mariadb
# Add a database
ENV MARIADB_DATABASE auBonBeurre
# Add the content of the sql-scripts/ directory to your image
# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup
COPY ./mariaDB-scripts/ /docker-entrypoint-initdb.d/

