def flames(person1, person2):
    pair = person1 + person2
    p1Score = 0
    p2Score = 0
    flames = ["Friendship", "Love", "Affection", "Marriage", "Enemies", "Siblings"]

    for i in range(len(pair)):
        if i % 2 == 0:
            p1Score += 1
        else:
            p2Score += 1

    flame = flames[(p1Score - p2Score) % len(flames)]

    return flame

person1 = input()
person2 = input()

result = flames(person1, person2)
print(f"The flame between {person1} and {person2} is {result}.")