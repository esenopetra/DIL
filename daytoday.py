from datetime import date


class Date:
	def __init__(self, d, m, y):
		self.d = d
		self.m = m
		self.y = y


monthDays = [31, 28, 31, 30, 31, 30,
			31, 31, 30, 31, 30, 31]



def countLeapYears(d):

	years = d.y

	if (d.m <= 2):
		years -= 1

	
	ans = int(years / 4)
	ans -= int(years / 100)
	ans += int(years / 400)
	return ans


def daylived(bd,bm,by):
	md = 31
	mm=12
	if (isinstance(bm, str)):
		result ="Error::Type month in number"
	else:

		if bd > md and bm>mm:
			result="Error::Invalid Input"
		else:
			dt1 = Date(bd, bm, by)
			today=date.today()
			d=today.day
			m=today.month
			y=today.year
			dt2 = Date(d, m, y)
			
			n1 = dt1.y * 365 + dt1.d

			for i in range(0, dt1.m - 1):
				n1 += monthDays[i]

			
			n1 += countLeapYears(dt1)

			
			n2 = dt2.y * 365 + dt2.d
			for i in range(0, dt2.m - 1):
				n2 += monthDays[i]
			n2 += countLeapYears(dt2)
			result = n2-n1
	
		

	
	#return (n2 - n1)
	return result



# bd=int(input("Birth date : "))
# bm=int(input("Birth month : "))
# by=int(input("Birth year : "))

# result = daylived(bd,bm,by)
# print(result)