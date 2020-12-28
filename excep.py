class AgedException(Exception):
	def __init__(self, msg):
		print("Msg : ",msg)


x = 40
if x==30:
	print("young")
else:
	raise AgedException("He is aged person")
