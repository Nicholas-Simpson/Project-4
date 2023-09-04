import matplotlib.pyplot as plt
import numpy as np

classes = ['3', '4', '5', '6', '7', '8']
precision = [0.00, 1.00, 0.65, 0.52, 0.61, 0.00]
recall = [0.00, 0.12, 0.74, 0.60, 0.32, 0.00]
f1_score = [0.00, 0.22, 0.69, 0.56, 0.42, 0.00]

x = np.arange(len(classes))
width = 0.2

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, precision, width, label='Precision')
rects2 = ax.bar(x, recall, width, label='Recall')
rects3 = ax.bar(x + width, f1_score, width, label='F1-Score')

ax.set_ylabel('Test')
ax.set_xlabel("Predictions")
ax.set_title('Classification Report')
ax.set_xticks(x)
ax.set_xticklabels(classes)
ax.legend()

fig.tight_layout()

plt.show()
