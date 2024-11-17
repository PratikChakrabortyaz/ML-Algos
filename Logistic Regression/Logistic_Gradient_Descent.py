x=np.array([1,2,3,4])
y=np.array([0,0,1,1])
b0,b1,alpha,epochs=0,0,0.01,50
loss=[]
def sigmoid(z):
  return 1/(1+np.exp(-z))
def compute_loss(y,y_pred):
  return -np.mean((y*np.log(y_pred+1e-15)+(1-y)*np.log(1-y_pred+1e-15)))
for _ in range(epochs):
  h=b0+b1*x
  y_pred=sigmoid(h)
  error=y_pred-y
  b0-=alpha*np.mean(error)
  b1-=alpha*np.mean(error*x)
  epoch_error=compute_loss(y,y_pred)
  loss.append(epoch_error)
pred_probs=sigmoid(b0+b1*x)
pred_class=(pred_probs>=0.5).astype(int)
accuracy=np.mean(pred_class==y)
print(accuracy)
