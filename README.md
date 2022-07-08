# version 1 (80%)
pre: start rabbitmq server

send message to rabbitmq (run api localhost, port 5002):
```
python run /src/emit/app.py
```

receive message to rabbitmq (run api localhost, port 5001):
```
python run /src/receiver/app.py
```


# next step:
use docker to build project
