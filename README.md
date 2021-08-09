# jigasya-telegram-bot
![Tests](https://github.com/qwanysh/jigasya-telegram-bot/actions/workflows/tests.yml/badge.svg)

### Setup
```bash
cp docker-compose.override.example.yml docker-compose.override.yml
# Configure environment variables in docker-compose.override.yml
docker-compose build
```

### Run
```bash
docker-compose up
```

### Test
```bash
docker-compose run bot pytest
```
