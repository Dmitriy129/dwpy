# Moodle - Git

## How to get Moodle accessToken?

Request:

```bash
curl --location --request GET 'http://e.moevm.info/login/token.php?username=<username>&password=<password>&service=moodle_mobile_app'
```

Response:

```json
{
    "token": "someaccesstoken", /* the value we need */
    "privatetoken": null
}
```
