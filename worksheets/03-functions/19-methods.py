#Obje icin tanimlanmis functionlardir.
list = [1,2,3,4,5]
list.append(6) #[1,2,3,4,5,6] #Bu bir metoddur
list = [1,2,3,4,5]
list.pop() #[1,2,3,4] #Bu bir metoddur
list = [1,2,3,4,5]
list.insert(8, 1) #[1,8,2,3,4,5] #Bu bir metoddur

#Metodun ne is yaptigini unutursak
help(list.append)
# Help on built-in function append:                                                                              
# append(object, /) method of builtins.list instance
#     Append object to the end of the list.