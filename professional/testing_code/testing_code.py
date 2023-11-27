from string import capwords

value = "   hi_my name is ryan   "

if value.strip():
            value = capwords(value)
	
print(value)