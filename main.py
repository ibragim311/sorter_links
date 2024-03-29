def read_links(file):
    with open(file + ".txt", "r", encoding="utf-8") as f:
        return f.read().split("\n")


def add_links():

    links1 = read_links("Ссылки1")  # список ссылок 1
    links2 = read_links("Ссылки2")  # список ссылок 2

    # очистка файла "Совпадающие ссылки.txt"
    matching_links_file = open("Совпадающие ссылки.txt", "w", encoding="utf-8")
    matching_links_file.write("")
    matching_links_file.close()

    # очистка файла "Несовпадающие ссылки.txt"
    not_matching_links_file = open("Несовпадающие ссылки.txt", "w", encoding="utf-8")
    not_matching_links_file.write("")
    not_matching_links_file.close()

    # открытие для записи "Совпадающие ссылки.txt" и "Несовпадающие ссылки.txt"
    matching_links_file = open("Совпадающие ссылки.txt", "a", encoding="utf-8")
    not_matching_links_file = open("Несовпадающие ссылки.txt", "a", encoding="utf-8")

    for link in links1:
        if link in links2 or link.replace("!", "") in links2:
            matching_links_file.write(link + "\n")
            del links2[links2.index(link.replace("!", ""))]
        else:
            not_matching_links_file.write(link + "\n")

    for link in links2:
        if link not in links1 and link.replace("!", "") not in links1:
            not_matching_links_file.write(link + "\n")

    matching_links_file.close()
    not_matching_links_file.close()


add_links()
