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
		s = str(value)
		if not s.isdigit() or len(s) != 10:
			raise ValueError("Phone number must contain exactly 10 digits.")
		super().__init__(s)

class Record:
	def __init__(self, name):
		self.name = Name(name)
		self.phones = []

	def add_phone(self, phone_str):
		phone = Phone(phone_str)
		self.phones.append(phone)

	def remove_phone(self, phone_str):
		for phone in self.phones:
			if phone.value == phone_str:
				self.phones.remove(phone)
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
		if not self.data:
			return "AddressBook: <empty>"
		return "\n".join(str(record) for record in self.data.values())


book = AddressBook()
print("=== Створюємо нову адресну книгу ===")
print(book)
print()
# Додаємо John
print("=== Додаємо контакт John з двома телефонами ===")
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)
print(book)
print()
# Додаємо Jane
print("=== Додаємо контакт Jane ===")
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)
print(book)
print()
# Редагуємо телефон у John
print("=== Редагуємо телефон John (1234567890 → 1112223333) ===")
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)
print()
# Шукаємо конкретний номер
print("=== Шукаємо у John номер 5555555555 ===")
found_phone = john.find_phone("5555555555")
if found_phone:
	print(f"Знайдено: {found_phone.value}")
else:
	print("Номер не знайдено.")
print()
# Видаляємо телефон у John
print("=== Видаляємо у John номер 5555555555 ===")
try:
	john.remove_phone("5555555555")
	print("Номер успішно видалено.")
except ValueError as e:
	print(e)
print(john)
print()
# Спробуємо видалити неіснуючий номер
print("=== Спроба видалити неіснуючий номер 0000000000 ===")
try:
	john.remove_phone("0000000000")
except ValueError as e:
	print("Помилка:", e)
print()
# Видаляємо контакт Jane
print("=== Видаляємо контакт Jane ===")
book.delete("Jane")
print(book)
print()
# Перевіряємо, що John залишився
print("=== Перевіряємо залишок у книзі ===")
print(book)
