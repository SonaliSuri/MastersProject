import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Prepare', 'Commit', 'CommitACK')
y_pos = np.arange(len(objects))
performance = [0.025992870330810547*1000000, 0.000009894371032714844*1000000, 0.05437207221984863*1000000]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
plt.show()