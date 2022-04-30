#!/usr/bin/env bash

platform tunne:open -e main -y

export PLATFORM_RELATIONSHIPS="$(platform tunnel:info --encode)"

# Redis
CACHE_SCHEME_REDIS=$(echo $PLATFORM_RELATIONSHIPS | base64 --decode | jq -r ".rediscache[0].scheme")
CACHE_USER_REDIS=$(echo $PLATFORM_RELATIONSHIPS | base64 --decode | jq -r ".rediscache[0].username")
CACHE_PW_REDIS=$(echo $PLATFORM_RELATIONSHIPS | base64 --decode | jq -r ".rediscache[0].password")
CACHE_HOST_REDIS=$(echo $PLATFORM_RELATIONSHIPS | base64 --decode | jq -r ".rediscache[0].host")
CACHE_PORT_REDIS=$(echo $PLATFORM_RELATIONSHIPS | base64 --decode | jq -r ".rediscache[0].port")

printf "# Generated Platform.sh local environment file.

## Application
FLASK_APP=flask-mariadb
FLASK_EN=production

## Databases.
# MariaDB/MySQL.
DB_NAME_MYSQL=$(echo $PLATFORM_RELATIONSHIPS | base64 --decode | jq -r ".database[0].path")
DB_HOST_MYSQL=$(echo $PLATFORM_RELATIONSHIPS | base64 --decode | jq -r ".database[0].host")
DB_PORT_MYSQL=$(echo $PLATFORM_RELATIONSHIPS | base64 --decode | jq -r ".database[0].port")
DB_USER_MYSQL=$(echo $PLATFORM_RELATIONSHIPS | base64 --decode | jq -r ".database[0].username")

## Caching.
# Redis.
CACHE_LOCATION_REDIS=$CACHE_SCHEME_REDIS://$CACHE_HOST_REDIS:$CACHE_PORT_REDIS
" > .env


# migrations
# FLASK_APP=run.py poetry run flask db init
# FLASK_APP=run.py poetry run flask db migrate
# FLASK_APP=run.py poetry run flask db upgrade