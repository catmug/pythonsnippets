def for_each():
    """
    #python #foreach #for
    Example of looping through a list
    foo = ["foo", "bar", "foobar"]
    for x in foo:
        print(x)
    :return:
    """
    languages = ["estonian", "english", "russian"]
    for language in languages:
        print(language)


def for_with_index():
    """
    #python #for #index
    :return:
    """
    cars = ["elantra", "passat"]
    for i, car in enumerate(cars, start=1):
        print(i, car)
