from pyscript import document, display

# Elements
# Dictionary with information about Elements
# Element Name: symbol, atomic number, atomic weight

# nonmetals from google search

nonmetals = {
    "Hydrogen" : ("H", 1, 1.0078),
    "Helium" : ("He", 2, 4.0026),
    "Carbon" : ("C", 6, 12.011),
    "Nitrogen" : ("N", 7, 14.007),
    "Oxygen" : ("O", 8, 15.999),
    "Fluorine" : ("F", 9, 18.998),
    "Neon" : ("Ne", 10, 20.180),
    "Phosphorus" : ("P", 15, 30.974),
    "Sulfur" : ("S", 16, 32.065),
    "Chlorine" : ("Cl", 17, 35.453),
    "Argon" : ("Ar", 18, 39.948),
    "Selenium" : ("Se", 34, 78.960),
    "Bromine" : ("Br", 35, 79.904),
    "Krypton" : ("Kr", 36, 83.798),
    "Iodine" : ("I", 53, 126.90),
    "Xenon" : ("Xe", 54, 131.29),
    "Radon" : ("Rn", 86, 222),
}

# Function in searching for an element

def search_element(e):
    # Get the input from HTML
    elementinput = document.getElementById("elementinput").value
    # Retrieve information from the dictionary
    result = nonmetals.get(elementinput, ("Element not found", "-", "-"))
    # Display of result
    document.getElementById("name").innerText = elementinput
    document.getElementById("symbol").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("weight").innerText = result[2]