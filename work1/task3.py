country_capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "UK": "London"
}

country = input("Enter a country name: ")
capital = country_capitals.get(country)

if capital:
    print(f"The capital of {country} is {capital}")
else:
    print("Sorry, country not found")