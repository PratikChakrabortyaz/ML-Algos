# Define 1-dimensional data points
data_points = np.array([18, 22, 25, 27, 42, 43]).reshape(-1, 1)
# Function to compute the single linkage distance between two clusters
def single_linkage_distance(cluster1, cluster2):
    return np.min([np.abs(a - b) for a in cluster1 for b in cluster2])

# Initialize clusters (each point starts as its own cluster)
clusters = [[point] for point in data_points.flatten()]

# Print initial proximity matrix
def print_proximity_matrix(clusters):
    n = len(clusters)
    proximity_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            proximity_matrix[i][j] = proximity_matrix[j][i] = single_linkage_distance(clusters[i], clusters[j])
    print(pd.DataFrame(proximity_matrix, index=[f'C{i+1}' for i in range(n)], columns=[f'C{i+1}' for i in range(n)]))
# Perform clustering
iteration = 1
while len(clusters) > 1:
    print(f"Iteration {iteration}")
    print("Current Clusters:", clusters)
    print_proximity_matrix(clusters)

    # Find the two clusters with the smallest single-linkage distance
    min_distance = float('inf')
    cluster_to_merge = (None, None)
    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            dist = single_linkage_distance(clusters[i], clusters[j])
            if dist < min_distance:
                min_distance = dist
                cluster_to_merge = (i, j)

    # Merge the two closest clusters
    i, j = cluster_to_merge
    clusters[i] = clusters[i] + clusters[j]  # Merge clusters
    del clusters[j]  # Remove the merged cluster

    print(f"Merging clusters {i+1} and {j+1} with distance {min_distance}\n")
    iteration += 1
