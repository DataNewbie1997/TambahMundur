def tambahMundur (x,y):
        try:
            print('Masukan angka 1:',x)
            if x > 359999:
                print('Invalid input!')
            mundur = 0
            while x > 0:
                a = x%10 #INI UNTUK MENCARI DARI ANGKA PALING BELAKANG 
                mundur = (mundur*10) + a # INI HASIL DARI LOOPING SEHINGGA SETELAH ANGKA PALING BELAKANG, MENCARI HURUF SESUDAHNYA
                x = x//10 #INI AGAR MELANJUTKAN KE ANGKA SELANJUTNYA DARI BELAKANG
            # print (mundur)
            if y > 359999:
                print('Invalid input!')
            mundur2 = 0
            print('Masukan angka 2:',y)
            while y > 0:
                b = y%10 #INI UNTUK MENCARI DARI ANGKA PALING BELAKANG
                mundur2 = (mundur2*10) + b # INI HASIL DARI LOOPING SEHINGGA SETELAH ANGKA PALING BELAKANG, MENCARI HURUF SESUDAHNYA# INI HASIL DARI LOOPING SEHINGGA SETELAH ANGKA PALING BELAKANG, MENCARI HURUF SESUDAHNYA
                y = y//10 #INI AGAR MELANJUTKAN KE ANGKA SELANJUTNYA DARI BELAKANG
            # print(mundur2)
            z = mundur+mundur2 # MENAMBAHKAN X DAN Y
            #SAMA SEPERTI X DAN Y
            mundur3 = 0
            while z > 0:
                c = z%10
                mundur3 = (mundur3*10) + c
                z = z//10 
            print('hasil tambah angka mundurnya:',mundur3)
        except ValueError:
            print('Invalid input!')
tambahMundur(24,1)
tambahMundur(4358,754)
tambahMundur(1234,5678)