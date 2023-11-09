from cerberus import Validator


# schema = {'numbers': {'type':'integer'}}
# v = Validator(schema)
# data = {'numbers': 5}
# if v.validate(data):
#     print("Data is valid")
# else:
#     print("Data is invalid")

# validating with various rules and printing errors
# v = Validator()
# v.schema = {'ID': {'required': True, 'type': 'number'}, 'age': {'type': 'integer'}}
# if v.validate({'age': 60}):
#     print('Data is valid')
# else:
#     print('Data is invalid')
#     print(v.errors)


# Setting min and max value ranges
# v = Validator()
# v.schema = {'name': {'type': 'string', 'minlength': 5, 'maxlength': 10}, 'age': {'type': 'integer', 'min':18, 'max': 65}}
# if v.validate({'name': 'VJ', 'age': 16}):
#     print('Date is valid')
# else:
#     print('Data is valid')
#     print(v.errors)


