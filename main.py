"""
Returneaza true daca n este prim si false daca nu
n - nr. natural
returneaza True daca nr. este prim sau False daca numarul nu este prim
"""


def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
    return True


assert is_prime(1) is False
assert is_prime(2) is True
assert is_prime(3) is True
assert is_prime(4) is False


def get_largest_prime_below(n):
    """
    Returneaza cel mai mare numar prim, mai mic decat parametrul n, sau False daca nu s-a gasit numarul cerut
    :param n: numar natural
    """
    while n - 1 > 0:
        if is_prime(n - 1):
            return n - 1
        n = n - 1
    return False


def test_get_largest_prime_below():
    assert get_largest_prime_below(20) == 19
    assert get_largest_prime_below(19) == 17
    assert get_largest_prime_below(2) is False
    assert get_largest_prime_below(1) is False


def get_age_in_days(birthday, today):
    """
    Returneaza varsta in zile a persoane a carei data a nasterii a fost introdusa
    :param birthday: Lista ce contine data nasterii, de forma DD/MM/YYYY
    :param today: Lista ce contine data din prezent, de forma DD/MM/YYYY
    :return: un numar natural (ds)
    """
    # ziua, luna si anul nasterii
    bd = int(birthday[0:2])
    bm = int(birthday[3:5])
    by = int(birthday[6:10])

    # ziua, luna si anul din prezent
    td = int(today[0:2])
    tm = int(today[3:5])
    ty = int(today[6:10])
    ds = 0
    month = [31, 29, 30, 31, 30, 31, 30, 31, 30, 31, 30, 31]

    # adaugam zilele trecute din anul curent
    ds = ds + td
    for i in range(0, tm):
        ds = ds + month[i]

    # adaugam zilele trecute din anul nasterii
    ds = ds + (month[bm] - bd)
    for i in range(bm + 1, 12):
        ds = ds + month[i]

    # adaugam zilele din anii ramasi
    for i in range(by + 1, ty):
        if i % 4 == 0:
            ds += 366
        else:
            ds += 365
    return ds


def test_get_age_in_days():
    assert get_age_in_days("16/01/2003", "05/10/2021") == 6837


# problema 6 din lab2
def is_antipalindrome(n) -> bool:
    """
    Functia determina daca un numar sau un cuvant este antipalindrom sau nu
    Metoda: verificarea elemtelor simetrice din lista, in functie de mijlocul listei
    :param n: variabila de tip string ce poate contine un cuvant sau un numar
    :return: True daca elementul este palindrom, False daca nu este palindrom
    """
    l = len(n) // 2
    for i in range(0, l):
        if len(n) % 2 == 1:
            if n[i] == n[-i + 1]:
                return False
        elif n[i] == n[-i]:
            return False
    return True


def test_is_antipalindrome():
 #   assert is_antipalindrome("mara") is False
 #   assert is_antipalindrome("hannah") is True
    assert is_antipalindrome("12321") is True
    assert is_antipalindrome("123322") is False
    assert is_antipalindrome(("6")) is True


def main():
    shouldRun = True
    while shouldRun:
        print("Alegeti optiunea 1, 2 sau 3 in functie de exercitiul ales"
              " sau x daca doriti sa iesiti")
        optiune = input("Scrieti optiunea: ")
        if optiune == "x":
            shouldRun = False
        if optiune == "1":
            test_get_largest_prime_below()
            n = int(input("Scrieti numarul :"))
            print("Rezultat: ",get_largest_prime_below(n))
        if optiune == "2":
            test_get_age_in_days()
            birthday = input("Introduceti data nasterii, in formatul DD/MM/YYYY : ")
            today = input("Introduceti data curenta, in formatul DD/MM/YYYY : ")
            print("Rezultat: ",get_age_in_days(birthday, today))
        if optiune == "3":
            test_is_antipalindrome()
            n = input("introduceeti numarul sau cuvantul: ")
            print("Rezultat: ", is_antipalindrome(n))


main()



#done