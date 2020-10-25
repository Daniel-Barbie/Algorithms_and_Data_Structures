class RomanConverter:
    # NO DICTIONARY, because dictionaries are not ordered (the order is simply not guaranteed!)! use a list with tuples instead: [("M", 1000), ("CM", 900)...]
    # -> then we can sort it also by value
    # the code depends on the order to run properly!
    # sort list with tuples:
    # my_list.sort(key=lambda x: x[1])
    # or, slightly faster:
    # import operator
    # my_list.sort(key=operator.itemgetter(1))
    roman_numerals = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    def convert_to_roman(self, number):
        roman_output = []
        for k, v in RomanConverter.roman_numerals.items():
            roman_output.append((number // v) * k)
            number = number % v
            if number == 0:
                break
        return "".join(roman_output)

    def convert_to_integer(self, roman_number):
        integer_output = 0
        i = 0
        j = 1
        while i < len(roman_number):
            if j < len(roman_number):
                int_number_pos_1 = RomanConverter.roman_numerals[roman_number[i]]
                int_number_pos_2 = RomanConverter.roman_numerals[roman_number[j]]
                if int_number_pos_1 < int_number_pos_2:
                    integer_output += RomanConverter.roman_numerals[roman_number[i] + roman_number[j]]
                    i += 2
                    j += 2
                else:
                    integer_output += RomanConverter.roman_numerals[roman_number[i]]
                    i += 1
                    j += 1
            else:
                integer_output += RomanConverter.roman_numerals[roman_number[i]]
                i += 1
                j += 1
        return integer_output


rc = RomanConverter()
print(rc.convert_to_roman(114))
print(rc.convert_to_integer("MXIV"))
print(rc.convert_to_integer("MCXV"))
