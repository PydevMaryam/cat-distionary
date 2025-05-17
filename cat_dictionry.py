print("Welcome to Mariam's Cat Dictionary! 🐱")

cat_list = []

while True:
    name = input("Enter the cat's name (or type 'exit' to finish): ")
    if name.lower() == "exit":
        break

    description = input(f"Enter a short description for {name}: ")
    rating = input(f"What rating would you give {name} out of 10? ")

    cat = {
        "Name": name,
        "Description": description,
        "Rating": rating
    }

    cat_list.append(cat)
    print(f"{name} has been added to your cat dictionary!")

# Sort cats by rating (high to low)
cat_list.sort(key=lambda cat: int(cat['Rating']), reverse=True)

# Search for a cat by name
search = input("\nDo you want to search for a cat by name? (yes/no): ")
if search.lower() == "yes":
    keyword = input("Enter the cat's name: ")
    found = False
    for cat in cat_list:
        if cat['Name'].lower() == keyword.lower():
            print(f"\nFound it! {cat['Name']} — {cat['Description']} (Rating: {cat['Rating']}/10)")
            found = True
            break
    if not found:
        print("Sorry, no cat found with that name.")

# Show final cat dictionary
print("\n— Final Cat Dictionary (Sorted by Rating) —")
for cat in cat_list:
    print(f"{cat['Name']} — {cat['Description']} (Rating: {cat['Rating']}/10)")

# Calculate average rating
total = sum(int(cat['Rating']) for cat in cat_list)
average = total / len(cat_list)
print(f"\nAverage Rating of All Cats: {round(average, 2)}/10")

# Save to file
with open("my_cat_dictionary.txt", "w") as file:
    file.write("Mariam's Cat Dictionary 🐱\n\n")
    for cat in cat_list:
        file.write(f"{cat['Name']} — {cat['Description']} (Rating: {cat['Rating']}/10)\n")
    file.write(f"\nAverage Rating: {round(average, 2)}/10")