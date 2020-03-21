import matplotlib.pyplot as plt
import request

data = request.request()
plt.plot(data['confirmed'])
plt.show()
