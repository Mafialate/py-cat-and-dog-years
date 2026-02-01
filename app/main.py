import math


def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    result = []
    animal_to_human_ratio = 4

    for age in cat_age, dog_age:
        if age < 15:
            result.append(0)
        elif age < 24:
            result.append(1)
        else:
            human_age = math.floor((age - 24) / animal_to_human_ratio) + 2
            result.append(human_age)
            animal_to_human_ratio += 1

    return result
