# rpi_led_control_python
This is the learning repository to contorl the leds on the raspberry pi with the python language.

## Deployment

For Developers:
```
docker-compose -f docker/docker-compose.dev.yml up --build --remove-orphans
```

For Production:
```
docker-compose -f docker/docker-compose.yml -f docker/docker-compose.dev.yml up --build --remove-orphans
```