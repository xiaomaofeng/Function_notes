import socket


def fetch(url):
    sock = socket.socket()
    sock.connect(('www.baidu.com', 80))
    request = 'GET {} HTTP/1.0\r\nHost:www.baidu.com\r\n\r\n'.format(url)
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)

    #Page is now download.
    links = parse_links(response)
    q.add(links)
