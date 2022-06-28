from nested_lookup import nested_lookup

#https://pypi.org/project/nested-lookup/

document = [ { 'taco' : 42 } , { 'salsa' : [ { 'burrito' : { 'taco' : 69 } } ] } ]

print(nested_lookup('taco', document))