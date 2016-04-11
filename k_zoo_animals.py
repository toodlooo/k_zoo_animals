animals = ["Turtle", "Kangaroo", "Playtypus", "Killer Whale", "Unicorn", "Mermaid", "Kinkajou", "Dragon", "Koala", "Centaur", "Komodo Dragon", "Hummingbird", "Kookaburra", "King Kong"]

def k_animals(animals):
    k_list = []
    for i in animals:
        if (i[0] == "k") or (i[0] == "K"):
        	k_list.append(i)
    return k_list

k_animal_names = k_animals(animals)

print k_animal_names