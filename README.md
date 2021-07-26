# jigasya-telegram-bot
![Tests](https://github.com/qwanysh/jigasya-telegram-bot/actions/workflows/tests.yml/badge.svg)

### Setup
```
cp docker-compose.override.example.yml docker-compose.override.yml
# Configure environment variables in docker-compose.override.yml
docker-compose build
```

### Run
```
docker-compose up
```

### Test
```
docker-compose run bot pytest
```
