# 💬 teleme 💬
Download your [Telegram](https://telegram.org/) messages.

# Installation:

Before working with Telegram’s API, you need to get your own API ID and hash:

1. Follow [this link](https://my.telegram.org/) and login with your phone number.
2. Click under [`API Development tools`](https://my.telegram.org/apps).
3. A Create new application window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.
4. Click on *Create application* at the end. Remember that your API hash is secret and Telegram won’t let you revoke it. **Don’t post it anywhere!**
5. Create a *`secrets.json`* file inside the root of this project. This file will be read by the application, make sure it looks like this:
```json
{
    "id": "1234556789",
    "hash": "8u23918eu1281dh912eh89sdadyas9dy89"
}
```
6. Create a new virtual environment or make sure the one you're using satisfies the [requirements](requirements.txt):

```bash
# if you want to create a new environment (with conda)
conda create --name teleme --no-default-packages python=3.7 && pip install -r requirements.txt
```

```bash
# or maybe just
pip install -r requirements.txt
```
7. You're good to go!
```bash
python downdall.py -h
```
