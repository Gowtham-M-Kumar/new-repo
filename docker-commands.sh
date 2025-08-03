#!/bin/bash

# Docker commands for Django Portfolio Project

case "$1" in
    "build")
        echo "Building Docker image..."
        docker build -t portfolio-app .
        ;;
    "run")
        echo "Running with Docker Compose (production)..."
        docker-compose up -d
        ;;
    "dev")
        echo "Running with Docker Compose (development)..."
        docker-compose -f docker-compose.dev.yml up -d
        ;;
    "stop")
        echo "Stopping containers..."
        docker-compose down
        ;;
    "logs")
        echo "Showing logs..."
        docker-compose logs -f web
        ;;
    "shell")
        echo "Opening shell in web container..."
        docker-compose exec web bash
        ;;
    "migrate")
        echo "Running migrations..."
        docker-compose exec web python manage.py migrate
        ;;
    "collectstatic")
        echo "Collecting static files..."
        docker-compose exec web python manage.py collectstatic --noinput
        ;;
    "createsuperuser")
        echo "Creating superuser..."
        docker-compose exec web python manage.py createsuperuser
        ;;
    "clean")
        echo "Cleaning up Docker resources..."
        docker-compose down -v
        docker system prune -f
        ;;
    *)
        echo "Usage: $0 {build|run|dev|stop|logs|shell|migrate|collectstatic|createsuperuser|clean}"
        echo ""
        echo "Commands:"
        echo "  build         - Build Docker image"
        echo "  run           - Run production environment"
        echo "  dev           - Run development environment"
        echo "  stop          - Stop all containers"
        echo "  logs          - Show web container logs"
        echo "  shell         - Open shell in web container"
        echo "  migrate       - Run database migrations"
        echo "  collectstatic - Collect static files"
        echo "  createsuperuser - Create Django superuser"
        echo "  clean         - Clean up Docker resources"
        exit 1
        ;;
esac 