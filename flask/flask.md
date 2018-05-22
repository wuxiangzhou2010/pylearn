# flask

## install

``` bash
pip3 install flask
```

## variables

url_for('index')

``` html
<a href="{{url_for('index')}}">GO back</a>
```

<!--   hide for future addtion
## layout template

``` html
{% extends "layout.html" %}
```

hide for future addtion-->

## session

``` python
from flask session import Session
if session.get("note) is None:
    session["note] = []
```