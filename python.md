
## Python

### Install pip
``` bash
# sudo apt-get install python3-pip 
# sudo pip3 install --upgrade pip
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
# for jsonlines
sudo pip3 install jsonlines
# for PIL and Image
sudo pip3 install Pillow
sudo pip3 install urlparse2

```

### Python networking and servers

Python3 udp tcp socket http https
``` 
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

###  for pillow image 

from PIL import Image

### socks is not an official feature supported in python

[socksipy](https://sourceforge.net/projects/socksipy/)


### [C++ socket ](https://www.cs.rutgers.edu/~pxk/417/notes/sockets/index.html)

``` c++
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
2. site_package path

add to the sys.path
``` python 
import sys
sys.path.append('/path/to/module')
```
export PYTHONPATH="/PATH/TO/MODULE"