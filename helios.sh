#!/usr/bin/env bash

case $1 in
    docker)
        case $2 in
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
        esac
        exit 0
    ;;
    esac
    