import json
import csv


with open('city.list.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 1. Определить кол-во городов в файле.

    print('Количество городов: ',len(data))

# 2. Создать словарь, где ключ - это код страны, а значение - количество городов.

country_counts = {}

for city in data:
    country = city["country"]
    if country in country_counts:
        country_counts[country] += 1
    else:
        country_counts[country] = 1

print(country_counts)

# 3. Подсчитать кол-во городов в северном полушарии и южном.

count_north = 0
count_south = 0
for city in data:
    semisphere = city["coord"]["lat"]
    if semisphere > 0:
        count_north += 1
    else:
        count_south += 1
print("Кол-во городов в северном полушарии: ", count_north)
print("Кол-во городов в южном полушарии: ", count_south)

# 4. Перевести в CSV файл данные по городам (координаты представить в виде строки значений через запятую).

with open("city.list.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(['id', 'name', 'country', 'coord'])

    for city in data:
        city_id = city["id"]
        name = city["name"]
        country = city["country"]
        lat = city["coord"]["lat"]
        lon = city["coord"]["lon"]
        coord = lat, lon
        writer.writerow([city_id, name, country, coord])

# 5. Создать другой JSON файл, в который сохранить только города одной выбранной страны.

    select_country = "RU"

    filter_cities = []

    for city in data:
        if city["country"] == select_country:
            filter_cities.append(city)


with open("new.city.list.json", "w", encoding="utf-8") as file:
        json.dump(filter_cities, file, ensure_ascii=False, indent=4)

# 6. Для каждой страны создать свой файл JSON с данными городов. Лучше создать отдельную папку в PyCharm, и
# указать путь к новому файлу с этой папкой.

geo_ua = "UA"
filtered_ua_cities = []
for city in data:
    if city["country"] == geo_ua:
        filtered_ua_cities.append(city)

filtered_ua_cities = filtered_ua_cities[:100]

geojson = {
    "type": "FeatureCollection",
    "features": []
}

for city in filtered_ua_cities:
    feature = {
        "type": "Feature",
        "id": city["id"],
        "geometry": {
            "type": "Point",
            "coordinates": [city["coord"]["lon"], city["coord"]["lat"]]
        },
        "properties": {
            "iconCaption": city["name"],
            "market-color": "b51eff"
        }
    }
    geojson["features"].append(feature)

    with open("cities.geojson", "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=4)