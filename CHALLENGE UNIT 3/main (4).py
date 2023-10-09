def linearSearchProduct(productList,targetProduct):
  indices=[]
  for index, product in enumerate(productList):
   if product==targetProduct:
    indices.append(index)
  return indices

products= ["sandal","shoes","loafer","boot","sandal","shoes"]
target="sandal"
result=linearSearchProduct(products, target)
print(result)