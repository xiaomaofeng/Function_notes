# def fetch(url):
#     sock = socket.socket()
#     sock.connect(('www.runoob.com', 80))
#     request = 'GET {} HTTP/1.0\r\nHost: www.runoob.com\r\n\r\n'.format(url)
#     sock.send(request.encode('ascii'))
#     response = b'' #Empty array of bytes.
#     chunk = sock.recv(4096)
#     while chunk:
#         response += chunk
#         chunk = sock.recv(4096)
#
#     #Page is now dowloaded.
#     links = parse_links(response)
#     q.add(links)

# import numpy;
#
#
# array = numpy.arange(5)#; array
# #array([0, 1, 2, 3, 4])
# print(array)
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import matplotlib
print(matplotlib.get_backend())
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

x = np.linspace(0,4,50)
y = func(x, 2.5, 1.3, 0.5)
ydata = y+0.2 * np.random.normal(size=len(x))
popt, pcov = curve_fit(func, x, ydata)
plt.plot(x, ydata, 'b*')
plt.plot(x, func(x, popt[0], popt[1], popt[2]), 'r-')
#plt.title('$f(x)=ae^{-bx}+c$ curve fitting')
plt.title('a * np.exp(-b * x) + c curve fitting')
plt.show()