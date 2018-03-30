# menace_man
There were too many people in university and other places that I had to know.
But my memory is weak a little and I can't remember people and things about
them very well! So I decided to start this little project and save some data
about every person I know.

Anyway... It may be used not only in case of weak memory! It would be used to
save contacts' phone numbers and ...

You can simply run a version of this project on your server using this piece
of bash code:

```
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver 0.0.0.0:8000
```

Note that in the last command, you may replace `8000` with any port you want.
