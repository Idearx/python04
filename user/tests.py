import json

from django.test import TestCase

# Create your tests here.
data = {
    'uid':1,
    'name':'亚伦',
    "age":23,
    'gender':"男",
    'result':{
        'bool':False,
    }
}

print(data,type(data))

data1 = json.dumps(data)
print(data1,type(data1))

data2 = json.loads(data1)
print(data2,type(data2))