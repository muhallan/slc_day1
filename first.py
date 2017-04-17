## make breakfast

def get_meal_type ():
    meal = input ("enter the meal u want cooked\n")
    print ("you want to cook", meal)
    print ("---------------")
    return meal

def get_ingredients ():
    print ("\n\nenter 3 ingredients to use\n")
    ingredients = [] 
    maxLengthList = 3
    while len(ingredients) < maxLengthList:
        item = input("Enter an Item to the List: ")
        ingredients.append(item)
        print (ingredients)
    return ingredients

def make_breakfast (meal_to_cook, ingredients):
    print ("\n\n this is how " + meal_to_cook + " is prepared\n")
    print ('get the ingredients {}: '.format(', '.join (ingredients)))
    print ('pour into the heated pan')
    print ('flip to the other side')
    print ('check if the ' + meal_to_cook + ' is ready')
    return ('Yummy ' + meal_to_cook)


def main():
    make_breakfast(get_meal_type(), get_ingredients())

if __name__ == '__main__':
    main()