def linearsearchproduct(productlist, trangetproduct):
    indices = []

    for index,products in enumerate(productlist):
        if products == trangetproduct:
            indices.append(index)
        

    return indices


products = ["shoes","boot","loafer","shoes", "sandal","shoes","loafer"]

target = "shoes"
target2 = "apple"
result = linearsearchproduct(products,target)
result2 = linearsearchproduct(products,target2)
print(result)
print(result2)