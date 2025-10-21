def get_cats_info(path):
    with open(path, "r") as file:
        text = [el.strip() for el in file.readlines()]
        cats = []
        
        for cat in text:
            splited = cat.split(',')
            cat_obj = {
                "id" : splited[0],
                "name" : splited[1],
                "age" : splited[2]
            }
            cats.append(cat_obj)
        return cats

cats_info = get_cats_info("task2/cats_file.txt")
print(cats_info)
