def print_presents(presents):
        for pres in presents:
            print(f'{pres['id']}. Dovanos {pres['present_title']}{pres['price']}. Kam skirta {pres['for_who']}')

def create_presents(id_counter, presents):
    print("pridedu nauja")
    print("iveskite dovanos pavadinima")
    present_title = input()
    print("iveskite kaina")
    price = float(input())
    print("Iveskite kam")
    for_who = input()
    id_counter +=1
    pres = {'id': id_counter, "present_title": present_title, "price": price, "for_who":for_who}
    presents.append(pres)
    return id_counter

def edit_presents(presents):
    print_presents(presents)
    print('iveskite id iraso, kuri nori redaguoti')
    edit_id = input()
    for pres in presents:
        if edit_id == str(pres['id']):
            print("iveskite dovanos pavadinima")
            pres['present_title'] = input()
            print('Iveskite kaina')
            pres['price'] = float(input())
            print('Iveskite kam skirta')
            pres['for_who'] = input()
            break

def delete_presents(presents):
    print_presents(presents)
    print('Iveskite id dovanos, kuria norite istrint')
    del_id = input()
    for pres in presents:
        if del_id == str(pres['id']):
            print(pres)
            pos = presents.index(pres)
            del presents[pos]
            break

def print_info():
    print("____________________________")
    print("1. Atvaizduoti dovanu sarasa")
    print("2. Itraukti dovanas i sarasa")
    print("3. Koreguoti dovanas")
    print("4. Istrinti dovanas")
    print("5. Iseiti is programos")
    print("_________Pasirinkite:________")