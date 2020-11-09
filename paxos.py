import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Propose', 'Accept')
y_pos = np.arange(len(objects))
performance = [0.14373135566711426*1000000, 0.1298236846923828*1000000]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Time')
plt.title('Paxos')
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