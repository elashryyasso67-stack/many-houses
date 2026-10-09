# The demo properties. A property's name is its ID, so every name must be different.
PROPERTIES = [
    {
        "name": "Luxury Apartment",
        "image": "https://picsum.photos/seed/luxury_apartment/800/600",
        "place": "Cairo",
        "rooms": 3,
        "bathrooms": 2,
        "price": 2500000,
        "area": 150,
        "type": "Apartment",
        "latitude": 30.0444,
        "longitude": 31.2357,
        "image2": "",
        "image3": ""
    },
    {
        "name": "Modern Villa",
        "image": "https://picsum.photos/seed/modern_villa/800/600",
        "place": "Cairo",
        "rooms": 5,
        "bathrooms": 3,
        "price": 6000000,
        "area": 300,
        "type": "Villa",
        "latitude": 30.0561,
        "longitude": 31.2394
    },
    {
        "name": "Penthouse Downtown",
        "image": "https://picsum.photos/seed/penthouse_downtown/800/600",
        "place": "Cairo",
        "rooms": 4,
        "bathrooms": 3,
        "price": 4500000,
        "area": 220,
        "type": "Penthouse",
        "latitude": 30.0450,
        "longitude": 31.2400
    },
    {
        "name": "Beach House",
        "image": "https://picsum.photos/seed/beach_house/800/600",
        "place": "Sharm El Sheikh",
        "rooms": 4,
        "bathrooms": 2,
        "price": 5000000,
        "area": 200,
        "type": "House",
        "latitude": 27.9158,
        "longitude": 34.3290
    },
    {
        "name": "Sea View Villa",
        "image": "https://picsum.photos/seed/sea_view_villa/800/600",
        "place": "Hurghada",
        "rooms": 5,
        "bathrooms": 4,
        "price": 8500000,
        "area": 350,
        "type": "Villa",
        "latitude": 27.2579,
        "longitude": 33.8116
    },
    {
        "name": "Nile Garden Apartment",
        "image": "https://picsum.photos/seed/nile_garden/800/600",
        "place": "Giza",
        "rooms": 2,
        "bathrooms": 1,
        "price": 1800000,
        "area": 110,
        "type": "Apartment",
        "latitude": 30.0131,
        "longitude": 31.2089
    },
    {
        "name": "Ancient City Apartment",
        "image": "https://picsum.photos/seed/ancient_city/800/600",
        "place": "Luxor",
        "rooms": 3,
        "bathrooms": 2,
        "price": 1200000,
        "area": 130,
        "type": "Apartment",
        "latitude": 25.6872,
        "longitude": 32.6396
    },
    {
        "name": "Red Sea Resort",
        "image": "https://picsum.photos/seed/red_sea_resort/800/600",
        "place": "Marsa Alam",
        "rooms": 3,
        "bathrooms": 2,
        "price": 3500000,
        "area": 180,
        "type": "Villa",
        "latitude": 24.0621,
        "longitude": 34.8953
    },
    {
        "name": "Oasis Villa",
        "image": "https://picsum.photos/seed/oasis_villa/800/600",
        "place": "Siwa",
        "rooms": 4,
        "bathrooms": 3,
        "price": 2800000,
        "area": 250,
        "type": "Villa",
        "latitude": 29.2042,
        "longitude": 25.5199
    },
    {
        "name": "Alexandria Cornish Flat",
        "image": "https://picsum.photos/seed/alex_cornish/800/600",
        "place": "Alexandria",
        "rooms": 2,
        "bathrooms": 1,
        "price": 1500000,
        "area": 95,
        "type": "Apartment",
        "latitude": 31.2001,
        "longitude": 29.9187
    },
    {
        "name": "Aswan Riverside Home",
        "image": "https://picsum.photos/seed/aswan_riverside/800/600",
        "place": "Aswan",
        "rooms": 3,
        "bathrooms": 2,
        "price": 950000,
        "area": 160,
        "type": "House",
        "latitude": 24.0889,
        "longitude": 32.8998
    },
    {
        "name": "City Star Apartment",
        "image": "https://picsum.photos/seed/city_star/800/600",
        "place": "New Administrative Capital",
        "rooms": 3,
        "bathrooms": 2,
        "price": 3200000,
        "area": 170,
        "type": "Apartment",
        "latitude": 30.0390,
        "longitude": 31.4580
    },
]


def find_property(name):
    # Go through the list until the name matches. Return None if nothing matches.
    for item in PROPERTIES:
        if item["name"] == name:
            return item
    return None
