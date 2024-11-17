text=["A great game","The election was over","Very clean match","A clean but forgettable game","It was a close election"]
tag=["Sports","Not sports","Sports","Sports","Not sports"]
test="A very close game"
d_pos={}
d_neg={}
unique_words=set()
n=len(tag)
pos_len,neg_len=0,0
tech,non_tech=tag.count('Sports'),tag.count('Not sports')
for i in range(n):
  words = text[i].lower().split()
  if tag[i]=='Sports':
    for word in words:
      d_pos[word]=d_pos.get(word,0)+1
      pos_len+=1
  else:
    for word in words:
      d_neg[word]=d_neg.get(word,0)+1
      neg_len+=1
  unique_words.update(words)
len_unique=len(unique_words)
prob_pos,prob_neg={},{}
for word in test.lower().split():
  prob_pos[word]=(d_pos.get(word,0)+1)/(len_unique+pos_len)
  prob_neg[word]=(d_neg.get(word,0)+1)/(len_unique+neg_len)
Ptech_cond=tech/n
Pnontech_cond=non_tech/n
for k in prob_pos.values():
  Ptech_cond*=k
for k in prob_neg.values():
  Pnontech_cond*=k
print(Ptech_cond)
print(Pnontech_cond)
