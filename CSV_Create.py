import pandas as pd
from faker import Faker
import random

# Ініціалізуємо Faker для генерації фіктивних даних
fake = Faker("uk_UA")
ukrainian_male_patronymics = ["Андрійович","Борисович","Васильович","Вікторович","Володимирович","Геннадійович","Григорійович","Давидович","Данилович",
    "Денисович","Євгенович","Захарович","Зеновійович","Ігорович","Іванович","Кирилович","Костянтинович","Леонідович","Максимович","Мар'янович","Марківич",
    "Михайлович","Назарович","Олегович","Олександрович","Олексійович","Остапович","Павлович","Петрович","Романович","Сергійович","Станіславович","Тарасович",
    "Тимофійович","Федорович","Юрійович","Ярославович"]

ukrainian_female_patronymics = ["Андріївна","Борисівна","Василівна","Вікторівна","Володимирівна","Геннадіївна","Григоріївна","Давидівна","Данилівна",
    "Денисівна","Євгенівна","Захарівна","Зеновіївна","Ігорівна","Іванівна","Кирилівна","Костянтинівна","Леонідівна","Максимівна","Мар'янівна","Марківна",
    "Михайлівна","Назарівна","Олегівна","Олександрівна","Олексіївна","Остапівна","Павлівна","Петрівна","Романівна","Сергіївна","Станіславівна","Тарасівна",
    "Тимофіївна","Федорівна","Юріївна", "Ярославівна"]

# Створюємо порожню таблицю
data = {
    'Прізвище': [],
    'Ім’я': [],
    'По батькові': [],
    'Стать': [],
    'Дата народження': [],
    'Посада': [],
    'Місто проживання': [],
    'Адреса проживання': [],
    'Телефон': [],
    'Email': []
}

# Генеруємо 40% жіночих і 60% чоловічих записів
total_records = 2000
female_records = int(total_records * 0.4)
male_records = total_records - female_records

for _ in range(female_records):
    data['Прізвище'].append(fake.last_name_female())
    data['Ім’я'].append(fake.first_name_female())
    data['По батькові'].append(random.choice(ukrainian_female_patronymics))  # Замінено на middle_name_female
    data['Стать'].append('жіноча')
    data['Дата народження'].append(fake.date_of_birth(minimum_age=15, maximum_age=85))
    data['Посада'].append(fake.job())
    data['Місто проживання'].append(fake.city())
    data['Адреса проживання'].append(fake.address())
    data['Телефон'].append(fake.phone_number())
    data['Email'].append(fake.email())

for _ in range(male_records):
    data['Прізвище'].append(fake.last_name_male())
    data['Ім’я'].append(fake.first_name_male())
    data['По батькові'].append(random.choice(ukrainian_male_patronymics))  # Використовуємо теж first_name_male
    data['Стать'].append('чоловіча')
    data['Дата народження'].append(fake.date_of_birth(minimum_age=15, maximum_age=85))
    data['Посада'].append(fake.job())
    data['Місто проживання'].append(fake.city())
    data['Адреса проживання'].append(fake.address())
    data['Телефон'].append(fake.phone_number())
    data['Email'].append(fake.email())

# Створюємо DataFrame зі згенерованими даними
df = pd.DataFrame(data)

# Зберігаємо таблицю в файл CSV
df.to_csv('employees.csv', index=False)
