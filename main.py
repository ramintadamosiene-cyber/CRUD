presents = [
    {'id': 1,
     'present_title': "Imbieriniai sausainiai",
     'price': ' 8.0',
     'for_who': "draugei"
     },
    {'id': 2,
     'present_title': "Salikas",
     'price': ' 30.0',
     'for_who': "broliui"
    },
    {'id': 3,
     'present_title': "Zalgirio bilietai",
     'price': ' 100.0',
     'for_who': "vyrui"
     }
]
id_counter = 3
while True:
    print("____________________________")
    print("1. Atvaizduoti dovanu sarasa")
    print("2. Itraukti dovanas i sarasa")
    print("3. Koreguoti dovanas")
    print("4. Istrinti dovanas")
    print("5. Iseiti is programos")
    print("_________Pasirinkite:________")
    option = input()
    match option:
        case "1":
            print("yeeeey, dovanos")
            for pres in presents:
                print(f'{pres['id']}. Dovanos {pres['present_title']}{pres['price']}. Kam skirta {pres['for_who']}')
        case "2":
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
        case '3':
            for pres in presents:
                print(f'{pres['id']}. Dovanos {pres["present_title"]}{pres['price']}. Kam skirta {pres['for_who']}')
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
        case '4':
            for pres in presents:
                print(f'{pres['id']}. Dovanos {pres['present_title']}{pres['price']}. Kam skirta {pres['for_who']}')
            print('Iveskite id dovanos, kuria norite istrint')
            del_id = input()
            for pres in presents:
                if del_id == str(pres['id']):
                    print(pres)
                    pos = presents.index(pres)
                    del presents[pos]
                    break
        case '5':
            break