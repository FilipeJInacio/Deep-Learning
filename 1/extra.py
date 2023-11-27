import numpy as np

# Load the npz file
file_path = 'octmnist.npz'
data = np.load(file_path)

# Extract the data and labels
train_images = data['train_images']
train_labels = data['train_labels']

# Count the number of elements for each class in the training set
class_counts_train = {i: np.sum(train_labels == i) for i in range(4)}  # Assuming there are 10 classes

# Print the results for the training set
print("Training set:")
for class_label, count in class_counts_train.items():
    print(f"Class {class_label}: {count} elements")

# Repeat the process for validation and test sets if needed
val_images = data['val_images']
val_labels = data['val_labels']
class_counts_val = {i: np.sum(val_labels == i) for i in range(4)}

print("\nValidation set:")
for class_label, count in class_counts_val.items():
    print(f"Class {class_label}: {count} elements")

test_images = data['test_images']
test_labels = data['test_labels']
class_counts_test = {i: np.sum(test_labels == i) for i in range(4)}

print("\nTest set:")
for class_label, count in class_counts_test.items():
    print(f"Class {class_label}: {count} elements")
