# request ratings from users
ratings = input("Enter your ratings separated by spaces: ").split()
ratings = [float(rating) for rating in ratings]
# add up all the ratings and divide by the number
def ratings_calculator(ratings):

    average_rating = sum(ratings) / len(ratings)

    return f"{average_rating:.2f}"

# result
print("Среднее значение оценок:", ratings_calculator(ratings))
