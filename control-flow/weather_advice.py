weather_conditions = input(f"What's the weather like today? (sunny/rainy/cold): ")

if weather_conditions == "sunny":
    print(f" Wear a t-shirt and sunglasses.")
elif weather_conditions == "rainy":
    print(f" Don't forget your umbrella and a raincoat.")
elif weather_conditions == "cold":
    print(f"Make sure to wear a warm coat and a scarf.")
else:
    print(f"Sorry, I don't have recommendations for this weather.")

