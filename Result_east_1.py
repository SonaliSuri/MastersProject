import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Prepare', 'Commit', 'CommitACK')
y_pos = np.arange(len(objects))
performance = [0.026417255401611328*1000000, 0.021852970123291016*1000000, 0.0708770751953125*1000000]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Time')
plt.title('us-east-1')
plt.show()



