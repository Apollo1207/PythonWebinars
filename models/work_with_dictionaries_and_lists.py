if __name__ == "__main__":
    dict_1 = {"first": 2, (23,): "second", 2: 23, frozenset([23, 45]): "value"}
    dict_2 = dict(first=2, second="second", third=23, forth="value")
    dict_3 = dict([("first", 2), ((23,), "second")])
    dict_4 = dict({"first": 2, (23,): "second", 2: 23, frozenset([23, 45]): "value"})
    dict_5 = {}
    dict = dict()
    print(dict_1)
    print(dict_2)
    print("Element by key first" + str(dict_1["first"]))
    print("Element by key first" + str(dict_1.get("nine")))

    print("Element by key first default value" + str(dict_1.get("nine", 2345)))

    dict_1["nine"] = 2500
    print(dict_1.keys())
    print(dict_1.values())

    # dict_1.pop("first")
    # del dict_1[2]
    # dict_1.clear()

    dict_6 = {"first": 3456, "second": 1, "third": 23.2}
    dict_1.update(dict_6)
    print(dict_1)

    for x in iter(dict_1.keys()):
        print(x)

    valueble_dict = {x: x * x for x in range(10)}
    print(valueble_dict)

    string_1 = "hello"
    list_1 = "-".join(string_1)
    print(list_1)

    string_2 = "hello dear friend lets go to the university"
    print(string_2.center(50, "-"))

    print("     hello       ".lstrip() + "hi")
    print("     hello       ".rstrip() + "hi")
    print("     hello       ".strip() + "hi")

    print(string_2.zfill(150))
