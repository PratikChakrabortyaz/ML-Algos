positives=np.array([[3,1],[3,-1],[6,1],[6,-1]])
negatives=np.array([[1,0],[0,1],[0,-1],[-1,0]])
X=np.vstack([positives,negatives])
y=np.array([1]*len(positives)+[-1]*len(negatives))
def fit_svm(X,y):
  pos=X[y==1]
  neg=X[y==-1]
  pos_mean=np.mean(pos,axis=0)
  neg_mean=np.mean(neg,axis=0)
  normal_vector=pos_mean-neg_mean
  b=-0.5*(np.dot(pos_mean,normal_vector)+np.dot(neg_mean,normal_vector))
  return normal_vector,b
w,b=fit_svm(X,y)
print(f"w is {w},b is {b}")
def plot_svm(X,y,w,b):
  plt.scatter(X[y==1][:,0],X[y==1][:,1],color='red')
  plt.scatter(X[y==-1][:,0],X[y==-1][:,1],color='blue')
  x_min,x_max=X[:,0].min()-1,X[:,0].max()+1
  y_min,y_max=X[:,1].min()-1,X[:,1].max()+1
  xx,yy=np.meshgrid(np.linspace(x_min,x_max,100),np.linspace(y_min,y_max,100))
  Z=w[0]*xx+w[1]*yy+b
  plt.contour(xx,yy,Z,levels=[0],color='green')
  plt.xlim(x_min,x_max)
  plt.ylim(y_min,y_max)
  plt.show()
plot_svm(X,y,w,b)
