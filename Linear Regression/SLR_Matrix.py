x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([3, 4, 8, 8, 14, 12, 17, 19, 22, 24])
X=np.vstack([np.ones_like(x),x]).T
X_T_X=np.dot(X.T,X)
X_T_Y=np.dot(X.T,y)
B=np.dot(np.linalg.inv(X_T_X),X_T_Y)
print(B)
B0,B1=B
print(f"B0={B0}")
print(f"B1={B1}")
y_pred_mat=B0+B1*x
mse=np.mean((y-y_pred_mat)**2)
rmse=np.sqrt(mse)
print(f"mse={mse}")
print(f"rmse={rmse}")
