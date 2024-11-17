def gini_impurity(target_column):
  values,counts=np.unique(target_column,return_counts=True)
  prop=counts/counts.sum()
  g_imp=1-np.sum(prop**2)
  return g_imp
def gini_gain(data,feature,target_column):
   total_impurity=gini_impurity(data[target_column])
   values,counts=np.unique(data[feature],return_counts=True)
   weighted_impurity=sum((counts[i]/counts.sum())*gini_impurity(data[data[feature]==values[i]][target_column]) for i in range(len(values)))
   gain=total_impurity-weighted_impurity
   return gain

def gini_gain(data,feature,target_column):
  total_impurity=gini_impurity(data[target_column])
  values,counts=np.unique(data[feature],return_counts=True)
  weighted_impurity=0
  for i,value in enumerate(values):
    weighted_impurity += (counts[i]/counts.sum())*gini_impurity(data[data[feature]==value][target_column])
  gain=total_impurity-weighted_impurity
  return gaindef cart(data,original_data,features,target_column,parent_node_class=None):
  target_gini=gini_impurity(data[target_column])
  if target_gini>0:
    print(f"Target gini impurity is {target_gini}")
  if len(np.unique(data[target_column]))==1:
    return np.unique(data[target_column])[0]
  elif len(data)==0:
    return parent_node_class
  elif len(features)==0:
    return np.unique(original_data[target_column])[np.argmax(np.unique(original_data[target_column],return_counts=True)[1])]
  else:
    parent_node_class=np.unique(data[target_column])[np.argmax(np.unique(data[target_column],return_counts=True)[1])]
    gini_gains=[]
    for feature in features:
      gg=gini_gain(data,feature,target_column)
      gini_gains.append(gg)
      print(f"Gini Gain for feature {feature}:{gg}")
    best_feature=features[np.argmax(gini_gains)]
    print(f"Best feature is {best_feature}")
    tree={best_feature:{}}
    features=[f for f in features if f!=best_feature]
    for value in np.unique(data[best_feature]):
      sub_data=data[data[best_feature]==value]
      subtree=cart(sub_data,original_data,features,target_column)
      tree[best_feature][value]=subtree
    return tree
def predict(tree,sample):
  for node in tree.keys():
    value=sample[node]
    subtree=tree[node].get(value,None)
    if isinstance(subtree,dict):
      return predict(tree,sample)
    else:
      return subtree
data = pd.DataFrame({
    'Age': ['<=30','<=30','31..40','>=40','>=40','>=40','31..40','<=30','<=30','>=40','<=30','31..40','31..40','>=40'],
    'Income': ['High', 'High', 'High', 'Medium', 'Low', 'Low', 'Low', 'Medium', 'Low', 'Medium', 'Medium','Medium','High','Medium'],
    'Student': ['N','N','N','N','Y','Y','Y','N','Y','Y','Y','N','Y','N'],
    'CR':['F','E','F','F','F','E','E','F','F','F','E','E','F','E'],
    'BUYS COMPUTER':['N','N','Y','Y','Y','N','Y','N','Y','Y','Y','Y','Y','N']
})

features = list(data.columns[:-1])
tree = cart(data, data, features, target_column="BUYS COMPUTER")
print("\nDecision Tree:", tree)

new_patient = {'Age': '31..40', 'Income': 'Low', 'Student': 'Y','CR':'E'}
prediction = predict(tree, new_patient)
print("Prediction for new patient:", prediction)
