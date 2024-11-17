# Entropy function
def entropy(target_column):
    values, counts = np.unique(target_column, return_counts=True)
    probabilities = counts / counts.sum()
    ent = -np.sum(probabilities * np.log2(probabilities))
    return ent

# Information Gain function
def information_gain(data, feature, target_name="BUYS COMPUTER"):
    total_entropy = entropy(data[target_name])
    values, counts = np.unique(data[feature], return_counts=True)
    weighted_entropy = sum((counts[i] / counts.sum()) * entropy(data[data[feature] == values[i]][target_name])
                           for i in range(len(values)))
    ig = total_entropy - weighted_entropy
    return ig

# ID3 function with adjusted print statements for target entropy
def id3(data, original_data, features, target_name="BUYS COMPUTER", parent_node_class=None):
    # Calculate entropy of the target variable for this split and print only if not pure
    target_entropy = entropy(data[target_name])
    if target_entropy > 0:
        print(f"\nEntropy of target (Diagnosis) at this split: {target_entropy}")

    # If all target values are the same, return that class without further calculation
    if len(np.unique(data[target_name])) == 1:
        return np.unique(data[target_name])[0]

    # If the dataset is empty, return the parent node class
    elif len(data) == 0:
        return parent_node_class

    # If no features left, return the majority class in the original dataset
    elif len(features) == 0:
        return np.unique(original_data[target_name])[np.argmax(np.unique(original_data[target_name], return_counts=True)[1])]

    # Otherwise, calculate IG for each feature and choose the best feature
    else:
        parent_node_class = np.unique(data[target_name])[np.argmax(np.unique(data[target_name], return_counts=True)[1])]

        print("Calculating Information Gain for each feature:")
        ig_values = []
        for feature in features:
            ig = information_gain(data, feature, target_name)
            ig_values.append(ig)
            print(f"Information Gain for {feature}: {ig}")

        # Choose the feature with the highest information gain
        best_feature = features[np.argmax(ig_values)]
        print(f"Best feature chosen for split: {best_feature}")

        # Create tree structure for the selected best feature
        tree = {best_feature: {}}
        features = [f for f in features if f != best_feature]

        # For each value in the best feature, split and recurse
        for value in np.unique(data[best_feature]):
            sub_data = data[data[best_feature] == value]
            subtree = id3(su
            b_data, original_data, features, target_name, parent_node_class)
            tree[best_feature][value] = subtree

        return tree
        # Prediction function
def predict(tree, sample):
    for node in tree.keys():
        value = sample[node]
        subtree = tree[node].get(value, None)

        if isinstance(subtree, dict):
            return predict(subtree, sample)
        else:
            return subtree
# Example dataset
data = pd.DataFrame({
    'Age': ['<=30','<=30','31..40','>=40','>=40','>=40','31..40','<=30','<=30','>=40','<=30','31..40','31..40','>=40'],
    'Income': ['High', 'High', 'High', 'Medium', 'Low', 'Low', 'Low', 'Medium', 'Low', 'Medium', 'Medium','Medium','High','Medium'],
    'Student': ['N','N','N','N','Y','Y','Y','N','Y','Y','Y','N','Y','N'],
    'CR':['F','E','F','F','F','E','E','F','F','F','E','E','F','E'],
    'BUYS COMPUTER':['N','N','Y','Y','Y','N','Y','N','Y','Y','Y','Y','Y','N']
})

# Build the decision tree
features = list(data.columns[:-1])  # All columns except target
tree = id3(data, data, features, target_name="BUYS COMPUTER")
print("\nDecision Tree:", tree)

# Predict for a new patient
new_patient = {'Age': '31..40', 'Income': 'Low', 'Student': 'Y','CR':'E'}
prediction = predict(tree, new_patient)
print("Prediction for new patient:", prediction)
