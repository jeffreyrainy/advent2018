def main():
    file = open("inputs/input14.txt")

    value = file.readline().strip()
    length = len(value)
    recipes = "37"

    elves = [0,1]

    while True:
        sum = int(recipes[elves[0]]) + int(recipes[elves[1]])

        recipes += str(sum)

        elves[0] = (elves[0] + int(recipes[elves[0]]) + 1) % len(recipes)
        elves[1] = (elves[1] + int(recipes[elves[1]]) + 1) % len(recipes)

        if value in recipes[-length - 2:]:
            print(recipes.find(value))
            return

main()