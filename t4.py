import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('10000','100000','1048000','10230000','40000000','41300000')
y_pos = np.arange(len(objects))
performance = [7.01,69.23,736.19, 7110.11,28981.65, 29865.24]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Time')
plt.title('us-east-2')
plt.show()

import matplotlib.pyplot as plt

plt.plot(objects,performance)
plt.title('Throughput - us-east-2')
plt.xlabel('Bytes/s')
plt.ylabel('PPS')
plt.show()

"""








1603168394.6725395
1603168394.6862798

1603168394.6116283
1603168394.63283

1603168394.590597
1603168394.5971508

1603168394.6025865
1603168394.6148098


1603168394.5829484
1603168394.6023405"""