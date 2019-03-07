# Python

## Install pip

```bash
sudo apt-get purge python
sudo apt-get autoremove
sudo apt-get install python3-pip

sudo pip3 install --upgrade pip
sudo pip3 install jsonlines
sudo pip3 install urlparse2
sudo pip3 install Pillow

curl https://bootstrap.pypa.io/get-pip.py | python
# for windows need to set the path
# C:\Users\wuxiang\AppData\Local\Programs\Python\Python36\Scripts
# C:\Users\wuxiang\AppData\Local\Programs\Python\Python36

# verify pip
pip freeze

# for jsonlines
sudo pip3 install jsonlines
# for PIL and Image
sudo pip3 install Pillow
sudo pip3 install urlparse2

# uninstall
pip uninstall pillow

```

### Python networking and servers

Python3 udp tcp socket http https

```txt
socket
socketServer  Classes that simplily writing network servers
+------------+
| BaseServer |
+------------+
      |
      v
+-----------+        +------------------+
| TCPServer |------->| UnixStreamServer |
+-----------+        +------------------+
      |
      v
+-----------+        +--------------------+
| UDPServer |------->| UnixDatagramServer |
+-----------+        +--------------------+
StreamRequestHandler
DatagramRequestHandler

    TCPServer
    UDPServer
    UnixStreamServer
    UnixDatagramServer

    ForkingTCPServer
    ThreadingTCPServer
    ForkingUDPServer
    ThreadingUDPServer

```

### http

    http.client
    http.server
    urllib.request
    http.HTTPStatus

ssl a TLS/SSL wrapper for socket Objects

### requests is based on [urllib3](https://github.com/urllib3/urllib3)

requests.get()

### for pillow image

```python
from PIL import Image
```

### socks is not an official feature supported in python

[socksipy](https://sourceforge.net/projects/socksipy/)

### [C++ socket](https://www.cs.rutgers.edu/~pxk/417/notes/sockets/index.html)

```c++
#include <sys/socket>
f = socket(AF_INET, SOCK_STREAM)
```

SOCK_DIAGRAM
bind
connect
accept
read/write

[C++ Proxy](http://www.alhem.net/project/example2/index.html)

### Python concurrency

multiprocessing/threading

process/thread based parallelism

### [Import order](https://www.youtube.com/watch?v=CqvZ3vGoGs0&t=1065s)

When import a module, it actually run the code in that module, including the function definition and variables

1. current path
2. standard libiary path
3. site_package path

add to the sys.path

```python
import sys
sys.path.append('/path/to/module')
```

```sh
export PYTHONPATH="/PATH/TO/MODULE"
```

### [CI and CD --Cs50](https://www.youtube.com/watch?v=alMRNeRJKUE&t=3683s)

continous intergration and delivery
Jenkins
tomcat
git
build jobs
Unit Testing
Automated Testing
Notification
Reporting
Code Analysis

using github together with travis

[Travis CI](https://travis-ci.org)

```yml
language: python
python:
  - 3.6
install:
  - pip install -r requirements.txt
script:
  - python manage.py test
```

using containers to keep same environment

```Dockerfile
FROM   python:3
WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app
RUN pip install -r requirements/txt
ADD . /usr/src/app
```

docker-compose.yml

```yml
version: '3'
services:
    db:
        image: postgres
    migration:
        build:.
        command: python3 manage.py migrate
        volumes:
            -.:/usr/src/app
        depends_on:
            - db
    web:
        build: .
        command: python3 manage.py runserver 0.0.0.0:8000
        volumes:
            - /:/usr/src/app
        ports"
            - "8000:8000"
        depends_on:
            - db
            - migration
```

### functions

### class

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
p = Poinit(3, 5)
print(p.x)
print(p.y)
```

### static method and class method

method - need the object/instance
static method - need the class
class method - do not need the class

### **init**.py

```txt
The __init__.py files are required to make Python treat the directories as containing packages;
this is done to prevent directories with a common name, such as string, from unintentionally hiding valid modules that occur later on the module search path.
```

### **init** function

```txt
__init__ is the constructor for a class. The self parameter refers to the instance of the object (like this in C++).
```

### **main** **name**

```txt
'__main__' is the name of the scope in which top-level code executes.
Every module in python has a special attribute called __name__ . The value of __name__  attribute is set to '__main__'  when module run as main program. Otherwise the value of __name__  is set to contain the name of the modu
```
