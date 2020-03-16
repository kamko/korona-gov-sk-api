# korona-gov-sk-api
[![Actions Status](https://github.com/kamko/korona-gov-sk-api/workflows/Docker%20build/badge.svg)](https://github.com/kamko/korona-gov-sk-api/actions "docker build status badge")
[![image metadata](https://images.microbadger.com/badges/image/kamko/korona-gov-sk-api.svg)](https://microbadger.com/images/kamko/korona-gov-sk-api "kamko/echoer image metadata")

transforms data from https://www.korona.gov.sk/ into simple json

```json
{
  "tested": 1436,
  "negative": 1375,
  "positive": 61
}
```

## configuration via environment vars
```
SQLALCHEMY_DATABASE_URI=<path-to-sqllite-db>
CHECK_FREQUENCY=<frequency-of-korona.gov.sk-scrapes-seconds>
TELEGRAM_TOKEN=<telegram-bot-token>
TELEGRAM_CHAT_ID=<telegram-chat-id>
```

## disclaimer

deploy and use only at your own responsibility

## license
[MIT](LICENSE)
