list1=[12,"HARRY",1,23,45,6,"MOKSH","ASGARD",2354.75,True,3,False]
for item in list1:
  if type(item)==int or type(item)==float or type(item)==bool:
      if item>6 or type(item)==bool:
          print(item)
