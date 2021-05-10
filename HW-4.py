# Get the generation for a given year.
def getGeneration(year):
        if 1883 <= year <= 1900:
                return "The Lost Generation"
        elif 1901 <= year <= 1927:
                return "The Greatest Generation"
        elif 1928 <= year <= 1945:
                return "The Silent Generation"
        elif 1946 <= year <= 1964:
                return "Me Generation"
        elif 1965 <= year <= 1980:
                return "Generation X"
        elif 1981 <= year <= 1996:
                return "Generation Y"
        elif 1997 <= year <= 2012:
                return "Generation Z"
        elif 2013 <= year <= 2025:
                return "Generation Alpha"


# Read the birth year from user.
birthYear = int(input("What is your birth year: "))

# Get the generation for user's brith year.
generation = getGeneration(birthYear)

# Print the fetched generation.
print(generation)