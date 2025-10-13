from collections import UserDict

class Field:
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return str(self.value)

class Name(Field):
	pass

class Phone(Field):
	def __init__(self, value):
		if not value.isdigit() or len(value) != 10:
			raise ValueError("Phone number must contain exactly 10 digits.")
		super().__init__(value)

class Record:
	def __init__(self, name):
		self.name = Name(name)
		self.phones = []

	def add_phone(self, phone_str):
		phone = Phone(phone_str)
		self.phones.append(phone)

	def remove_phone(self, phone_str):
		for phone in self.phones:
			if phone == phone_str:
				self.phones.remove(phone_str)
			return
		raise ValueError(f"Phone number {phone_str} not found.")

	def edit_phone(self, old_phone_str, new_phone_str):
		for i, phone in enumerate(self.phones):
			if phone.value == old_phone_str:
				self.phones[i] = Phone(new_phone_str)
			return
		raise ValueError(f"Phone number {old_phone_str} not found.")

	def find_phone(self, phone_str):
		for phone in self.phones:
			if phone.value == phone_str:
				return phone
		return None

	def __str__(self):
		return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
		def add_record(self, record):
			self.data[record.name.value] = record

		def find(self, name):
			return self.data.get(name)

		def delete(self, name):
			if name in self.data:
				del self.data[name]

		def __str__(self):
			return "\n".join(str(record) for record in self.data.values())


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")

