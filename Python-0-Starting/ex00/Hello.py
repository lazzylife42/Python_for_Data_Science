# Sujet
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Modifications

ft_list[1] = "World"
ft_tuple = ft_tuple[:1] + ("Switzerland",)
ft_set.remove("tutu!")
ft_set.add("Lausanne")
ft_dict["Hello"] = "42Lausanne"

# Résultats
print(ft_list)     # ['Hello', 'World']
print(ft_tuple)    # ('Hello', 'Switzerland')
print(ft_set)      # {'Hello', 'Lausanne'}
print(ft_dict)     # {'Hello': '42Lausanne'}
