words = raw_input("You're deciding which animals get to go on Noah's Ark, so gimme some animals! (Please separate them with commas and spaces) Alternatively, if you'd prefer to input an example list, you can say 'example': ")
if words.lower() == "example":
	animals = ["Turtle", "Kangaroo", "Playtypus", "Killer Whale", "Unicorn", "Mermaid", "Kinkajou", "Dragon", "Koala", "Centaur", "Komodo Dragon", "Hummingbird", "Kookaburra", "King Kong"]
else:
	animals = words.split(", ") # Is there a way to say ", " OR ","?

def k_animals(animals):
    k_list = []
    for i in animals:
        if (i[0] == "k") or (i[0] == "K"):
        	k_list.append(i)
    return k_list

k_animal_names = k_animals(animals)

if k_animal_names == []:
	print "Fun Fact! None of those animals started with the letter K!"
else:
	k_animals_string = ", ".join(k_animal_names)
	# animals_string = ", ".join(animals)
	print "Fun Fact! Out of those animals, the ones that start with the letter K include: {}".format(k_animals_string)