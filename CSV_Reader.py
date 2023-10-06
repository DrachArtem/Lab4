import matplotlib
matplotlib.use('TkAgg')  # Змінюємо бекенд на TkAgg
import pandas as pd
import matplotlib.pyplot as plt

# Функція для розрахунку віку на основі дати народження
def calculate_age(birthdate):
    current_year = pd.Timestamp.now().year
    birth_year = pd.to_datetime(birthdate).year
    return current_year - birth_year

try:
    # Зчитуємо дані з CSV-файлу
    df = pd.read_csv('employees.csv')

    # Розраховуємо вік для кожного співробітника та додаємо цей стовпчик до датафрейму
    df['Вік'] = df['Дата народження'].apply(calculate_age)

    # Рахуємо кількість співробітників чоловічої та жіночої статі
    gender_counts = df['Стать'].value_counts()

    # Рахуємо кількість співробітників в кожній віковій категорії
    age_bins = [0, 18, 45, 70, 150]  # Вікові категорії
    age_labels = ['0-17', '18-45', '46-70', '71+']  # Підписи для категорій
    df['Вікова категорія'] = pd.cut(df['Вік'], bins=age_bins, labels=age_labels)
    age_category_counts = df['Вікова категорія'].value_counts().reindex(age_labels, fill_value=0)

    # Рахуємо кількість співробітників жіночої та чоловічої статі в кожній віковій категорії
    gender_age_counts = df.groupby(['Стать', 'Вікова категорія']).size().unstack().reindex(columns=age_labels, fill_value=0)

    # Виводимо результати в консоль
    print("Кількість співробітників чоловічої та жіночої статі:")
    print(gender_counts)
    print("\nКількість співробітників в кожній віковій категорії:")
    print(age_category_counts)
    print("\nКількість співробітників жіночої та чоловічої статі в кожній віковій категорії:")
    print(gender_age_counts)

    # Будуємо діаграми
    plt.figure(figsize=(12, 5))

    plt.subplot(131)
    gender_counts.plot(kind='bar', rot=0)
    plt.title('Кількість співробітників за статтю')

    plt.subplot(132)
    age_category_counts.plot(kind='bar', rot=0)
    plt.title('Кількість співробітників за віком')

    plt.subplot(133)
    gender_age_counts.plot(kind='bar', rot=0)
    plt.title('Кількість співробітників за статтю та віком')

    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Помилка: CSV-файл не знайдено.")
except Exception as e:
    print(f"Помилка: {e}")
