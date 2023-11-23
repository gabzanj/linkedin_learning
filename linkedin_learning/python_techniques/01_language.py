from string import Template

def string_and_byte():
    """
    String é uma sequência de valores unicode
    Cada caractere da string é representado por um ponteiro de código
    Bytes: valores de 8 bits
    """
    byte_value = bytes([0x41, 0x42, 0x43, 0x44])
    print(byte_value)

    string_value = "This is a string"
    print(string_value)

    # TODO: join/concatenate byte and string
    print(string_value + ' ' + byte_value.decode('utf-8'))
    print(string_value.encode('utf-32') + byte_value)


def string_template():
    phrase = "Bananas are {0} and {1}.".format(
        "yellow", "delicious")
    print(phrase)

    template = Template("I'm ${verb} how to use string.Template.")
    phrase_2 = template.substitute(
        verb="learning"
    )
    print(phrase_2)

    datas = {"verb": "learning"}
    phrase_3 = template.substitute(datas)
    print(phrase_3)

def main():
    string_and_byte()
    string_template()


if __name__ == '__main__':
    main()
