# korona-gov-sk-api
[![Actions Status](https://github.com/kamko/korona-gov-sk-api/workflows/Docker%20build/badge.svg)](https://github.com/kamko/korona-gov-sk-api/actions "docker build status badge")
[![image metadata](https://images.microbadger.com/badges/image/kamko/korona-gov-sk-api.svg)](https://microbadger.com/images/kamko/korona-gov-sk-api "kamko/echoer image metadata")

transforms data from https://www.korona.gov.sk/ or https://virus-korona.sk into simple json. (and saves history)

optionally sends notifications to telegram (via bot) or slack (via webhook)

- `/` or `/stats`
    ```json
    {
      "id": 1,
      "negative": 1523,
      "positive": 72,
      "tested": 1595,
      "sync_time": "2020-03-16T21:57:10.599369"
    }
    ```
- `/stats/all`
    ```json
     [
      {
        "id": 1,
        "negative": 1523,
        "positive": 72,
        "sync_time": "2020-03-16T21:57:10.599369",
        "tested": 1595
      }
    ]
    ```

## configuration via environment vars
```
SQLALCHEMY_DATABASE_URI=<path-to-sqllite-db>
CHECK_FREQUENCY=<frequency-of-korona.gov.sk-scrapes-seconds>
TELEGRAM_TARGETS = "<token>~<chat-id>;<token>~<chat-id>" # multiple separated by ;
SLACK_TARGETS = "<webhookid>;<webhookid>" # multiple separated by ;
DATA_SOURCE = "korona.gov.sk" # or "virus-korona.sk"
```

note: `https://hooks.slack.com/services/<webhookid>`

## requirements
python 3.7+

## disclaimer

deploy and use only at your own responsibility

## license
[MIT](LICENSE)
