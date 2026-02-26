# Initial movie dataset
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

# ---- Extra Challenge: Allow user to add movies ----
add_more = int(input("How many movies would you like to add? "))

for i in range(add_more):
    name = input("Enter movie name: ")
    budget = int(input("Enter movie budget: "))
    movies.append((name, budget))

# ---- Calculate average budget ----
total_budget = 0

for movie in movies:
    total_budget += movie[1]

average_budget = total_budget / len(movies)

print("\nAverage Budget: $", average_budget)

# ---- Find movies above average ----
count = 0

print("\nMovies with budgets higher than average:")

for movie in movies:
    if movie[1] > average_budget:
        difference = movie[1] - average_budget
        print(f"{movie[0]} is ${difference:.2f} above the average.")
        count += 1

# ---- Print total count ----
print(f"\nNumber of movies above average budget: {count}")