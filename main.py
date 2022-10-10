#membuat atm sederhana
print('Selamat datang di program atm sedernana')
print('=======================================')
print('Pilih option ')
print('1. Cek saldo ')
print('2. Ambil saldo ')
print('3. Deposit uang ')
print('4 Keluar')

option = int(input('masukan nomor yang anda pilih :'))

if option == 1:
    print('Uang kamu berjumlah Rp.3.000.000')
elif option == 2:
    print(input('Masukan nominal yang ingin di amabil :'))
elif option == 3:
    print(input('Tekan nominal yang ingin di deposit : '))
elif option == 4:
    quit()
else:
    print('masukan angka dengan benar')
 







