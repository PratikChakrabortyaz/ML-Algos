x = np.array([1, 2, 4,3,5])
y = np.array([1,3,3,2,5])
b0,b1,alpha=0,0,0.01
epochs=4
n=len(x)
mse_history=[]
for _ in range(epochs):
  h=b0+b1*x
  error=h-y
  b0-=alpha*(1/n)*np.sum(error)
  b1-=alpha*(1/n)*np.sum(error*x)
  y_pred=b0+b1*x
  mse=np.mean((y-y_pred)**2)
  mse_history.append(mse)
print(f"b0={b0}")
print(f"b1={b1}")
y_pred_tot=b0+b1*x
mse=np.mean((y_pred_tot-y)**2)
rmse=np.sqrt(mse)
print(f"mse={mse}")
print(f"rmse={rmse}")
