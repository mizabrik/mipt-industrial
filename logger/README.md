Важно: нет проброса портов,
поэтому клиента нужно подключать к network'у,
создаваемому compose'ом.
Пример запуска:

```bash
docker-compose up -d
docker build -t logger_client client
docker run --rm -it --network=logger_public logger_client
```
