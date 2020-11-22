import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('1', '100', '1000','10000','100000','1048000','10230000')
y_pos = np.arange(len(objects))
performance = [45207.02362060547,71541.54777526855,72881.46018981934, 78318.35746765137, 85385.08415222168,122057.91473388672, 454283.6856842041]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Time')
plt.title('us-west-1')
plt.show()

import matplotlib.pyplot as plt

plt.plot(objects,performance)
plt.title('Latency - us-west-1')
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