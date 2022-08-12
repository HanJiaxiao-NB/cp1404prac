COLOUR_CODES = {"AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                "Aquamarine1": "#7fffd4", "Aquamarine2": "#76eec6",
                "Army Green":"#4b5320","Arylide Yellow":"e9d66b",
                "Azure2": "#e0eeee", "Azure3": "#c1cdcd",
                "Bistre": "#3d2b1f", "Bisque1": "#ffe4c4"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name,
                                             COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")