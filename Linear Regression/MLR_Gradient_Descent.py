x1 = np.array([1, 2, 4, 3, 5])
x2 = np.array([2, 4, 1, 3, 5])
y = np.array([1, 3, 3, 2, 5])
b0,b1,b2,alpha,epochs=0,0,0,0.01,40
loss=[]
for _ in range(epochs):
  h=b0+b1*x1+b2*x2
  error=h-y
  b0-=alpha*np.mean(error)
  b1-=alpha*np.mean(error*x1)
  b2-=alpha*np.mean(error*x2)
  y_pred=b0+b1*x1+b2*x2
  mse=np.mean((y_pred-y)**2)
  loss.append(mse)
y_pred=b0+b1*x1+b2*x2
mse=np.mean((y_pred-y)**2)
rmse=np.sqrt(mse)
print(f"b0:{b0}")
print(f"b1:{b1}")
print(f"b2:{b2}")
print(f"mse:{mse}")
print(f"rmse:{rmse}")
