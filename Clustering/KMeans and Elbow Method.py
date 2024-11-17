# Sample data for 10 people (Age, Height, Weight)
data = np.array([
    [25, 175, 70],
    [30, 180, 75],
    [35, 170, 60],
    [40, 165, 65],
    [28, 160, 55],
    [50, 155, 72],
    [48, 158, 68],
    [45, 162, 63],
    [32, 168, 70],
    [27, 172, 80]
])
# Euclidean Distance Function
def euclidean_distance(point, centroid):
    return np.sqrt(np.sum((point - centroid) ** 2))

# K-means Clustering Function
def k_means_clustering(data, k, max_iterations=100):
    n_samples, n_features = data.shape
    centroids = data[np.random.choice(n_samples, k, replace=False)]
    clusters = np.zeros(n_samples)
    sse_list = []

    for iteration in range(max_iterations):
        # Assign clusters based on closest centroid
        for i, point in enumerate(data):
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            clusters[i] = np.argmin(distances)

        # Calculate SSE
        sse = 0
        for j in range(k):
            points_in_cluster = data[clusters == j]
            if len(points_in_cluster) > 0:
                sse += np.sum((points_in_cluster - centroids[j]) ** 2)
        sse_list.append(sse)

        # Update centroids
        new_centroids = np.array([data[clusters == j].mean(axis=0) if len(data[clusters == j]) > 0 else centroids[j] for j in range(k)])

        # Check for convergence
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids

    return clusters, centroids, sse_list
# Plotting Clusters
def plot_clusters(data, clusters, centroids, k):
    plt.figure()
    for i in range(k):
        points = data[clusters == i]
        plt.scatter(points[:, 0], points[:, 1], label=f'Cluster {i+1}')
    plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red', marker='X', label='Centroids')
    plt.xlabel('Age')
    plt.ylabel('Height')
    plt.legend()
    plt.show()
# Optimal K Calculation using Largest Absolute Drop in SSE
def find_optimal_k(sse_values):
    sse_diffs = np.diff(sse_values)
    optimal_k = np.argmax(sse_diffs) + 1  # +1 to get the corresponding K value (starting from K=2)
    return optimal_k

# SSE Plotting with Optimal K Line
def plot_sse_vs_k(sse_values):
    optimal_k = find_optimal_k(sse_values)
    plt.plot(range(1, len(sse_values) + 1), sse_values, marker='o')
    plt.axvline(x=optimal_k, color='r', linestyle='--', label=f'Optimal K = {optimal_k}')
    plt.xlabel("Number of Clusters (K)")
    plt.ylabel("Sum of Squared Errors (SSE)")
    plt.title("Elbow Method for Optimal K")
    plt.legend()
    plt.show()
    print(f"The optimal number of clusters (K) is: {optimal_k}")
# Running K-means for K=1 to 4
k_values = [1, 2, 3, 4]
sse_summary = []

for k in k_values:
    clusters, centroids, sse_list = k_means_clustering(data, k)
    sse_summary.append({'K': k, 'SSE': sse_list[-1]})
    plot_clusters(data, clusters, centroids, k)

# Create and display the SSE vs K table
sse_df = pd.DataFrame(sse_summary)
print("SSE vs K Table")
print(sse_df)

# Plotting SSE vs. K with the Elbow Method
plot_sse_vs_k(sse_df['SSE'])
