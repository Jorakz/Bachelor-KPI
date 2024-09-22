import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
digits = load_digits()
datas = digits.data
images = digits.images
target = digits.target



class_samples = {}
for class_l  in range(10):
    class_samples[class_l] = images[target == class_l]

print(class_samples)
print(len(class_samples[2]))

plt.figure(figsize=(15, 10))

for class_label in range(10):
    samples_for_class = class_samples[class_label]

    attribute = samples_for_class.reshape(-1)
    print('==============')
    print(attribute)
    print(len(attribute),f'Number {class_label}')
    plt.subplot(2, 5, class_label + 1)
    plt.hist(attribute, bins=10, alpha=0.4,color='black', label=f'Class {class_label}')
    plt.xlabel('Значення')
    plt.ylabel('Кількість')
    plt.title(f'Class  {class_label}')
    plt.legend()

plt.tight_layout()
plt.show()