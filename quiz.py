def list(b):
	s = [x%3 for x in b]

	return s

 




def sorted(a,b,c):
	
	d = a + b + c
	d.sort()
	return d




def divisible(n):
	y = []
	for x in range(1,n+1):
		if x%3==0:
			y.append(x)
	return y		


def flatten(x):
	flat = []
	for sublist in x:
		for a in sublist:
			flat.append(a)
	return flat	


def	smallest(b):
   c = min(b)
   return c	

def letters(x):
	b = set(x)

	return b


def squares(n):
    a = dict()
    for x in range(149,159):
        a[x] = x**2
    return a  


def students():
   student1={'age': 19, 'name':'Eunice'}
		      
   student2={'age': 21, 'name': "Agnes"}
		      
   student3={'age': 18, 'name': 'Teresa'}
		      
   student4={'age': 22, 'name': 'Asha'}
		      

   students=[student1,student2,student3,student4]
   for student in students:
   	 age=(2019-student["age"])
   	 messege=("Hello {}, you were born in {}".format(student['name'],student['age']))
   	 print(messege)












		








		                     


		



