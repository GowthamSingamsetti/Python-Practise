'''class Car:
	def _init_(self, company, model):
		self.company = company
		self.model = model
Dzire = Car('Maruti','Swift Dzire ZX')
print(Dzire.model)
print(Dzire.mfg_years)


class ABC:
	def _init_(self, var):
		self._var = var
	def display(self):
		print("From class method, var = ",self._var)
obj = ABC(10)
obj.display()


class Car:
	def _init_(self, company, model):
		self.company = company
		self.model = model
	def display(self):
		print("Company = %s, Model = %s"%(self.company, self.model))
Dzire = Car('Maruti','Swift Dzire ZX')
del Dzire.display()
Dzire.display()


class Car:
	def _init_(self, company, model):
		self.company = company
		self.model = model
Dzire = Car('Maruti','Swift Dzire ZX')
print(Dzire.model)


class ABC():
	def _init_(self, var):
		self._var = var
	def display(self):
		print("From class method, var = ",self._var)
obj = ABC(10)
obj.display()
print("From main module, var = ",obj._var)'''
