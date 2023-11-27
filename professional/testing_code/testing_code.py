value = "   hi there my name is ryan   "

if len(value.strip()) > 0:
	value = " ".join([idx.title() for idx in value.strip().split(" ")])
	
print(value)