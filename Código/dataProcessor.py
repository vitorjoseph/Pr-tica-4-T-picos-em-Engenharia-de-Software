import json

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")

def avgAgeCountry(data, transformation_func=None):
    country_age_sum = {}
    country_count = {}
    
    for record in data:
        country = record.get("country")
        age = record.get("age")

        if country and age is not None:
            if transformation_func:
                age = transformation_func(age)
            
            if country in country_age_sum:
                country_age_sum[country] += age
                country_count[country] += 1
            else:
                country_age_sum[country] = age
                country_count[country] = 1

    avg_age_by_country = {country: country_age_sum[country] / country_count[country] for country in country_age_sum}
    
    return avg_age_by_country


def avgAgeCountry(data, transform_func=None):
    if not data:
        return {}

    country_age_sum = {}
    country_count = {}

    for entry in data:
        if 'age' in entry and 'country' in entry:
            age = entry['age']
            country = entry['country']

            # Aplicar a função de transformação, se fornecida
            if transform_func:
                age = transform_func(age)

            if country in country_age_sum:
                country_age_sum[country] += age
                country_count[country] += 1
            else:
                country_age_sum[country] = age
                country_count[country] = 1

    avg_age_country = {}
    for country, age_sum in country_age_sum.items():
        avg_age_country[country] = age_sum / country_count[country]

    return avg_age_country
