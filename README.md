Zeus Data consumption API
==============================

An api for Zeus data consumption

## Develop

To develop:

```
vagrant up
```

```
vagrant ssh
```

```
cd /vagrant
```

```
python zeus_api/manage.py migrate
```

Hack some code now :), and then:

```
python zeus_api/manage.py runserver 0.0.0.0:8000
```

Then you can navigate to `http://localhost:8000` in your browser.

## Docs - Swagger
To see the swagger docs, navigate to: `http://localhost:8000/docs`

## Test

To test, run:

```
python zeus_api/manage.py test
```

Zeus Team.