import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('1', '100', '1000','10000','100000','1048000','10230000')
y_pos = np.arange(len(objects))
performance = [91368.19839477539,106181.85997009277,111442.58689880371, 123977.91862487793, 129824.9870300293,150538.4635925293, 498165.1306152344]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Time')
plt.title('us-east-2')
plt.show()

import matplotlib.pyplot as plt

plt.plot(objects,performance)
plt.title('Latency - us-east-2')
plt.xlabel('Bytes')
plt.ylabel('Time in Microseconds')
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