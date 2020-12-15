def eval_expr(s,d={}):
	
	moj_list = [] #moj "zasobnik"

	for i in s.split():
		if i.isdigit():
			moj_list.append(i)
		elif i in d:
			moj_list.append(str(d[i]))		
		else:
			val1 = moj_list.pop()
			val2 = moj_list.pop()
			moj_list.append(str(int(eval(val2 + i + val1))))
	
	return int(float(moj_list.pop()))
			
def to_infix(s):
	
	moj_list = [] #moj "zasobnik"

	for i in s.split():
		if i.isdigit():
			moj_list.append(i)
		else:
			val1 = moj_list.pop()
			val2 = moj_list.pop()
			moj_list.append(str("( " + val2 + " " + i + " " + val1 + " )"))
	
	return moj_list.pop()


