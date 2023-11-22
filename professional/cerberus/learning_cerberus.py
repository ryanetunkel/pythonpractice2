from cerberus import Validator


# # You define a validation scheam and pass it to an instance of the Validator class
# schema = {'name': {'type': 'string'}}
# v = Validator(schema)

# Then you simply invoke the validate() to validate a dictionary against the schema
# If validation succeeds, true is returned
# document = {'name': 'john doe'}
# v.validate(document)

# ****************

# Alternatively, you can pass both the dictionary and the schema to the validate() method:
# schema = {'name': {'type': 'string'}}
# document = {'name': 'john doe'}
# v = Validator()
# v.validate(document, schema)
# Which can be handy if your schema is changing through the life of the instance.

# Details about validation schemas are covered in Validation Schemas. See Validation Rules and Normalization Rules for an extensive documentation of all supported rules.

# Unlike other validation tools, Cerberus will not halt and raise an exception on the first validation issue. The whole document will always be processed, 
# and False will be returned if validation failed. You can then access the errors property to obtain a list of issues. See Errors & Error Handling for different output options.

# schema = {'name': {'type': 'string'}, 'age': {'type': 'integer', 'min': 10}}
# document = {'name': 'Little Joe', 'age': 5}
# v.validate(document, schema)
# False
# v.errors
# {'age': ['min value is 10']}
# A DocumentError is raised when the document is not a mapping.

# The Validator class and its instances are callable, allowing for the following shorthand syntax:

# document = {'name': 'john doe'}
# v(document)
# True
# New in version 0.4.1.

# Allowing the Unknown
# By default only keys defined in the schema are allowed:

# schema = {'name': {'type': 'string', 'maxlength': 10}}
# v.validate({'name': 'john', 'sex': 'M'}, schema)
# False
# v.errors
# {'sex': ['unknown field']}
# However, you can allow unknown document keys pairs by either setting allow_unknown to True:

# v.schema = {}
# v.allow_unknown = True
# v.validate({'name': 'john', 'sex': 'M'})
# True
# Or you can set allow_unknown to a validation schema, in which case unknown fields will be validated against it:

# v.schema = {}
# v.allow_unknown = {'type': 'string'}
# v.validate({'an_unknown_field': 'john'})
# True
# v.validate({'an_unknown_field': 1})
# False
# v.errors
# {'an_unknown_field': ['must be of string type']}
# allow_unknown can also be set at initialization:

# v = Validator({}, allow_unknown=True)
# v.validate({'name': 'john', 'sex': 'M'})
# True
# v.allow_unknown = False
# v.validate({'name': 'john', 'sex': 'M'})
# False
# allow_unknown can also be set as rule to configure a validator for a nested mapping that is checked against the schema rule:

# v = Validator()
# print(v.allow_unknown)

# schema = {
#     'name': {'type': 'string'},
#     'a_dict': {
#         'type': 'dict',
#         'allow_unknown': True,
#         'schema': {
#             'address': {'type': 'string'}
#             }
#         }
#     }

# v.validate({'name': 'john',
#             'a_dict': {'an_unkown_field': 'is allowed'}},
#             schema)

# print(v.errors)

# v.validate({'name': 'john',
#             'an_unknown_field': 'is not allowed',
#             'a_dict': {'an_unkown_field': 'is allowed'}},
#             schema)

# print(v.errors)


# Requiring all
# v = Validator()
# v.require_all
# print(v.require_all)

# schema = {
#     'name': {'type': 'string'},
#     'a_dict': {
#         'type': 'dict',
#         'require_all': True,
#         'schema': {
#             'address': {'type': 'string'}
#         }
#     }
# }

# v.validate({'name':'foo', 'a_dict':{}}, schema)

# print(v.errors)

# v.validate({'a_dict': {'address': 'foobar'}}, schema)

# print(v.errors)

# Fetching Processed Documents
# v = Validator()

# v.schema = {'amount': {'type': 'integer', 'coerce': int}}
# print(v.validate({'amount': '1'}))
# print(v.document)

# validated method
# there's a wrapper-method validated() that returns the validated document. If the document didn't validate, None is returned,
# unless you call the method with the keyword argument always_return_document set to True. It can be useful for flows like this:
# v = Validator()

# v.schema = {'amount': {'type': 'integer', 'coerce': int}}
# print(v.validate({'amount': '1'}))
# print(v.document)
# v = Validator(v.schema)
# valid_documents = [x for x in [v.validated(y) for y in v.documents] if x is not None]
# # If a coercion callable or method raises an exception then the exception will be caught and the validation will fail.

# # normalized method
# # Similarly, the normalized() method returns a normalized copy of a document without validating it:
# schema = {'amount': {'coerce': int}}
# document = {'model': 'consumerism', 'amount': '1'}
# normalized_document = v.normalized(document, schema)
# print(type(normalized_document['amount']))

# Warnings
# warnings, such as about deprecations or likely causes of trouble, are issued through the Python standard library's warnings module.
# The logging module can be configured to catch these logging.captureWarnings().

# Validation Schemas
# A validation schema is a mapping, usually a dict. Schema keys are the keys allowed in the target dictionary. 
# Schema values express the rules that must be matched by the corresponding target values.
# schema = {'name': {'type': 'string', 'maxlength': 10}}
# By default all keys in a document are optional unless the required rule is set True for individual fields or the validator's 
# :attr:~cerberus.Validator.require_all is set to True in order to expect all schema defined fields to be present in the document.

# registries
# There are two default registries in teh cerberus module namespace where you can store definitions for schema and rule sets which then
# can be referenced in a validation schema. You can furthermore instantiate more Registry objects and bind them to the rules_set_registry
# or schema_registry of a validator. You may also set these as keyword-adrguments upon initialization.

# Using registries is particularly interesting if:
# - schemas shall include references to themselves, vulgo: schema recursion
# - schemas contain a lot of reused parts and are supposed to be serialized

# from cerberus import schema_registry


# schema_registry.add('non-system user',
#                     {'uid': {'min': 1000, 'max': 0xffff}})
# schema = {'sender': {'schema': 'non-system user',
#                      'allow_unknown': True},
#                      'receiver': {'schema': 'non-system user',
#                                   'allow_unkown': True}}


# from cerberus import rules_set_registry


# rules_set_registry.extend((('boolean', {'type': 'boolean'}),
#                            ('booleans', {'valuesrules': 'boolean'})))
# schema = {'foo': 'booleans'}


# Validation
# Validation schemas themselves are validated when passed to the validator or a new set of rules is set for a document's field. 
# A SchemaError is raised when an invalid validation schema is encountered. See Schema Validation Schema for a reference.
# However, be aware that no validation can be triggered for all changes below that level or when a used definition in a registry changes.
# You could therefore trigger a validation and catch the exception:
# The four lines below are intentionally not working to show how it looks without catching the exception
# v = Validator({'foo': {'allowed': []}})
# v.schema['foo'] = {'allowed': 1}


# v.schema['foo']['allowed'] = 'strings are no valid constraint for allowed'
# v.schema.validate()


# Serialization 
# Cerberus schemas are built with vanilla Python types: dict, list, string, etc. Even user-defined validation rules are invoked in the schema by name as a string.
# A useful side effect of this design is that schemas can be defined in a number of ways, for example with PyYAML.
# import yaml


# v = Validator()
# schema_text = '''
# name:
#     type: string
# age:
#     type: integer
#     min: 10
# '''
# schema = yaml.safe_load(schema_text)
# document = {'name': 'Little Joe', 'age': 5}
# print(v.validate(document, schema))

# print(v.errors)

# Can use json as well as yaml or another serializer as long as there is a decoder that can produce a nested dict.
# That nested dict is what you used to define a schema
# For populating and dumping one of hte registries, use extend() and all()

# Validation Rules
# allow_uknown
# Can be used in conjunction with the schema(dict) rule when validating a mapping in order to set the allow_unkown property of the validator for the subdocument. 
# This rule has precedence over purge_unknown

# allowed
# Takes a py3:collectionsabc.Container of allowed values. Valiodates the target calue if hte value is in the allowed values. 
# If the target value is an iterable, all its members must be in the allowed values.

# v = Validator()

# v.schema = {'role': {'type': 'list', 'allowed': ['agent', 'client', 'supplier']}}
# print(v.validate({'role': ['agent', 'supplier']}))

# print(v.validate({'role': ['intern']}))

# print(v.errors)

# v.schema = {'role': {'type': 'string', 'allowed': ['agent', 'client', 'supplier']}}
# print(v.validate({'role': 'supplier'}))

# print(v.validate({'role': 'intern'}))

# print(v.errors)

# v.schema = {'a_restricted_integer': {'type': 'integer', 'allowed': [-1, 0, 1]}}
# print(v.validate({'a_restricted_integer': 2}))

# print(v.errors)

# allof
# Validates if ALL of the provided constraints validates the field - think AND
# anyof
# Validates if ANY of the provided constraints validates the field - think OR

# check_with
# Validates the value of a field by calling either a function or method
# A function must be implmented like the following prototype:
# pseudocode:
# def functionname(field, value, error):
#     if value is invalid:
#         error(field, 'error message')

