data = np.array([
    [150, 4.5, "Apple"],
    [170, 5.0, "Apple"],
    [140, 4.0, "Apple"],
    [190, 6.0, "Orange"],
    [175, 5.5, "Orange"],
    [165, 6.0, "Orange"]
])
new_fruit = np.array([165,5.5])
def euclidian_distance(point1, point2):
  return np.sqrt(np.sum((point1-point2)**2))

def manhattan_distance(point1,point2):
  return np.sum(np.abs(point1-point2))

def mikowski_distance(point1, point2,p=3):
  return np.sum(np.abs(point1-point2)**p)**(1/p)
def knn(new_fruit, k, distance_metric):
    distances = []

    for fruit in data:
        fruit_features = fruit[:2].astype(float)

        if distance_metric == "euclidean":
            dist = euclidian_distance(new_fruit, fruit_features)
        elif distance_metric == "manhattan":
            dist = manhattan_distance(new_fruit, fruit_features)
        elif distance_metric == "minkowski":
            dist = mikowski_distance(new_fruit, fruit_features)

        distances.append((dist, fruit[2]))


    distances.sort(key=lambda x: x[0])
    distances = distances[:k]


    labels = [label for _, label in distances]
    max_label = max(set(labels), key=labels.count)

    return max_label, distances


dist_metrics = ['euclidean', 'manhattan', 'minkowski']
for metric in dist_metrics:
    prediction, dists = knn(new_fruit, k=3, distance_metric=metric)
    print(f"Metric: {metric.capitalize()}, Prediction: {prediction}")
    for dist, label in dists:
        print(f"Distance: {dist:.2f}, Label: {label}")
predicted_label,_ = knn(new_fruit, k=3, distance_metric="euclidean")
new_fruit_color = "red" if predicted_label == "Apple" else "orange"
print(f"Label for new class is {predicted_label}")
# Add the new fruit to the data array
new_fruit_with_label = np.append(new_fruit, predicted_label)
data = np.vstack([data, new_fruit_with_label])
weights = data[:, 0].astype(float)
sweetness = data[:, 1].astype(float)
labels = data[:, 2]

def plot_data():
    # Map labels to colors
    colors = {"Apple": "red", "Orange": "orange"}
    plot_colors = [colors[label] for label in labels]

    # Scatter plot all fruits including the new fruit
    plt.scatter(weights, sweetness, color=plot_colors, edgecolor='black')


    plt.xlabel('Weight')
    plt.ylabel('Sweetness')
    plt.title('Fruit Classification with KNN')



    # Show the plot
    plt.show()

# Plot the data
plot_data()
