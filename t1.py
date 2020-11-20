import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('1', '100', '1000','10000','100000','1048000','10230000')
y_pos = np.arange(len(objects))
performance = [98257.06481933594,118568.18199157715,119150.16174316406, 134236.09733581543, 136705.3985595703,173153.87725830078, 539921.9989776611]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Time')
plt.title('us-east-1')
plt.show()

import matplotlib.pyplot as plt

plt.plot(objects,performance)
plt.title('Latency')
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