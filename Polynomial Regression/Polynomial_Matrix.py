x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([2, 6, 12, 20, 30, 42, 56, 72, 90, 110])
X_square=np.square(x)
X=np.vstack([np.ones_like(x),x,X_square]).T
X_T_X=np.dot(X.T,X)
X_T_Y=np.dot(X.T,y)
B=np.dot(np.linalg.inv(X_T_X),X_T_Y)
print(B)
b0,b1,b2=B
print(f"b0={b0}")
print(f"b1={b1}")
print(f"b2={b2}")
y_pred=b0+b1*x+b2*X_square
mse=np.mean((y-y_pred)**2)
rmse=np.sqrt(mse)
print(f"mse={mse}")
print(f"rmse={rmse}")
