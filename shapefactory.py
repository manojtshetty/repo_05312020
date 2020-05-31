class Shape:
	def drawShape(self):
		pass
	

class Square(Shape):
	def drawShape(self):
		print('Drawing a Square')

class Circle(Shape):
	def drawShape(self):
		print('Drawing a Circle')

class Rectangle(Shape):
	def drawShape(self):
		print('Drawing a Rectangle')
		
class ShapeFactory:
	def drawShape(self,input):
		if input='Square':
			sq = Square()
			sq.drawShape()
		elif input='Circle':
			cir = Circle()
			cir.drawShape()
		elif input='Rectangle':
			rec = Rectangle()
			rec.drawShape()	
		else:
			print('Drawing a '+input+' is not supported')
			
obj = ShapeFactory()
obj.drawShape('Square')

