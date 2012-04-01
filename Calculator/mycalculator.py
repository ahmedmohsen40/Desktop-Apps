# Gaurav Kakkar		200901017
# Sanket Garg		200901041

import sys
from math import *

try:
	import pygtk
	pygtk.require('2.0')
except:
	pass
try:
	import gtk
	import gtk.glade
except:
	print('GTK not available')
	sys.exit(1)

class Calculator:
	def __init__(self):
		self.gladefile = "myCalculator.glade"
		self.wTree = gtk.glade.XML(self.gladefile)
		dictionary = {
			"on_zero_clicked" : self.zero,
			"on_one_clicked" : self.one,
			"on_two_clicked" : self.two,
			"on_three_clicked" : self.three,			
			"on_four_clicked" : self.four,
			"on_five_clicked" : self.five,
			"on_six_clicked" : self.six,
			"on_seven_clicked" : self.seven,
			"on_eight_clicked" : self.eight,
			"on_nine_clicked"  : self.nine,
			"on_CE_clicked" : self.ce,
			"on_clear_clicked" : self.clear,
			"on_modulus_clicked" : self.modulus,
			"on_divide_clicked" : self.division,
			"on_multiply_clicked" : self.multiply,
			"on_subtract_clicked" : self.subtract,
			"on_point_clicked" : self.point,
			"on_equal_clicked" : self.equal,
			"on_add_clicked" : self.add,			
			"on_window_calculator_destroy" : self.quit,
			"on_off_clicked" : self.quit,
			"on_sin_clicked" : self.sin,
			"on_cos_clicked" : self.cos,
			"on_tan_clicked" : self.tan,
			"on_openbracket_clicked" : self.openbracket,
			"on_closebracket_clicked" : self.closebracket,
			"on_log_clicked" : self.log,
			"on_ln_clicked" : self.ln,
			"on_squareroot_clicked" : self.squareroot,
			"on_power_clicked" : self.power,
			"on_backspace_clicked" : self.backspace,
			}
		self.wTree.signal_autoconnect(dictionary)
		self.window = self.wTree.get_widget("window1")
		self.window.show()

	def display_operand(self, operand):
		self.wTree.get_widget("mydisplay").insert_text(operand, position=20)

	
	def compute(self, operator):
		if operator == 'clear':
			self.wTree.get_widget("mydisplay").set_text("")
		elif operator == 'CE':
			self.wTree.get_widget("mydisplay").set_text("0")	
		elif operator == '=':
			self.input_string = self.wTree.get_widget("mydisplay").get_text()
			count=0
			flag=0		
			for i in self.input_string:
				if i=='/':
					break
				else:
					count=count+1
			#print self.input_string[count+1:count+2]
			if self.input_string[count+1:count+2]=="0":
				flag=1
			try:
				if flag==0:
					self.input_string=self.input_string[:count]+"/1.0"+self.input_string[count:]
					answer = eval(self.input_string)
					self.wTree.get_widget("mydisplay").set_text(str(answer))
				else:
					self.wTree.get_widget("mydisplay").set_text("Invalid Operation")
			except:
				self.wTree.get_widget("mydisplay").set_text("Invalid Syntax")

	
	def clear(self,widget):
		self.compute("clear")

	def ce(self,widget):
		self.compute("CE")	

	def zero(self,widget):
		self.display_operand("0")	
	
	def one(self,widget):
		self.display_operand("1")

	def two(self,widget):
		self.display_operand("2")

	def three(self,widget):
		self.display_operand("3")

	def four(self,widget):
		self.display_operand("4")

	def five(self,widget):
		self.display_operand("5")

	def six(self,widget):
		self.display_operand("6")
	
	def seven(self,widget):
		self.display_operand("7")

	def eight(self,widget):
		self.display_operand("8")

	def nine(self,widget):
		self.display_operand("9")
	
	def point(self,widget):
		self.display_operand(".")	

	def modulus(self,widget):
		self.display_operand("%")	
	
	def division(self,widget):
		self.display_operand("/")	

	def multiply(self,widget):
		self.display_operand("*")	
	
	def subtract(self,widget):
		self.display_operand("-")	
	
	def equal(self,widget):
		self.compute("=")	

	def add(self,widget):
		self.display_operand("+")
		
	def sin(self, widget):
		self.display_operand("sin")

	def cos(self, widget):
		self.display_operand("cos")

	def tan(self, widget):
		self.display_operand("tan")

	def openbracket(self, widget):
		self.display_operand("(")
	
	def closebracket(self, widget):
		self.display_operand(")")

	def log(self, widget):
		self.display_operand("log10")

	def ln(self, widget):
		self.display_operand("log")

	def squareroot(self, widget):
		self.display_operand("sqrt")

	def power(self, widget):
		self.display_operand("**")

	def backspace(self, widget):
		self.wTree.get_widget("mydisplay").set_text(self.wTree.get_widget("mydisplay").get_text()[0:-1])

	def quit(self,widget):
		sys.exit(0)

if __name__ == "__main__":	
	cal = Calculator()
	gtk.main()
