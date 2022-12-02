cook_book = {}

with open('recipes.txt', 'r', encoding='utf-8') as f:
  for line in f:
    dish_name = (line.strip('\n'))
    ing_number = int(f.readline())
    ingredients = []
    for i in range(ing_number):
      ingr = f.readline().strip().split(' | ')
     #print(ingr)
      ingredient_name, quantity, measure = ingr
      ingredients.append({'ingredient_name': ingredient_name,
                          'quantity': quantity,
                          'measure': measure
      })

    f.readline()
    cook_book.update({dish_name : ingredients})

print(cook_book)
print()

dishes = []
for k in cook_book:
  dishes.append(k)
# print(dishes)
print()

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for i in dishes:  
    ingr = cook_book.get(i)
    for item in ingr:
      shop_list.update({item.get('ingredient_name') : {'measure': item.get('measure'),
                                                      'quantity': int(item.get('quantity')) * person_count
      }})  
  return(shop_list)

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
    