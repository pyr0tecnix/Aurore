#!/usr/bin/env bash

case $1 in
    docker)
        case $2 in
            up)
                docker-compose -f docker-compose.dev.yml up -d
            ;;
            start)
                docker-compose -f docker-compose.dev.yml start
            ;;
            stop)
                docker-compose -f docker-compose.dev.yml stop
            ;;
            restart)
                docker-compose -f docker-compose.dev.yml stop
                docker-compose -f docker-compose.dev.yml start
            ;;
            create)
                docker-compose -f docker-compose.dev.yml down
                docker-compose -f docker-compose.dev.yml build
                docker-compose -f docker-compose.dev.yml up -d --force-recreate
            ;;
            stats)
                docker ps -q | xargs  docker stats --no-stream
            ;;
        esac
        exit 0
    ;;
    log)
        case $2 in
            server)
                docker-compose -f docker-compose.dev.yml logs -f server
            ;;
            nginx)
                docker-compose -f docker-compose.dev.yml logs -f nginx
            ;;
            redis)
                docker-compose -f docker-compose.dev.yml logs -f redis
            ;;
        esac
        exit 0
    ;;
    ssh)
        case $2 in
            server)
                docker-compose -f docker-compose.dev.yml exec server /bin/bash
            ;;
            nginx)
                docker-compose -f docker-compose.dev.yml exec nginx /bin/bash
            ;;
            redis)
                docker-compose -f docker-compose.dev.yml exec redis /bin/bash
            ;;
        esac
        exit 0
    ;;
    app)
        case $2 in
            init)
                docker-compose -f docker-compose.dev.yml exec server /bin/bash -c "cd src && pypy3 manage.py makemigrations"
                docker-compose -f docker-compose.dev.yml exec server /bin/bash -c "cd src && pypy3 manage.py migrate"
                docker-compose -f docker-compose.dev.yml exec server /bin/bash -c "cd src && pypy3 manage.py createsuperuser"
            ;;
            migrate)
                docker-compose -f docker-compose.dev.yml exec server /bin/bash -c "cd src && pypy3 manage.py makemigrations"
                docker-compose -f docker-compose.dev.yml exec server /bin/bash -c "cd src && pypy3 manage.py migrate"
            ;;         
            static)
                docker-compose -f docker-compose.dev.yml exec server /bin/bash -c "cd src && pypy3 manage.py collectstatic"
            ;;
            manage)
                docker-compose -f docker-compose.dev.yml exec server /bin/bash -c "cd src && pypy3 manage.py ${3}"
            ;;
            runtest)
                docker-compose -f docker-compose.dev.yml exec server /bin/bash -c "cd src && pypy3 -Wa manage.py test"
            ;;
        esac
        exit 0
    esac
    