def entropy(target_column):
  values,counts=np.unique(target_column,return_counts=True)
  prob=counts/counts.sum()
  ent=-np.sum(prob*np.log2(prob))
  return ent

def information_gain(data, feature, target_column):
    total_entropy = entropy(data[target_column])
    values, counts = np.unique(data[feature], return_counts=True)
    weighted_entropy = 0
    for i, value in enumerate(values):
        weighted_entropy += (counts[i] / counts.sum()) * entropy(data[data[feature] == value][target_column])
    return total_entropy - weighted_entropy

def split_info(data,feature):
  _,counts=np.unique(data[feature],return_counts=True)
  prop=counts/counts.sum()
  split_info_val=-np.sum(prop*np.log2(prop))
  return split_info_val
def gain_ratio(data,feature,target_column):
  info_gain=information_gain(data,feature,target_column)
  split_info_val=split_info(data,feature)
  if split_info_val==0:
    return 0
  return info_gain/split_info_val
def c4_5(data,original_data,features,target_column,parent_node_class=None):
  target_entropy=entropy(data[target_column])
  if target_entropy>0:
    print(f"Target entropy is {target_entropy}")
  if len(np.unique(data[target_column]))==1:
    return np.unique(data[target_column])[0]
  elif len(data)==0:
    return parent_node_class
  elif len(features)==0:
    return np.unique(original_data[target_column])[np.argmax(np.unique(original_data[target_column],return_counts=True)[1])]
  else:
    parent_node_class=np.unique(data[target_column])[np.argmax(np.unique(data[target_column],return_counts=True)[1])]
    gain_ratios=[]
    for feature in features:
      gr=gain_ratio(data,feature,target_column)
      gain_ratios.append(gr)
      print(f"Gain ratio for {feature}:{gr}")
    best_feature=features[np.argmax(gain_ratios)]
    print(f"Best feature is {best_feature}")
    tree={best_feature:{}}
    features=[f for f in features if f!=best_feature]
    for value in np.unique(data[best_feature]):
      sub_data=data[data[best_feature]==value]
      sub_tree=c4_5(sub_data,original_data,features,target_column)
      tree[best_feature][value]=sub_tree
    return tree
def predict(tree,sample):
  for node in tree.keys():
    value=sample[node]
    subtree=tree[node].get(value,None)
    if isinstance(subtree,dict):
      return predict(subtree,sample)
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
tree = c4_5(data, data, features, target_column="BUYS COMPUTER")
print("\nDecision Tree:", tree)

new_patient = {'Age': '31..40', 'Income': 'Low', 'Student': 'Y','CR':'E'}
prediction = predict(tree, new_patient)
print("Prediction for new patient:", prediction)
