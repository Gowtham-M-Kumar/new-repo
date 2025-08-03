@echo off

REM Docker commands for Django Portfolio Project

if "%1"=="build" (
    echo Building Docker image...
    docker build -t portfolio-app .
    goto :eof
)

if "%1"=="run" (
    echo Running with Docker Compose (production)...
    docker-compose up -d
    goto :eof
)

if "%1"=="dev" (
    echo Running with Docker Compose (development)...
    docker-compose -f docker-compose.dev.yml up -d
    goto :eof
)

if "%1"=="stop" (
    echo Stopping containers...
    docker-compose down
    goto :eof
)

if "%1"=="logs" (
    echo Showing logs...
    docker-compose logs -f web
    goto :eof
)

if "%1"=="shell" (
    echo Opening shell in web container...
    docker-compose exec web bash
    goto :eof
)

if "%1"=="migrate" (
    echo Running migrations...
    docker-compose exec web python manage.py migrate
    goto :eof
)

if "%1"=="collectstatic" (
    echo Collecting static files...
    docker-compose exec web python manage.py collectstatic --noinput
    goto :eof
)

if "%1"=="createsuperuser" (
    echo Creating superuser...
    docker-compose exec web python manage.py createsuperuser
    goto :eof
)

if "%1"=="clean" (
    echo Cleaning up Docker resources...
    docker-compose down -v
    docker system prune -f
    goto :eof
)

echo Usage: %0 {build^|run^|dev^|stop^|logs^|shell^|migrate^|collectstatic^|createsuperuser^|clean}
echo.
echo Commands:
echo   build         - Build Docker image
echo   run           - Run production environment
echo   dev           - Run development environment
echo   stop          - Stop all containers
echo   logs          - Show web container logs
echo   shell         - Open shell in web container
echo   migrate       - Run database migrations
echo   collectstatic - Collect static files
echo   createsuperuser - Create Django superuser
echo   clean         - Clean up Docker resources 