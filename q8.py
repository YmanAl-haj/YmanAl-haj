class Country():
	def __init__(self, country_name):
		self.country_name = country_name

	def display(self):
		print(self.country_name)
		

class City(Country):
	def __init__(self, country_name,city_name,user_name):
		self.city_name=city_name
		self.__user_name=user_name

		super(Country, self).__init__()
		self.country_name = country_name

	def get_user_name(self):
		return 	self.__user_name

	def set_user_name(self,name):
			if name.isalpha():
				self.__user_name=name
			else:
				print("Sorry ",name,"is not defined")					

	def display(self):
		print("Country Name is: ",self.country_name)
		print("City Name is: ",self.city_name)
		

city=City("Sana'a","Yemen","Ali")
city.display()
city.set_user_name("Arwa")
print(city.get_user_name())



	


