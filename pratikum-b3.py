print('praktikum-3\n\n')
print('Nama Lengkap : PAULUS JEMIANUS OME')
print('NIM          : 231031063')
print('Prodi        : Sistem Informasi B')


####################################################
print()
a =  True
b = False

print('\n===================NAND===================')
hasil = not(a and a)
print(a, 'nand', a, 'adalah =',hasil)
hasil = not(a and b)
print(a, 'nand', b, 'adalah =',hasil)
hasil = not(b and a)
print(b, 'nand', a, 'adalah =',hasil)
hasil = not(b and b)
print(b, 'nand', b, 'adalah =',hasil)

print('\n===================NOR===================')
hasil = not(a or a)
print(a, 'nor', a, 'adalah =',hasil)
hasil = not(a or b)
print(a, 'nor', b, 'adalah =',hasil)
hasil = not(b or a)
print(b, 'nor', a, 'adalah =',hasil)
hasil = not(b or b)
print(b, 'nor', b, 'adalah =',hasil)

print('\n===================NXOR===================')
hasil = not(a ^ a)
print(a, 'nxor', a, 'adalah =',hasil)
hasil = not(a ^ b)
print(a, 'nxor', b, 'adalah =',hasil)
hasil = not(b ^ a)
print(b, 'nxor', a, 'adalah =',hasil)
hasil = not(b ^ b)
print(b, 'nxor', b, 'adalah =',hasil)


# INI OPERATOR MEMBERSHIP
print('\n=================== IN ===================')
nama = 'Paulus Jemianus Ome'

test = 'Je' #ISI dengan 2 huruf ada di nama
cek  = test in nama
print(test, 'ada didalam nama', nama, 'adalah =', cek)

test = 'eJ' #ISI dengan 2 huruf ada di nama
cek  = test in nama
print(test, 'ada didalam ', nama, 'adalah =', cek)

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

print()
cek  = test1 in nama
print(test1,'ada di', nama, 'adalah=', cek)

cek  = test2 in nama
print(test2,'ada di', nama, 'adalah=', cek)

cek  = test3 in nama
print(test3,'ada di', nama, 'adalah=', cek)

cek  = test4 in nama
print(test4,'ada di', nama, 'adalah=', cek)

cek  = test5 in nama
print(test5,'ada di', nama, 'adalah=', cek)

# TUGAS Lanjutkan kode
# dengan cara yang sama buat operator not in
print()

cek  = not(test1 in nama)
print(test1,'tidak ada di', nama, 'adalah=', cek)

cek  = not(test2 in nama)
print(test2,'tidak ada di', nama, 'adalah=', cek)

cek  = not(test3 in nama)
print(test3,'tidak ada di', nama, 'adalah=', cek)

cek  = not(test4 in nama)
print(test4,'tidak ada di', nama, 'adalah=', cek)

cek  = not(test5 in nama)
print(test5,'tidak ada di', nama, 'adalah=', cek)

# INI Operator BITWISE
print('\n')
a = 25 #Tanggal lahir
b = 7 #Bulan Lahir
a += 60
b += 80
print('=========AND===========')
print('NIlai', a, 'biner adalah      =', format(a,'09b'))
print('NIlai', b, 'biner adalah      =', format(b,'09b'))
print('-----------------------------------------AND')
c = a & b
print('Nilai', a, '&', b, 'biner adalah =', format(c, '09b'))

##############################################
# Tugas buat untuk OR
print('\n=========OR===========')
print('NIlai', a, 'biner adalah      =', format(a,'09b'))
print('NIlai', b, 'biner adalah      =', format(b,'09b'))
print('-----------------------------------------OR')
c = a | b
print('Nilai', a, '||', b, 'biner adalah =', format(c, '09b'))

# Tugas buat untuk XOR
print('\n=========XOR===========')
print('NIlai', a, 'biner adalah      =', format(a,'09b'))
print('NIlai', b, 'biner adalah      =', format(b,'09b'))
print('-----------------------------------------XOR')
c = a ^ b
print('Nilai', a, 'xor', b, 'biner adalah =', format(c, '09b'))

print('\n=========NOT===========')
c = ~a
print('Nilai', a, 'biner adalah     =', format(a, '09b'))
print('Nilai not',a, 'biner adalah =', format(c, '09b'))

# Tugas Lanjutkan untuk not b
print('\n=========NOT===========')
c = ~b
print('Nilai', b, 'biner adalah     =', format(b, '09b'))
print('Nilai not',b, 'biner adalah =', format(c, '09b'))


print('\n=========Left Shift==========')
c = a << 2
print('Nilai', a, 'biner adalah      =', format(a, '09b'))
print('Nilai',a, '<< 2 biner adalah =', format(c, '09b'))

c = b << 2
print('Nilai', b, 'biner adalah      =', format(a, '09b'))
print('Nilai',b, '<< 2 biner adalah =', format(c, '09b'))

print()
print('\n=========Right Shift==========')
c = a >> 2
print('Nilai', a, 'biner adalah      =', format(a, '09b'))
print('Nilai',a, '>> 2 biner adalah =', format(c, '09b'))

c = b >> 2
print('Nilai', b, 'biner adalah      =', format(a, '09b'))
print('Nilai',b, '>> 2 biner adalah =', format(c, '09b'))


####################################################
print()
print('=======NOT AND===========')
print('NIlai', a, 'biner adalah           =', format(a,'09b'))
print('NIlai', b, 'biner adalah           =', format(b,'09b'))
print('-----------------------------------------NOT AND')
c = ~(a & b)
print('Nilai', a, 'not and', b, 'biner adalah =', format(c, '09b'))

print()
print('=========NOT OR=============')
print('NIlai', a, 'biner adalah            =', format(a,'09b'))
print('NIlai', b, 'biner adalah            =', format(b,'09b'))
print('-----------------------------------------NOT OR')
c = ~(a | b)
print('Nilai', a, 'not and', b, 'biner adalah =', format(c, '09b'))

print()
print('=========NOT XOR=============')
print('NIlai', a, 'biner adalah            =', format(a,'09b'))
print('NIlai', b, 'biner adalah            =', format(b,'09b'))
print('-----------------------------------------NOT XOR')
c = ~(a ^ b)
print('Nilai', a, 'not xor', b, 'biner adalah =', format(c, '09b'))

print()
print('=========NOT << 2=============')
c = ~(a << 2)
print('Nilai', a, 'biner adalah          =', format(a, '09b'))
print('Nilai',a, 'not << 2 biner adalah =', format(c, '09b'))

c = ~(b << 2)
print('Nilai', b, 'biner adalah          =', format(a, '09b'))
print('Nilai',b, 'not << 2 biner adalah =', format(c, '09b'))
# Tugas buat untuk c = ~(a<<2)
# Tugas buat untuk c = ~(b<<2)

print()
print('=========NOT >> 2=============')
c = ~(a >> 2)
print('Nilai', a, 'biner adalah          =', format(a, '09b'))
print('Nilai',a, 'not >> 2 biner adalah =', format(c, '09b'))

c = ~(b >> 2)
print('Nilai', b, 'biner adalah          =', format(a, '09b'))
print('Nilai',b, 'not >> 2 biner adalah =', format(c, '09b'))
# Tugas buat untuk c = ~(a>>2)
# Tugas buat untuk c = ~(b>>2)