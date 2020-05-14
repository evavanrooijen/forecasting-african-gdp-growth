from sklearn.datasets import make_blobs
X, y = make_blobs(n_samples=50, centers=3, n_features=2,random_state=0)

def plot_2D_clusters(X, y, title):
    if X.shape[1] == 2:
        print('Can only print in 2D but this is not 2D data')
    # print y number of unique , maximum at 6 for this function for now
    df = pd.DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
    colors = {0:'red', 1:'blue', 2:'green', 3:'yellow', 4:'purple', 5:'orange'}
    fig, ax = plt.subplots()
    grouped = df.groupby('label')
    for key, group in grouped:
        group.plot(ax=ax, kind='scatter', x='x', y='y', label=key, color=colors[key])
    plt.title(title)
    plt.show()

# Visual Inspection of K
plot_2D_clusters(X, y, '3 Blobs') 

# KMeans

# GMM

