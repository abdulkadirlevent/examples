age = int(input('Yaşınız : '))

if age > 99:
    print('Yaşınız kriterlere uygun değildir..')
elif age < 18:
    print('Geçerli bir yaş giriniz.')
elif age >= 18:
    print("Yaşınız kriterlere uygundur.")
else:
    print('Yaşınız kriterlere uygun değildir..')

if age > 17 and age < 100:
    print("Yaşınız kriterlere uygundur.")
else:
    print('Yaşınız kriterlere uygun değildir..')