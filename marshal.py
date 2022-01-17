#!/usr/bin/python1.7
#coding=utf-8
impor marshal,os,sys,time

os.system("hapus")
aleju = ("""
     ╔╦╗┌─┐┬─┐┌─┐┬ ┬┌─┐┬
     ║║║├─┤├┬┘└─┐├─┤├─┤│.
     ╩ ╩┴ ┴┴└─└─┘┴ ┴┴ ┴┴─┘
     Pencipta : Firzzz
     Instagram : putxv_xd\n""")
def aleeju():
        mencoba:
                cetak (aleju)
                print (' [-] Contoh > /sdcard/file.py')
                file = input (' [-] File Kamu : ')
                fileopen = buka(file).read()
                a = kompilasi (buka file, 'dg', 'exec')
                m = marshal.dumps(a)
                s = repr(m)
                b = ('import marshal\nexec(marshal.loads(' + s +'))')
                c = file.replace('.py', '.py')
                d = buka(c, 'w')
                d.menulis(b)
                d.tutup()
                print (' [-] Berhasil > ',c)
                waktu.tidur(1)
                aq = input (' [-] Ingin mengenkripsi lagi? [Y/T]')
                jika aq ="":
                        print ('Perintah tidak ditemukan!')
                        os.sys.keluar()
                elif aq ="y" atau aq ="Y":
                        aleeju()
                kalau tidak:
                        jika aq ="n" atau aq ="N":
                                print (' > Terima kasih anjeng ;v\n')
                        kalau tidak:
                                print ('Perintah tidak ditemukan!')
                                os.sys.keluar()
        kecuali IOError:
                print (' File Tidak Ditemukan ! ')
                waktu.tidur(1)
                aleeju()

jika __name__=='__main__':
        aleeju()