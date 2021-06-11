import geoEncoding
import search
import routing
import folium
import webbrowser

print("Welcome to the MAPS APIs Project")
while True:
    try:
        print("Please select what you want to do:\n")
        print("Enter 1: for Getting your location \nEnter 2: for getting a location based on your search \nEnter 3: for Getting direction to a destination \nEnter 0: Exit")

        choice = int(input("Your choice: "))
    except:
        print("Incorrect Input!!!!!!! Please try again\n\n\n")
        continue

    if choice == 0:
        break

    if choice == 1:
        latitude, longitude, city = geoEncoding.geoEncode(choice)
        m = folium.Map(location=[latitude, longitude], zoom_start=15)

        folium.Marker(
            location=[latitude, longitude],
            popup=city, # pop-up label for the marker
            icon=folium.Icon()
        ).add_to(m)

        m.save("map.html")
        webbrowser.open("map.html")

    elif choice == 2:
        latitude, longitude, city = search.searchLocation()
        m = folium.Map(location=[latitude, longitude], zoom_start=15)

        folium.Marker(
            location=[latitude, longitude],
            popup=city, # pop-up label for the marker
            icon=folium.Icon()
        ).add_to(m)

        m.save("map.html")
        webbrowser.open("map.html")

    elif choice == 3:
        print("Enter 1: for Keeping your location as source \nEnter 2: for searching the source")
        dec = int(input("Your choice: "))
        routing.direction(dec)
    
    else:
        print("Selected option not available. Please try again\n\n\n")