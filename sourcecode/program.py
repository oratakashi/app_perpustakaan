##============================================##
## Program By Kelompok 1                      ##
## Politeknik Negeri Bandung 2017             ##
##============================================##

##============================================##
## Starting System                            ##
##============================================##

print('=========================================')
print('Starting System...')
print('Starting Tkinter Module...')
from tkinter import *
import tkinter.messagebox as mb
import pymysql as db
import sys
print('Starting PyMySql Module...')
print('=========================================')

##============================================##
## Command on Startup ##
##============================================##

def waktu():
    import time
    a=time.localtime()
    hr=a.tm_hour
    mn=a.tm_min
    sc=a.tm_sec
    return ('{}:{}:{}'.format(hr,mn,sc))
def tanggal():
        from datetime import datetime
        sekarang=datetime.now()
        tahun=sekarang.year
        bulan=sekarang.month
        hari=sekarang.day
        return("{}/{}/{}".format(hari, bulan, tahun))



##=============================================================================##
## Background Progress
    
global datUser
global datPassword

abang='#cc0000'

##=============================================================================##
## Mulai Login
##=============================================================================##

def Main():
    root=Tk()
    
    def userpas():
        nmUser = root.entUser.get()
        passUser = root.entPass.get()
        user=("null")
        pswd=("null")
        try:
            cur.execute("SELECT user FROM `admin` WHERE `user` = '"+ nmUser +"'")
            user = cur.fetchall()
            cur.execute("SELECT pswd FROM `admin` WHERE `user` = '"+ nmUser +"'")
            pswd = cur.fetchall()
        except:
            print (waktu()+' - '+"Gagal Membaca User ID")
            if con:    
                con.close()
        ##Menampung User dan Pass
        datUser = user[0][0]
        datPassword = pswd[0][0]

        if nmUser=='':
            root.entUser.focus_set()
        elif passUser=='':
            mb.showwarning('Pesan Salah', 'Kata Kunci tidak boleh kosong!', parent=root)
            root.entPass.focus_set()
        elif (nmUser==datUser) and (passUser==datPassword ):
            mb.showinfo("Login", "Berhasil Login dan Terhubung ke Server..!!", parent=root)
            root.destroy()
            Menuutama(datUser,datPassword,'Program Perpustakaan Terpadu "E-Perpus" v4.0[Stabil]')
            #Tutup()
        else:
            mb.showwarning('Pesan Salah', 'Nama Pengguna atau Kata Kunci SALAH!!', parent=root)
            root.entUser.delete(0, END)
            root.entPass.delete(0, END)
            root.entUser.focus_set()
    
    def Atur(root):
        root.protocol("WM_DELETE_WINDOW", Tutup)

        frameJudul = Frame (root, bg=abang)
        frameJudul.pack(fill=BOTH)
        frameKet = Frame (root)
        frameUtama = Frame(root, bd=10)
        frameKet.pack(fill=BOTH)
        frameUtama.pack(fill=BOTH, expand=YES)

        Label(frameKet, text="Silahkan Masukan Username Anda !!").pack()
        Label(frameJudul, text="User Login", font="Forte 15", fg='white', bg=abang).pack()
        # atur frame data
        
        frData = Frame(frameUtama, bd=5)
        frData.pack(fill=BOTH, expand=YES)
        # atur input username
        Label(frData, text='User:').grid(row=0, column=0, sticky=W)
        root.entUser = Entry(frData,width=30)
        root.entUser.grid(row=0, column=1)
        
        Label(frData, text='Password:').grid(row=1, column=0, sticky=W)
        root.entPass = Entry(frData, show='*',width=30)
        root.entPass.grid(row=1, column=1)

        

     # atur frame tombol
        frTombol = Frame(frameUtama, bd=5)
        frTombol.pack(fill=BOTH, expand=YES)

        btnLogin = Button(frTombol, text='Login', command=userpas)
        btnLogin.pack(side=LEFT, fill=BOTH, expand=YES)
         
        btnBatal = Button(frTombol, text='Batal', command=Tutup)
        btnBatal.pack(side=LEFT, fill=BOTH, expand=YES)
    
    def Tutup():
        root.destroy()
        print(waktu()+' - '+"Disconnecting from Database...")
        print(waktu()+' - '+"Disconnecting from localhost...")
        print(waktu()+' - '+"Stoping Tkinter Module...")
        print(waktu()+' - '+"Stoping Pymysql Module...")
        print(waktu()+' - '+"Menutup Aplikasi...") 
    def Hapus():
        root.entUser.delete(0, END)
        root.entPass.delete(0, END)
        root.entUser.focus_set()
    def init():
        lebar = 250
        tinggi = 180
        setTengahX = (root.winfo_screenwidth()-lebar)//2
        setTengahY = (root.winfo_screenheight()-tinggi)//2
        root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        root.title('User Login')
        root.resizable(False, False)
        Atur(root)
    init()


##=================================================================================================================================##
## Form Tambah User
def tambahuser(datUser,datPassword):
    root=Tk()
    def tutup():
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Menutup Tambah Pengguna...")
    def goleki():
        cari=caris.get()
        if cari == '':
            mb.showerror("Error!!", "Jika ingin Menambah Pengguna\nKolom Nama Pengguna Tidak Boleh Kosong..!!", parent=root)
        else :
            cur.execute("SELECT * FROM `admin` WHERE `user` = '"+ cari +"'")
            global user
            user=cur.fetchall()
            if not user:
                data=(cari, cari)
                query="insert into admin (user,pswd) values"+str(data)
                cur.execute(query)
                con.commit()
                mb.showinfo("Sukses", "Berhasil Menambah Pengguna "+cari+" ke Database..!!", parent=root)
                print(waktu()+' - '+"User ["+datUser+"] Menambah Pengguna Baru "+cari+" ke Database...")
                tutup()
            else:
                mb.showerror("Error!!", "Username "+cari+" sudah digunakan\nSilahkan Ganti Nama Lain..!!", parent=root)
    root.protocol("WM_DELETE_WINDOW", tutup)
    lebar = 430
    tinggi = 130
    setTengahX = (root.winfo_screenwidth()-lebar)//2
    setTengahY = (root.winfo_screenheight()-tinggi)//2
    root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
    root.resizable(False, False)
    ##Local Variabel
    self=root
    ##Seting isi
    f=Frame(root,bg=abang)
    f.pack(fill=BOTH)
    fjudul=Frame(root)
    fjudul.pack(fill=BOTH, side=TOP,expand=YES)
    fisi=Frame(root)
    fisi.pack(fill=BOTH, expand=YES)
    fket=Frame(root)
    fket.pack(fill=BOTH)

    Label(f, text="Tambah Pengguna", font="Forte 15", fg='white', bg=abang).pack()
    
    Label(fjudul,text="Silahkan Masukan Nama Pengguna Baru", font=('Calibri',11)).pack(fill=BOTH, expand=YES)
    Label(fisi, text="Nama Pengguna :").grid(row=0,column=0,sticky=W)
    caris=Entry(fisi,width=40)
    caris.grid(row=0,column=1,sticky=W)
    Label(fket, text="nb*: Kata Sandi Otomatis sama dengan username").pack()
    Button(fisi,width=10,text='Tambah',command=goleki).grid(row=0,column=2,sticky=W)
    
##=================================================================================================================================##
## Form Programer
def programer(datUser):
    root=Tk()
    tgl=str(tanggal())
    jam=str(waktu())

    baris1="Aplikasi Perpustakaan Terpadu ini di Buat Oleh 5 Mahasiswa"
    baris2="\nPoliteknik Negeri Bandung 2017"
    baris3="\n\n1. Abdul Hafiidh S ( Databases Programer )"
    baris4="\n(WA : 085290059281 )"
    baris5="\n2. Anisia Suryani P ( Form Designer )"
    baris6="\n(WA : 085829014381 )"
    baris7="\n3. Aeni Rafika ( Form Designer )"
    baris8="\n(WA : 085225298142 )"
    baris9="\n4. Isnani H ( Form Designer )"
    baris10="\n(WA : 085742764721 )"
    baris11="\n5. Tantowi Jaya ( Form Designer )"
    baris12="\n(WA : 082324688230 )"
    baris13="\n\nGenerated :"
    baris14="\n"+tgl+" , "+jam
    total=baris1+baris2+baris3+baris4+baris5+baris6+baris7+baris8+baris9+baris10+baris11+baris12
    cetak=total+baris13+baris14
    
    def tutup():
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Menutup Contact Person...")
    def simpan():
        tulis=open("ContactPerson.txt", "w")
        
        tulis.write(str(cetak))
        tulis.close
        mb.showinfo("Sukses!!", "File berhasil di simpan dengan nama file 'ContactPerson.txt' di Lokasi Aplikasi Berada..!!")
        tutup()
    def komponen():
        ##Seting Frame
        f=Frame(root,bg=abang)
        f2=Frame(root)
        f3=Frame(root)
        f.pack(fill=BOTH)
        f2.pack(fill=BOTH, expand=YES)
        f3.pack(fill=BOTH, side=BOTTOM)
        ## Isi frame
        Label(f, text="Contact Person", font="Forte 15", fg='white', bg=abang).pack()
        gulung=Scrollbar(f2)
        gulung.pack(fill=Y,side=RIGHT)
        text = Text(f2,yscrollcommand = gulung.set)
        text.insert(INSERT, str(total))
        text.pack(fill=BOTH,expand=YES)

        gulung.config( command = text.yview )
        Button(f3, text="OK", width=15, command=tutup).pack(fill=BOTH,expand=YES,side=LEFT)
        Button(f3, text="Save to Files", width=15, command=simpan).pack(fill=BOTH,expand=YES, side=LEFT)
    def konfigurasi():
        lebar = 700
        tinggi = 450
        setTengahX = (root.winfo_screenwidth()-lebar)//2
        setTengahY = (root.winfo_screenheight()-tinggi)//2
        root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        komponen()
    konfigurasi()
##=================================================================================================================================##
## Form Bantuan
def bantuan(datUser):
    root=Tk()
    tgl=str(tanggal())
    jam=str(waktu())
    baris1="\n\tAplikasi Perpustakaan Terpadu atau E-Perpus ini mempunyai 4 menu utama,\nyaitu File, Kelola Buku, Kelola Anggota, dan Bantuan."
    baris2="\n\n1.   File"
    baris3="\n\tBerfungsi untuk melihat "
    baris4="\n1.1. About Us"
    baris5="\n\tBerisi tentang kami, para pembuat Aplikasi."
    baris51="\n1.2. Tambah Pengguna"
    baris52="\n\tBerfungsi untuk menambah pengguna ke dalam sistem."
    baris53="\n1.4. Ganti Username"
    baris54="\n\tBerfungsi untuk Mengganti Username Pengguna."
    baris6="\n1.5. Ganti Password"
    baris7="\n\tBerfungsi untuk Mengganti Password Pengguna."
    baris8="\n1.6. Log Out"
    baris81="\n\tBerfungsi untuk Mengganti Pengguna."
    baris9="\n\n1.7. Keluar"
    baris10="\n\tUntuk keluar dari aplikasi."
    baris11="\n\n2.   Kelola Buku"
    baris12="\n\tUntuk menambah buku, mengelola daftar buku, dan pencarian buku."
    baris13="\n2.1. Tambah Buku"
    baris14="\n\tMenu Tambah Buku dapat kita klik untuk menambah buku yang ingin dipinjam"
    baris15="\n2.2. Lihat Daftar Buku"
    baris16="\n\tTombol ini berguna untuk melihat daftar buku yang dapat dipinjam"
    baris17="\n2.3. Cari Buku"
    baris18="\n\tBerfungsi untuk mencari buku yang diinginkan dengan langsung memasukkan kata kunci"
    baris19="\n2.4. Lihat Peminjaman Buku"
    baris20="\n\tBerfungsi untuk Melihat daftar buku yang masih di pinjam oleh anggota"
    baris21="\n2.5. Lihat Pengembalian Buku"
    baris22="\n\tBerfungsi untuk Melihat daftar buku yang sudah dikembalikan oleh anggota"
    baris23="\n\n3. Kelola Anggota"
    baris24="\n3.1. Tambah Anggota"
    baris25="\n\tUntuk menambah keanggotaan perpustakaan"
    baris26="\n\tUntuk menambah keanggotaan perpustakaan"
    baris27="\n3.2. Cari Anggota"
    baris28="\n\tMelalui tombol ini, Anda dapat mencari dan melihat sesama anggota perpustakaan"
    baris29="\n\n4.Bantuan"
    baris30="\n4.1. Bantuan"
    baris31="\n\tMenu ini berisi bantuan cara menggunakan aplikasi serta fungsi dari setiap tombol pada aplikasi"
    baris32="\n4.2. Tentang Aplikasi"
    baris33="\n\tBerisi tentang aplikasi"
    baris34="\n\n Generated :"
    baris35="\n"+tgl+" , "+jam
    total=baris1+baris2+baris3+baris4+baris5+baris51+baris52+baris53+baris54+baris6+baris7+baris8+baris81+baris9+baris10+baris11+baris12+baris13+baris14+baris15+baris16+baris17+baris18+baris19+baris20+baris21+baris22+baris23+baris24+baris25+baris26+baris27+baris28+baris29+baris30+baris31+baris32+baris33
    cetak=total+baris34+baris35
    def tutup():
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Menutup Bantuan...")
    def simpan():
        tulis=open("Bantuan.txt", "w")
        
        tulis.write(str(cetak))
        tulis.close
        mb.showinfo("Sukses!!", "File berhasil di simpan dengan nama file 'Bantuan.txt' di Lokasi Aplikasi Berada..!!")
        tutup()
    def komponen():
        ##Seting Frame
        f=Frame(root,bg=abang)
        f2=Frame(root)
        f3=Frame(root)
        f.pack(fill=BOTH)
        f2.pack(fill=BOTH, expand=YES)
        f3.pack(fill=BOTH, side=BOTTOM)
        ## Isi frame
        Label(f, text="Bantuan", font="Forte 15", fg='white', bg=abang).pack()
        gulung=Scrollbar(f2)
        gulung.pack(fill=Y,side=RIGHT)
        text = Text(f2,yscrollcommand = gulung.set)
        text.insert(INSERT, str(total))
        text.pack(fill=BOTH,expand=YES)

        gulung.config( command = text.yview )
        Button(f3, text="OK", width=15, command=tutup).pack(fill=BOTH,expand=YES,side=LEFT)
        Button(f3, text="Save to Files", width=15, command=simpan).pack(fill=BOTH,expand=YES, side=LEFT)
    def konfigurasi():
        lebar = 700
        tinggi = 450
        setTengahX = (root.winfo_screenwidth()-lebar)//2
        setTengahY = (root.winfo_screenheight()-tinggi)//2
        root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        komponen()
    konfigurasi()##memuat konfigurasi

##=================================================================================================================================##
## Lihat Pengembalian

def lihatkembali(datUser):
    root=Tk()
    def tutup():
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Menutup Pengembalian Buku...")
    root.protocol("WM_DELETE_WINDOW", tutup)
    lebar = 1100
    tinggi = 600
    setTengahX = (root.winfo_screenwidth()-lebar)//2
    setTengahY = (root.winfo_screenheight()-tinggi)//2
    root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
    #root.resizable(False, False)
    ##Local Variabel
    self=root
    cur.execute('select * from data_kembalian')
    buku=cur.fetchall()
    ##Seting isi
    f=Frame(root,bg=abang)
    f2=Frame(root)
    f.pack(fill=BOTH)
    f2.pack(fill=BOTH, expand=YES)

    Label(f, text="Daftar Pengembalian Buku", font="Forte 15", fg='white', bg=abang).pack()
    
    tmnoaja=Label(f2,text='No Pengembalian')
    tmno=Label(f2,text='No Pinjaman')
    tmid=Label(f2,text='Kode Buku')
    tmjudul=Label(f2,text='Judul')
    tmnama=Label(f2,text='Nama Peminjam')
    tmjk=Label(f2,text='Jenis Kelamin')
    tmalamat=Label(f2,text='Alamat')
    tmtglpinjam=Label(f2,text='Tgl Pinjam')
    tmlamapinjam=Label(f2,text='Perkiraan Kembali')
    tmtglkembali=Label(f2,text='Tgl Kembali')
    tmdenda=Label(f2,text='Denda')

    tmnoaja.grid(row=0,column=0,sticky=W)
    tmno.grid(row=0,column=1,sticky=W)
    tmid.grid(row=0,column=2,sticky=W)
    tmjudul.grid(row=0,column=3,sticky=W)
    tmnama.grid(row=0,column=4,sticky=W)
    tmjk.grid(row=0,column=5,sticky=W)
    tmalamat.grid(row=0,column=6,sticky=W)
    tmtglpinjam.grid(row=0,column=7,sticky=W)
    tmlamapinjam.grid(row=0,column=8,sticky=W)
    tmtglkembali.grid(row=0,column=9,sticky=W)
    tmdenda.grid(row=0,column=10,sticky=W)

    for i in range(len(buku)):
        for j in range(len(buku[i])):
            teks=Entry(f2)
            teks.grid(row=i+1,column=j)
            teks.insert(END,buku[i][j])
            
##=================================================================================================================================##
## Lihat Pinjaman

def lihatpinjaman(datUser):
    root=Tk()
    def tutup():
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Menutup Peminjaman Buku...")
    root.protocol("WM_DELETE_WINDOW", tutup)
    lebar = 1100
    tinggi = 600
    setTengahX = (root.winfo_screenwidth()-lebar)//2
    setTengahY = (root.winfo_screenheight()-tinggi)//2
    root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
    root.resizable(False, False)
    ##Local Variabel
    self=root
    cur.execute('select * from data_pinjaman')
    buku=cur.fetchall()
    ##Seting isi
    f=Frame(root,bg=abang)
    f2=Frame(root)
    f.pack(fill=BOTH)
    f2.pack(fill=BOTH,expand=YES)
    
    Label(f, text="Daftar Peminjaman Buku", font="Forte 15", fg='white', bg=abang).pack()
    
    tmno=Label(f2,text='No Pinjaman')
    tmid=Label(f2,text='Kode Buku')
    tmjudul=Label(f2,text='Judul')
    tmnama=Label(f2,text='Nama Peminjam')
    tmjk=Label(f2,text='Jenis Kelamin')
    tmalamat=Label(f2,text='Alamat')
    tmtglpinjam=Label(f2,text='Tgl Pinjam')
    tmlamapinjam=Label(f2,text='Lama Pinjam')
    tmtglkembali=Label(f2,text='Perkiraan Kembali')

    tmno.grid(row=0,column=0,sticky=W)
    tmid.grid(row=0,column=1,sticky=W)
    tmjudul.grid(row=0,column=2,sticky=W)
    tmnama.grid(row=0,column=3,sticky=W)
    tmjk.grid(row=0,column=4,sticky=W)
    tmalamat.grid(row=0,column=5,sticky=W)
    tmtglpinjam.grid(row=0,column=6,sticky=W)
    tmlamapinjam.grid(row=0,column=7,sticky=W)
    tmtglkembali.grid(row=0,column=8,sticky=W)

    for i in range(len(buku)):
        for j in range(len(buku[i])):
            teks=Entry(f2)
            teks.grid(row=i+1,column=j)
            teks.insert(END,buku[i][j])
            
##=================================================================================================================================##
## Form Ganti Nama

def gantinama(datPassword,datUser):
    root=Tk()
    def tutup():
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Menutup Ganti Username...")
    
    def komponen():
        def simpan():
            cari=namabaru.get()
            if cari == '':
                mb.showerror("Error!!", "Jika ingin Mengganti Nama Pengguna\nKolom Username baru Tidak Boleh Kosong..!!", parent=root)
            else :
                cur.execute("SELECT * FROM `admin` WHERE `user` = '"+ cari +"'")
                global user
                user=cur.fetchall()
                if not user:
                    tampung=datUser
                    data=(cari)
                    query="update admin set "+"user='"+cari+"'"+","+"pswd='"+datPassword+"' where user="+"'"+datUser+"'"
                    cur.execute(query)
                    con.commit()
                    mb.showinfo("Sukses", "Berhasil Merubah Pengguna "+tampung+" menjadi "+cari+" ke Database..!!", parent=root)
                    mb.showwarning("Warning", "Anda Harus Login Ulang untuk menerapkan Perubahan..!!", parent=root)
                    print(waktu()+' - '+"User ["+datUser+"] Merubah Pengguna "+tampung+" menjadi "+cari+" ke Database...")
                    tutup()
                else:
                    mb.showerror("Error!!", "Username "+cari+" sudah digunakan\nSilahkan Ganti Nama Lain..!!", parent=root)    
        f=Frame(root, bg=abang)
        f2=Frame(root)
        f.pack(fill=BOTH)
        f2.pack(fill=BOTH,expand=YES)

        Label(f, text="Ganti Username", font="Forte 15", fg='white', bg=abang).pack()

        Label(root, text="Login Sebagai : "+datUser).pack()
        Label(root, text="Masukan Username Baru").pack()
        namabaru=Entry(root, width=35,)
        namabaru.pack()
        Label(root, text=" ").pack()
        Button(root, text="Simpan",width=10,command=simpan).pack()
        Button(root, text="Batal",width=10,command=tutup).pack()
        
    def konfigurasi():
        lebar = 300
        tinggi = 180
        setTengahX = (root.winfo_screenwidth()-lebar)//2
        setTengahY = (root.winfo_screenheight()-tinggi)//2
        root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        root.resizable(False, False)
        komponen()
    konfigurasi()

##=================================================================================================================================##
## Form Ganti Password
def gantipas(datPassword,datUser):
    root=Tk()
    def tutup():
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Menutup Ganti Password...")
    
    def komponen():
        def simpan():
            cur.execute("SELECT pswd FROM `admin` WHERE `user` = '"+ datUser +"'")
            pswd = cur.fetchall()
            pas=paslama.get()
            if pas==pswd[0][0] :
                barupas=pasbaru.get()
                pasver=verpas.get()
                if pasver==barupas :
                    data=(barupas)
                    query="update admin set "+"user='"+datUser+"'"+","+"pswd='"+barupas+"' where user="+"'"+datUser+"'"
                    cur.execute(query)
                    con.commit()
                    mb.showinfo('Sukses!!', 'Kata Sandi Berhasil di Ganti!!', parent=root)
                    print(waktu()+' - '+"User ["+datUser+"] Berhasil Ganti Password...")
                    tutup()
                else :
                    mb.showwarning('Warning!!', 'Kata Sandi yang anda masukan tidak sama!!\nSilahkan Cek Kembali!!', parent=root)
            else :
                mb.showwarning('Kata Sandi Salah', 'Kata sandi lama dari user '+datUser+' Salah!!\nSilahkan Cek Kembali!!', parent=root)
        f=Frame(root, bg=abang)
        f2=Frame(root)
        f.pack(fill=BOTH)
        f2.pack(fill=BOTH,expand=YES)

        Label(f, text="Ganti Kata Sandi", font="Forte 15", fg='white', bg=abang).pack()

        Label(root, text="Login Sebagai : "+datUser).pack()
        Label(root, text="Masukan Password Lama").pack()
        paslama=Entry(root, width=35, show="*")
        paslama.pack()
        Label(root, text="Masukan Password Baru").pack()
        pasbaru=Entry(root, width=35, show="*")
        pasbaru.pack()
        Label(root, text="Verifikasi Password Baru").pack()
        verpas=Entry(root, width=35, show="*")
        verpas.pack()
        Label(root, text=" ").pack()
        Button(root, text="Simpan",width=10,command=simpan).pack()
        Button(root, text="Batal",width=10,command=tutup).pack()
        
    def konfigurasi():
        lebar = 300
        tinggi = 260
        setTengahX = (root.winfo_screenwidth()-lebar)//2
        setTengahY = (root.winfo_screenheight()-tinggi)//2
        root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        root.resizable(False, False)
        komponen()
    konfigurasi()


##=================================================================================================================================##
## Form Kembali Buku
def kembalibuku(datUser):
    root=Tk()
    lebar = 450
    tinggi = 370
    setTengahX = (root.winfo_screenwidth()-lebar)//2
    setTengahY = (root.winfo_screenheight()-tinggi)//2
    root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
    root.resizable(False, False)
    cur.execute('select * from data_kembalian')
    ##Local Variabel
    self=root
    left=LEFT

    def tutup():
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Menutup Peminjaman Buku...")

    def simpan():
        smpinjam=pinjamans.get()
        smid=idbukus.get()
        smjudul=juduls.get()
        smnama=namas.get()
        smjk=jk.get()
        if smjk == "cowo" :
            smjk="Laki-Laki"
            smalamat=alamats.get()
            smtglpinjam=tglpinjams.get()
            smtglkmbali=tglkembalis.get()
            smback=tgljoins.get()
            smlong=brplamas.get()
            data=(smpinjam,smid,smjudul,smnama,smjk,smalamat,smtglpinjam,smtglkmbali,smback,smlong)
            query="insert into data_kembalian (no_pinjam, kode_buku, judul, nama, jenis_kelamin, alamat, tgl_pinjam, tgl_kembali, tgl_dikembalikan, denda) values"+str(data)
            cur.execute(query)
            con.commit()
            mb.showinfo("Sukses", "Berhasil Menambah "+smnama+" Mengembalikan Buku "+smjudul+" ke Database..!!", parent=root)
            print(waktu()+' - '+"User ["+datUser+"] Menambah "+smnama+" Mengembalikan Buku "+smjudul+" ke Database...")
            query="delete from data_pinjaman where no = '"+ smpinjam +"'"
            cur.execute(query)
            con.commit()
            tutup()
        elif smjk == "cewe" :
            smjk="Perempuan"
            smalamat=alamats.get()
            smtglpinjam=tglpinjams.get()
            smback=tgljoins.get()
            smlong=brplamas.get()
            data=(smpinjam,smid,smjudul,smnama,smjk,smalamat,smtglpinjam,smback,smlong)
            query="insert into data_kembalian (no_pinjam, kode_buku, judul, nama, jenis_kelamin, alamat, tgl_pinjam, tgl_kembali, denda) values"+str(data)
            cur.execute(query)
            con.commit()
            mb.showinfo("Sukses", "Berhasil Menambah "+smnama+" Mengembalikan Buku "+smjudul+" ke Database..!!", parent=root)
            print(waktu()+' - '+"User ["+datUser+"] Menambah "+smnama+" Mengembalikan Buku "+smjudul+" ke Database...")
            tutup()
        else:
            mb.showwarning("Warning!!", "Jenis Kelamin "+smjk+" Tidak di kenali,\nSilahkan ketik cowo untuk Laki-Laki atau cewe untuk perempuan..!!", parent=root)
    def caripinjaman():
        cari=pinjamans.get()
        def denda():
            cur.execute("SELECT lama_pinjam FROM `data_pinjaman` WHERE `no` = '"+ cari +"'")
            longday=cur.fetchall()
            def tgltog():
                from datetime import datetime
                sekarang=datetime.now()
                hari=sekarang.day
                return(hari)
            def wulantog():
                from datetime import datetime
                sekarang=datetime.now()
                bulan=sekarang.month
                return(bulan)
            def tahuntog():
                from datetime import datetime
                sekarang=datetime.now()
                tahun=sekarang.year
                return(tahun)
            def wulanntahun():
                from datetime import datetime
                sekarang=datetime.now()
                tahun=sekarang.year
                bulan=sekarang.month
                return("/{}/{}".format(bulan, tahun))
            cur.execute("SELECT tgl_kembali FROM `data_pinjaman` WHERE `no` = '"+ cari +"'")
            kembali=cur.fetchall()
            tmp=str(kembali[0][0])
            tamp=tmp[0]
            tampung=tmp[0]+tmp[1]
            bulan=int(wulantog())
            hari=int(tgltog())
            if tmp[1] == "/" :
                if hari > int(tamp) :
                    lopeh=hari-int(tamp)
                    if lopeh == 1:
                        brplamas.delete(0, END)
                        brplamas.insert(END, "1000")
                    if lopeh == 2:
                        brplamas.delete(0, END)
                        brplamas.insert(END, "2000")
                    if lopeh >= 3:
                        brplamas.delete(0, END)
                        brplamas.insert(END, "5000")
                else :
                    brplamas.delete(0, END)
                    brplamas.insert(END, "0")
            else:
                if hari > int(tampung) :
                    lopeh=hari-int(tampung)
                    if lopeh == 1:
                        brplamas.delete(0, END)
                        brplamas.insert(END, "1000")
                    if lopeh == 2:
                        brplamas.delete(0, END)
                        brplamas.insert(END, "2000")
                    if lopeh >= 3:
                        brplamas.delete(0, END)
                        brplamas.insert(END, "5000")
                else:
                    brplamas.delete(0, END)
                    brplamas.insert(END, "0")
            
        if cari == '':
            mb.showerror("Error!!", "Jika ingin Melakukan Pencarian\n No Pinjaman Tidak Boleh Kosong..!!", parent=root)
        else :
            cur.execute("SELECT * FROM `data_pinjaman` WHERE `no` = '"+ cari +"'")
            global buku
            buku=cur.fetchall()
            if not buku:
                mb.showerror("Error!!", "No Pinjaman tidak dikenali..!!", parent=root)
                juduls.delete(0, END)
                idbukus.delete(0, END)
                namas.delete(0, END)
                jk.delete(0, END)
                alamats.delete(0, END)
                tglpinjams.delete(0, END)
                tglkembalis.delete(0, END)
                brplamas.delete(0,END)
            else:
                cur.execute("SELECT kode_buku FROM `data_pinjaman` WHERE `no` = '"+ cari +"'")
                kodebuku=cur.fetchall()
                idbukus.delete(0, END)
                idbukus.insert(END, kodebuku[0][0])
                cur.execute("SELECT judul FROM `data_pinjaman` WHERE `no` = '"+ cari +"'")
                judul=cur.fetchall()
                juduls.delete(0, END)
                juduls.insert(END, judul[0][0])
                cur.execute("SELECT nama FROM `data_pinjaman` WHERE `no` = '"+ cari +"'")
                nama=cur.fetchall()
                namas.delete(0, END)
                namas.insert(END, nama[0][0])
                cur.execute("SELECT jenis_kelamin FROM `data_pinjaman` WHERE `no` = '"+ cari +"'")
                jenisk=cur.fetchall()
                if jenisk[0][0] == "Laki-Laki" :
                    jk.delete(0, END)
                    jk.insert(END, "cowo")
                if jenisk[0][0] == "Perempuan" :
                    jk.delete(0, END)
                    jk.insert(END, "cewe")
                cur.execute("SELECT alamat FROM `data_pinjaman` WHERE `no` = '"+ cari +"'")
                almt=cur.fetchall()
                alamats.delete(0, END)
                alamats.insert(END, almt[0][0])
                cur.execute("SELECT tgl_pinjam FROM `data_pinjaman` WHERE `no` = '"+ cari +"'")
                pnjm=cur.fetchall()
                tglpinjams.delete(0, END)
                tglpinjams.insert(END, pnjm[0][0])
                cur.execute("SELECT tgl_kembali FROM `data_pinjaman` WHERE `no` = '"+ cari +"'")
                kmbl=cur.fetchall()
                tglkembalis.delete(0, END)
                tglkembalis.insert(END, kmbl[0][0])
                #denda()
    root.protocol("WM_DELETE_WINDOW", tutup)        
    ##==========================================
    ##Seting Frame

    f=Frame(root,bg=abang)
    f2=Frame(root,bd=10)
    f3=Frame(root,bd=10)
    f.pack(fill=BOTH)
    f2.pack(fill=BOTH, expand=YES)
    f3.pack(fill=BOTH, )

    Label(f, text="Pengembalian Buku", font="Forte 15", fg='white', bg=abang).pack()
    
    
    ##Isi Frame
    head = Label(f2,text=' Silahkan Isi data\t:')
    pinjaman = Label(f2,text=' No Pinjaman\t:')
    pinjamans=Entry (f2,width=45)
    idbuku=Label(f2,text=' ID Buku\t\t:')
    idbukus=Entry (f2,width=45)
    pinjamans.focus_set()
    fndbook=Button(f2,text='Cari', width=7,command=caripinjaman)
    judul=Label(f2,text=' Judul\t\t:')
    juduls=Entry (f2,width=45)
    nama = Label(f2,text=' Nama\t\t:')
    namas=Entry (f2,width=45)
    jkelamin = Label(f2,text=' Jenis kelamin\t:')
    jk=Entry (f2,width=45)
    cewe=Label(f2,text="Ketik Cowo Untuk Laki-Laki,\nAtau Cewe Untuk Perempuan, huruf kecil semua")
    #pengarangs=Entry (root,width=45)
    alamat = Label(f2,text=' Alamat\t\t:')
    alamats=Entry (f2,width=45)
    tglpinjam = Label(f2,text=' Tgl Pinjam\t:')
    tglpinjams=Entry (f2,width=45)
    tglkembali=Label(f2,text=' Tgl Kembali\t:')
    tglkembalis=Entry(f2,width=45)
    brplama = Label(f2,text=' Denda\t\t:')
    brplamas=Entry (f2,width=45)
    tgljoin = Label(f2,text=' Tgl Dikembalikan\t:')
    tgljoins=Entry (f2,width=45)
    tgljoins.insert(INSERT, tanggal())
    tbsimpan=Button(f3,text='Simpan', width=10,command=simpan)

    #tampilan
    head.grid(row=1, column=1)
    pinjaman.grid(row=2,column=1)
    pinjamans.grid(row=2,column=2)
    idbuku.grid(row=3,column=1)
    idbukus.grid(row=3,column=2)
    fndbook.grid(row=2,column=3)
    judul.grid(row=4,column=1)
    juduls.grid(row=4,column=2)
    nama.grid(row=5,column=1)
    namas.grid(row=5,column=2)
    jkelamin.grid(row=6,column=1)
    jk.grid(row=6,column=2)
    cewe.grid(row=7,column=2)
    #pengarangs.grid(row=4,column=2)
    alamat.grid(row=8,column=1)
    alamats.grid(row=8,column=2)
    tglpinjam.grid(row=9,column=1)
    tglpinjams.grid(row=9,column=2)
    tglkembali.grid(row=10,column=1)
    tglkembalis.grid(row=10,column=2)
    brplama.grid(row=12,column=1)
    brplamas.grid(row=12,column=2)
    tgljoin.grid(row=11,column=1)
    tgljoins.grid(row=11, column=2)
    tbsimpan.pack()
##=================================================================================================================================##
## Form Pinjam Buku
def pinjambuku(datUser):
    root=Tk()
    lebar = 450
    tinggi = 360
    setTengahX = (root.winfo_screenwidth()-lebar)//2
    setTengahY = (root.winfo_screenheight()-tinggi)//2
    root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
    root.resizable(False, False)
    cur.execute('select * from data_pinjaman')
    baru=cur.fetchall()
    sekarang=len(baru)
    ##Local Variabel
    self=root
    left=LEFT
    def tglbalek():
        def tgltog():
            from datetime import datetime
            sekarang=datetime.now()
            hari=sekarang.day
            return(hari)
        def wulantog():
            from datetime import datetime
            sekarang=datetime.now()
            bulan=sekarang.month
            return(bulan)
        def tahuntog():
            from datetime import datetime
            sekarang=datetime.now()
            tahun=sekarang.year
            return(tahun)
        def wulanntahun():
            from datetime import datetime
            sekarang=datetime.now()
            tahun=sekarang.year
            bulan=sekarang.month
            return("/{}/{}".format(bulan, tahun))
        longday=brplamas.get()
        if longday=='' :
            mb.showerror("Error!!", "Jika ingin Melakukan Pencarian\nKolom Lama Pinjaman Tidak Boleh Kosong..!!", parent=root)
            brplamas.delete(0,END)
            longday=0
            hasil=' '
        hitung=int(longday)+int(tgltog())
        bulan=int(wulantog())
        hari=int(tgltog())
        if int(longday)>30:
            mb.showerror("Error!!", "Peminjaman Buku Dilarang lebih dari 30 Hari!!", parent=root)
            brplamas.delete(0,END)
            hasil=' '
        elif bulan==12 :
            if hitung<=31 :
                hasil=str(hitung)+str(wulanntahun())
            elif hitung>31:
                if bulan==12:
                    hari=int(tgltog())+int(longday)-31
                    if bulan==12 :
                        bulan=1
                        tahun=tahuntog()+1
                    hasil=str(hari)+"/"+str(bulan)+"/"+str(tahun)
        elif bulan==11 :
            if hitung<=30 :
                hasil=str(hitung)+str(wulanntahun())
            elif hitung>30:
                if bulan==12:
                    hari=int(tgltog())+int(longday)-30
                    if bulan==12 :
                        bulan=1
                        tahun=tahuntog()+1
                    else :
                        bulan=bulan+1
                        tahun=tahuntog()
                    hasil=str(hari)+"/"+str(bulan)+"/"+str(tahun)
        elif bulan==10 :
            if hitung<=31 :
                hasil=str(hitung)+str(wulanntahun())
            elif hitung>31:
                if bulan==12:
                    hari=int(tgltog())+int(longday)-31
                    if bulan==12 :
                        bulan=1
                        tahun=tahuntog()+1
                    else :
                        bulan=bulan+1
                        tahun=tahuntog()
                    hasil=str(hari)+"/"+str(bulan)+"/"+str(tahun)

        elif bulan==9 :
            if hitung<=30 :
                hasil=str(hitung)+str(wulanntahun())
            elif hitung>30:
                if bulan==12:
                    hari=int(tgltog())+int(longday)-30
                    if bulan==12 :
                        bulan=1
                        tahun=tahuntog()+1
                    else :
                        bulan=bulan+1
                        tahun=tahuntog()
                    hasil=str(hari)+"/"+str(bulan)+"/"+str(tahun)

        elif bulan==8 :
            if hitung<=31 :
                hasil=str(hitung)+str(wulanntahun())
            elif hitung>31:
                if bulan==12:
                    hari=int(tgltog())+int(longday)-31
                    if bulan==12 :
                        bulan=1
                        tahun=tahuntog()+1
                    else :
                        bulan=bulan+1
                        tahun=tahuntog()
                    hasil=str(hari)+"/"+str(bulan)+"/"+str(tahun)

        elif bulan==7 :
            if hitung<=31 :
                hasil=str(hitung)+str(wulanntahun())
            elif hitung>31:
                if bulan==12:
                    hari=int(tgltog())+int(longday)-31
                    if bulan==12 :
                        bulan=1
                        tahun=tahuntog()+1
                    else :
                        bulan=bulan+1
                        tahun=tahuntog()
                    hasil=str(hari)+"/"+str(bulan)+"/"+str(tahun)

        elif bulan==6 :
            if hitung<=30 :
                hasil=str(hitung)+str(wulanntahun())
            elif hitung>30:
                if bulan==12:
                    hari=int(tgltog())+int(longday)-30
                    if bulan==12 :
                        bulan=1
                        tahun=tahuntog()+1
                    else :
                        bulan=bulan+1
                        tahun=tahuntog()
                    hasil=str(hari)+"/"+str(bulan)+"/"+str(tahun)

        elif bulan==5 :
            if hitung<=31 :
                hasil=str(hitung)+str(wulanntahun())
            elif hitung>31:
                if bulan==12:
                    hari=int(tgltog())+int(longday)-31
                    if bulan==12 :
                        bulan=1
                        tahun=tahuntog()+1
                    else :
                        bulan=bulan+1
                        tahun=tahuntog()
                    hasil=str(hari)+"/"+str(bulan)+"/"+str(tahun)

        elif bulan==4 :
            if hitung<=30 :
                hasil=str(hitung)+str(wulanntahun())
            elif hitung>30:
                if bulan==12:
                    hari=int(tgltog())+int(longday)-30
                    if bulan==12 :
                        bulan=1
                        tahun=tahuntog()+1
                    else :
                        bulan=bulan+1
                        tahun=tahuntog()
                    hasil=str(hari)+"/"+str(bulan)+"/"+str(tahun)

        elif bulan==3 :
            if hitung<=31 :
                hasil=str(hitung)+str(wulanntahun())
            elif hitung>31:
                if bulan==12:
                    hari=int(tgltog())+int(longday)-31
                    if bulan==12 :
                        bulan=1
                        tahun=tahuntog()+1
                    else :
                        bulan=bulan+1
                        tahun=tahuntog()
                    hasil=str(hari)+"/"+str(bulan)+"/"+str(tahun)

        elif bulan==2 :
            if hitung<=28 :
                hasil=str(hitung)+str(wulanntahun())
            elif hitung>28:
                if bulan==12:
                    hari=int(tgltog())+int(longday)-28
                    if bulan==12 :
                        bulan=1
                        tahun=tahuntog()+1
                    else :
                        bulan=bulan+1
                        tahun=tahuntog()
                    hasil=str(hari)+"/"+str(bulan)+"/"+str(tahun)

        elif bulan==1 :
            if hitung<=31 :
                hasil=str(hitung)+str(wulanntahun())
            elif hitung>31:
                if bulan==12:
                    hari=int(tgltog())+int(longday)-31
                    if bulan==12 :
                        bulan=1
                        tahun=tahuntog()+1
                    else :
                        bulan=bulan+1
                        tahun=tahuntog()
                    hasil=str(hari)+"/"+str(bulan)+"/"+str(tahun)       

        
        tgljoins.delete(0, END)
        tgljoins.insert(END, str(hasil))

    def simpan():
        smid=idbukus.get()
        smjudul=juduls.get()
        smnama=namas.get()
        smjk=jk.get()
        if smjk=="cowo" :
            smjk="Laki-Laki"
            smalamat=alamats.get()
            smtglpinjam=tglpinjams.get()
            smlong=brplamas.get()
            smback=tgljoins.get()
            data=(smid,smjudul,smnama,smjk,smalamat,smtglpinjam,smlong,smback)
            query="insert into data_pinjaman (kode_buku, judul, nama, jenis_kelamin, alamat, tgl_pinjam, lama_pinjam, tgl_kembali) values"+str(data)
            cur.execute(query)
            con.commit()
            mb.showinfo("Sukses", "Berhasil Menambah Peminjam "+smnama+" ke Database..!!", parent=root)
            print(waktu()+' - '+"User ["+datUser+"] Menambah Peminjam "+smnama+" ke Database...")
            tutup()
        elif smjk=="cewe" :
            smjk="Perempuan"
            smalamat=alamats.get()
            smtglpinjam=tglpinjams.get()
            smlong=brplamas.get()
            smback=tgljoins.get()
            data=(smid,smjudul,smnama,smjk,smalamat,smtglpinjam,smlong,smback)
            query="insert into data_pinjaman (kode_buku, judul, nama, jenis_kelamin, alamat, tgl_pinjam, lama_pinjam, tgl_kembali) values"+str(data)
            cur.execute(query)
            con.commit()
            mb.showinfo("Sukses", "Berhasil Menambah Peminjam "+smnama+" ke Database..!!", parent=root)
            print(waktu()+' - '+"User ["+datUser+"] Menambah Peminjam "+smnama+" ke Database...")
            tutup()
        else:
            mb.showwarning("Warning!!", "Jenis Kelamin "+smjk+" Tidak di kenali,\nSilahkan ketik cowo untuk Laki-Laki atau cewe untuk perempuan..!!", parent=root)
        
        
    def caribuku():
        cari=idbukus.get()
        if cari == '':
            mb.showerror("Error!!", "Jika ingin Melakukan Pencarian\nKolom ID Buku Tidak Boleh Kosong..!!", parent=root)
        else :
            cur.execute("SELECT * FROM `data_buku` WHERE `id` = '"+ cari +"'")
            global buku
            buku=cur.fetchall()
            if not buku:
                mb.showerror("Error!!", "ID Buku tidak dikenali..!!", parent=root)
                juduls.delete(0, END)
            else:
                cur.execute("SELECT judul FROM `data_buku` WHERE `id` = '"+ cari +"'")
                bukujudul=cur.fetchall()
                juduls.delete(0, END)
                juduls.insert(END, bukujudul[0][0])
    def carianggota():
        cari=namas.get()
        if cari == '':
            mb.showerror("Error!!", "Jika ingin Melakukan Pencarian\nKolom Nama Tidak Boleh Kosong..!!", parent=root)
        else :
            cur.execute("SELECT * FROM `data_anggota` WHERE `nama` = '"+ cari +"'")
            global anggota
            anggota=cur.fetchall()
            if not anggota:
                mb.showerror("Error!!", "Tidak ada anggota bernama "+cari+" di daftar anggota..!!", parent=root)
                jk.delete(0, END)
                alamats.delete(0, END)
            else:
                cur.execute("SELECT jenis_kelamin FROM `data_anggota` WHERE `nama` = '"+ cari +"'")
                jenisk=cur.fetchall()
                if jenisk[0][0] == "Laki-Laki" :
                    jk.delete(0, END)
                    jk.insert(END, "cowo")
                if jenisk[0][0] == "Perempuan" :
                    jk.delete(0, END)
                    jk.insert(END, "cewe")
                cur.execute("SELECT alamat FROM `data_anggota` WHERE `nama` = '"+ cari +"'")
                almt=cur.fetchall()
                alamats.delete(0, END)
                alamats.insert(END, almt[0][0])
    def tutup():
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Menutup Peminjaman Buku...")

    root.protocol("WM_DELETE_WINDOW", tutup)        
    ##==========================================
    ##Seting Frame

    f=Frame(root,bg=abang)
    f2=Frame(root, bd=10)
    f3=Frame(root, bd=10)
    f.pack(fill=BOTH)
    f2.pack(fill=BOTH,expand=YES)
    f3.pack(fill=BOTH, side=BOTTOM)

    Label(f, text="Peminjaman Buku", font="Forte 15", fg='white', bg=abang).pack()
    
    ##Isi Frame
    head = Label(f2,text=' Silahkan Isi data\t:')
    pinjaman = Label(f2,text=' No Pinjaman\t:')
    pinjamans=Entry (f2,width=45)
    pinjamans.insert(INSERT, str(sekarang+1))
    idbuku=Label(f2,text=' ID Buku\t\t:')
    idbukus=Entry (f2,width=45)
    idbukus.focus_set()
    fndbook=Button(f2,text='Cari', width=7,command=caribuku)
    judul=Label(f2,text=' Judul\t\t:')
    juduls=Entry (f2,width=45)
    nama = Label(f2,text=' Nama\t\t:')
    namas=Entry (f2,width=45)
    fndname=Button(f2,text='Cari', width=7,command=carianggota)
    jkelamin = Label(f2,text=' Jenis kelamin\t:')
    jk=Entry (f2,width=45)
    cewe=Label(f2,text="Ketik Cowo Untuk Laki-Laki,\nAtau Cewe Untuk Perempuan, huruf kecil semua")
    #pengarangs=Entry (root,width=45)
    alamat = Label(f2,text=' Alamat\t\t:')
    alamats=Entry (f2,width=45)
    tglpinjam = Label(f2,text=' Tgl Pinjam\t:')
    tglpinjams=Entry (f2,width=45)
    tglpinjams.insert(INSERT, tanggal())
    brplama = Label(f2,text=' Lama Pinjaman\t:')
    brplamas=Entry (f2,width=45)
    fnddate=Button(f2,text='Hitung', width=7,command=tglbalek)
    tgljoin = Label(f2,text=' Tgl Kembali\t:')
    tgljoins=Entry (f2,width=45)
    tgljoins.insert(INSERT, tanggal())
    tbsimpan=Button(f3,text='Simpan', width=10, command=simpan)

    #tampilan
    head.grid(row=1, column=1)
    pinjaman.grid(row=2,column=1)
    pinjamans.grid(row=2,column=2)
    idbuku.grid(row=3,column=1)
    idbukus.grid(row=3,column=2)
    fndbook.grid(row=3,column=3)
    judul.grid(row=4,column=1)
    juduls.grid(row=4,column=2)
    nama.grid(row=5,column=1)
    namas.grid(row=5,column=2)
    fndname.grid(row=5,column=3)
    jkelamin.grid(row=6,column=1)
    jk.grid(row=6,column=2)
    cewe.grid(row=7,column=2)
    #pengarangs.grid(row=4,column=2)
    alamat.grid(row=8,column=1)
    alamats.grid(row=8,column=2)
    tglpinjam.grid(row=9,column=1)
    tglpinjams.grid(row=9,column=2)
    brplama.grid(row=10,column=1)
    brplamas.grid(row=10,column=2)
    fnddate.grid(row=10,column=3)
    tgljoin.grid(row=11,column=1)
    tgljoins.grid(row=11, column=2)
    tbsimpan.pack()
    
##=================================================================================================================================##
## Form Cari Anggota
def carianggota(datUser):
    root=Tk()
    def tutupaja():
        root.destroy()
    def tutup():
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Menutup Pencarian Anggota...")
    def hasilcari():
        root=Tk()
        def tutup():
            root.destroy()
            print(waktu()+' - '+"User ["+datUser+"] Menutup Pencarian Anggota...")
        root.protocol("WM_DELETE_WINDOW", tutup)
        lebar = 800
        tinggi = 480
        setTengahX = (root.winfo_screenwidth()-lebar)//2
        setTengahY = (root.winfo_screenheight()-tinggi)//2
        root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        root.resizable(False, False)
        ##Local Variabel
        self=root
        ##Seting isi

        f=Frame(root,bg=abang)
        f2=Frame(root)
        f.pack(fill=BOTH)
        f2.pack(fill=BOTH, expand=YES)
        
        Label(f, text="Hasil Pencarian", font="Forte 15", fg='white', bg=abang).pack()
        
        tmid=Label(f2,text='ID')
        tmjudul=Label(f2,text='Nama Anggota')
        tmpengarang=Label(f2,text='Jenis Kelamin')
        tmtterbit=Label(f2,text='Tanggal Lahir')
        tmpenerbit=Label(f2,text='Alamat')
        tmjumlah=Label(f2,text='Tanggal Bergabung')
        
        tmid.grid(row=0,column=0,sticky=W)
        tmjudul.grid(row=0,column=1,sticky=W)
        tmpengarang.grid(row=0,column=2,sticky=W)
        tmtterbit.grid(row=0,column=3,sticky=W)
        tmpenerbit.grid(row=0,column=4,sticky=W)
        tmjumlah.grid(row=0,column=5,sticky=W)

        for i in range(len(anggota)):
            for j in range(len(anggota[i])):
                teks=Entry(f2)
                teks.grid(row=i+1,column=j)
                teks.insert(END,anggota[i][j])
    def goleki():
        cari=caris.get()
        if cari == '':
            mb.showerror("Error!!", "Jika ingin Melakukan Pencarian\nKolom Pencarian Tidak Boleh Kosong..!!", parent=root)
        else :
            cur.execute("SELECT * FROM `data_anggota` WHERE `nama` = '"+ cari +"'")
            global anggota
            anggota=cur.fetchall()
            if not anggota:
                cur.execute("SELECT * FROM `data_anggota` WHERE `nama` LIKE '%"+ cari +"%'")
                anggota=cur.fetchall()
                if not anggota:
                    cur.execute("SELECT * FROM `data_anggota` WHERE `id` = '"+ cari +"'")
                    anggota=cur.fetchall()
                    if not anggota:
                        cur.execute("SELECT * FROM `data_anggota` WHERE `id` LIKE '%"+ cari +"'")
                        anggota=cur.fetchall()
                        if not anggota:
                            mb.showerror("Error!!", "Anggota yang anda cari tidak ditemukan..!!", parent=root)
                        else:
                            tutupaja()
                            hasilcari()
                    else:
                        tutupaja()
                        hasilcari()
                else:
                    tutupaja()
                    hasilcari()
            else:
                tutupaja()
                hasilcari()
    root.protocol("WM_DELETE_WINDOW", tutup)
    lebar = 420
    tinggi = 90
    setTengahX = (root.winfo_screenwidth()-lebar)//2
    setTengahY = (root.winfo_screenheight()-tinggi)//2
    root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
    root.resizable(False, False)
    ##Local Variabel
    self=root
    ##Seting isi
    f=Frame(root, bg=abang)
    f.pack(fill=BOTH)
    fjudul=Frame(root)
    fjudul.pack(fill=BOTH, side=TOP,expand=YES)
    fisi=Frame(root)
    fisi.pack(fill=BOTH, expand=YES)

    Label(f, text="Pencarian", font="Forte 15", fg='white', bg=abang).pack()
    
    Label(fjudul,text="Silahkan Masukan Nama Anggota / ID Anggota", font=('Calibri',11)).pack(fill=BOTH, expand=YES)
    Label(fisi, text="Cari : ").grid(row=0,column=0,sticky=W)
    caris=Entry(fisi,width=50)
    caris.grid(row=0,column=1,sticky=W)
    Button(fisi,width=10,text='Cari',command=goleki).grid(row=0,column=2,sticky=W)
##=================================================================================================================================##
## Form Cari Buku
def caribuku(datUser):
    root=Tk()
    def tutupaja():
        root.destroy()
    def tutup():
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Menutup Pencarian Buku...")
    def hasilcari():
        root=Tk()
        def tutup():
            root.destroy()
            print(waktu()+' - '+"User ["+datUser+"] Menutup Pencarian Buku...")
        root.protocol("WM_DELETE_WINDOW", tutup)
        lebar = 800
        tinggi = 480
        setTengahX = (root.winfo_screenwidth()-lebar)//2
        setTengahY = (root.winfo_screenheight()-tinggi)//2
        root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        root.resizable(False, False)
        ##Local Variabel
        self=root
        ##Seting isi

        f=Frame(root,bg=abang)
        f2=Frame(root)
        f.pack(fill=BOTH)
        f2.pack(fill=BOTH, expand=YES)
        
        Label(f, text="Hasil Pencarian", font="Forte 15", fg='white', bg=abang).pack()
        
        tmid=Label(f2,text='ID')
        tmjudul=Label(f2,text='Judul Buku')
        tmpengarang=Label(f2,text='Pengarang')
        tmtterbit=Label(f2,text='Tahun Terbit')
        tmpenerbit=Label(f2,text='Penerbit')
        tmjumlah=Label(f2,text='Jumlah')
        tmlokasi=Label(f2,text='Lokasi')

        tmid.grid(row=0,column=0,sticky=W)
        tmjudul.grid(row=0,column=1,sticky=W)
        tmpengarang.grid(row=0,column=2,sticky=W)
        tmtterbit.grid(row=0,column=3,sticky=W)
        tmpenerbit.grid(row=0,column=4,sticky=W)
        tmjumlah.grid(row=0,column=5,sticky=W)
        tmlokasi.grid(row=0,column=6,sticky=W)

        for i in range(len(buku)):
            for j in range(len(buku[i])):
                teks=Entry(f2)
                teks.grid(row=i+1,column=j)
                teks.insert(END,buku[i][j])
    def goleki():
        cari=caris.get()
        if cari == '':
            mb.showerror("Error!!", "Jika ingin Melakukan Pencarian\nKolom Pencarian Tidak Boleh Kosong..!!", parent=root)
        else :
            cur.execute("SELECT * FROM `data_buku` WHERE `judul` = '"+ cari +"'")
            global buku
            buku=cur.fetchall()
            if not buku:
                cur.execute("SELECT * FROM `data_buku` WHERE `judul` LIKE '%"+ cari +"%'")
                buku=cur.fetchall()
                if not buku:
                    mb.showerror("Error!!", "Buku yang anda cari tidak di temukan..!!", parent=root)
                else:
                    tutupaja()
                    hasilcari()
            else:
                tutupaja()
                hasilcari()
    root.protocol("WM_DELETE_WINDOW", tutup)
    lebar = 400
    tinggi = 90
    setTengahX = (root.winfo_screenwidth()-lebar)//2
    setTengahY = (root.winfo_screenheight()-tinggi)//2
    root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
    root.resizable(False, False)
    ##Local Variabel
    self=root
    ##Seting isi
    f=Frame(root,bg=abang)
    f.pack(fill=BOTH)
    fjudul=Frame(root)
    fjudul.pack(fill=BOTH, side=TOP,expand=YES)
    fisi=Frame(root)
    fisi.pack(fill=BOTH, expand=YES)

    Label(f, text="Pencarian", font="Forte 15", fg='white', bg=abang).pack()
    
    Label(fjudul,text="Silahkan Masukan Judul Buku", font=('Calibri',11)).pack(fill=BOTH, expand=YES)
    Label(fisi, text="Nama Buku :").grid(row=0,column=0,sticky=W)
    caris=Entry(fisi,width=40)
    caris.grid(row=0,column=1,sticky=W)
    Button(fisi,width=10,text='Cari',command=goleki).grid(row=0,column=2,sticky=W)
##=================================================================================================================================##
## Form Tampilkan anggota
def tampilanggota(datUser):
    root=Tk()
    def tutup():
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Menutup Tentang Daftar Anggota...")
    root.protocol("WM_DELETE_WINDOW", tutup)
    lebar = 750
    tinggi = 480
    setTengahX = (root.winfo_screenwidth()-lebar)//2
    setTengahY = (root.winfo_screenheight()-tinggi)//2
    root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
    root.resizable(False, False)
    ##Local Variabel
    self=root
    cur.execute('select * from data_anggota')
    anggota=cur.fetchall()
    ##Seting isi

    f=Frame(root,bg=abang)
    f2=Frame(root)
    f.pack(fill=BOTH)
    f2.pack(fill=BOTH,expand=YES)
    
    Label(f, text="Daftar Anggota", font="Forte 15", fg='white', bg=abang).pack()
    
    tmid=Label(f2,text='ID')
    tmjudul=Label(f2,text='Nama Anggota')
    tmpengarang=Label(f2,text='Jenis Kelamin')
    tmtterbit=Label(f2,text='Tanggal Lahir')
    tmpenerbit=Label(f2,text='Alamat')
    tmjumlah=Label(f2,text='Tanggal Bergabung')

    tmid.grid(row=0,column=0,sticky=W)
    tmjudul.grid(row=0,column=1,sticky=W)
    tmpengarang.grid(row=0,column=2,sticky=W)
    tmtterbit.grid(row=0,column=3,sticky=W)
    tmpenerbit.grid(row=0,column=4,sticky=W)
    tmjumlah.grid(row=0,column=5,sticky=W)

    for i in range(len(anggota)):
        for j in range(len(anggota[i])):
            teks=Entry(f2)
            teks.grid(row=i+1,column=j)
            teks.insert(END,anggota[i][j])
##=================================================================================================================================##
## Form Tampilkan Buku
def tampilbuku(datUser):
    root=Tk()
    def tutup():
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Menutup Tentang Daftar Buku...")
    root.protocol("WM_DELETE_WINDOW", tutup)
    lebar = 800
    tinggi = 480
    setTengahX = (root.winfo_screenwidth()-lebar)//2
    setTengahY = (root.winfo_screenheight()-tinggi)//2
    root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
    root.resizable(False, False)
    ##Local Variabel
    self=root
    cur.execute('select * from data_buku')
    buku=cur.fetchall()
    ##Seting isi

    f=Frame(root,bg=abang)
    f2=Frame(root)
    f.pack(fill=BOTH)
    f2.pack(fill=BOTH, expand=YES)
    
    Label(f, text="Daftar Buku", font="Forte 15", fg='white', bg=abang).pack()
    
    tmid=Label(f2,text='ID')
    tmjudul=Label(f2,text='Judul Buku')
    tmpengarang=Label(f2,text='Pengarang')
    tmtterbit=Label(f2,text='Tahun Terbit')
    tmpenerbit=Label(f2,text='Penerbit')
    tmjumlah=Label(f2,text='Jumlah')
    tmlokasi=Label(f2,text='Lokasi')

    tmid.grid(row=0,column=0,sticky=W)
    tmjudul.grid(row=0,column=1,sticky=W)
    tmpengarang.grid(row=0,column=2,sticky=W)
    tmtterbit.grid(row=0,column=3,sticky=W)
    tmpenerbit.grid(row=0,column=4,sticky=W)
    tmjumlah.grid(row=0,column=5,sticky=W)
    tmlokasi.grid(row=0,column=6,sticky=W)

    for i in range(len(buku)):
        for j in range(len(buku[i])):
            teks=Entry(f2)
            teks.grid(row=i+1,column=j)
            teks.insert(END,buku[i][j])
##=================================================================================================================================##
## Form Tentang App
def tentangapp(datUser):
    root=Tk()
    def tutup():
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Menutup Tentang Aplikasi...")
    def cp():
        programer(datUser)
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Menutup Tentang Aplikasi...")
        print(waktu()+' - '+"User ["+datUser+"] Membuka Contact Person...")
    def komponen():
        ##Seting Frame
        f=Frame(root, bg=abang)
        f2=Frame(root)
        f3=Frame(root,bd=15)
        f.pack(fill=BOTH)
        f2.pack(fill=Y)
        f3.pack(fill=Y, expand=YES,side=BOTTOM)
        ## Isi frame
        Label(f, text="Tengtang Aplikasi", font="Forte 15", fg='white', bg=abang).pack()
        Label(f2, text='Program Perpustakaan Terpadu').pack()
        Label(f2, text='E-Perpus').pack()
        Label(f2, text='Software Version : 4.0 (Stabil)').pack()
        Label(f2, text='Engine Version : Python 3.6.0').pack()
        Label(f2, text='Database Version : Mysql 10.1.21-MariaDB').pack()
        Button(f3, text='Contact Person', width=15, command=cp).pack()
        Button(f3, text='OK', width=15, command=tutup).pack()
    def konfigurasi():
        lebar = 300
        tinggi = 220
        setTengahX = (root.winfo_screenwidth()-lebar)//2
        setTengahY = (root.winfo_screenheight()-tinggi)//2
        root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        root.resizable(False, False)
        komponen()
    konfigurasi()##memuat konfigurasi
##=================================================================================================================================##
## Form Tambah Anggota
def tambahanggota(datUser):
    root=Tk()
    lebar = 400
    tinggi = 260
    setTengahX = (root.winfo_screenwidth()-lebar)//2
    setTengahY = (root.winfo_screenheight()-tinggi)//2
    root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
    root.resizable(False, False)
    cur.execute('select * from data_anggota')
    baru=cur.fetchall()
    sekarang=len(baru)
    ##Local Variabel
    self=root
    left=LEFT
    pilihan=IntVar()
    ##Fungtion
    def tutup():
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Menutup Tambah Anggota...")
    root.protocol("WM_DELETE_WINDOW", tutup)
    def simpan():
        #smid=int(bukus.get())
        #smid=' '
        #tmp=0+int(pilihan.get())
        smnama=namas.get()
        smtgllahir=tgllahirs.get()
        smalamat=alamats.get()
        smjoin=tgljoins.get()
        if jk.get()=="cowo":
            smjk='Laki-Laki'
            data=(smnama, smjk, smtgllahir, smalamat, smjoin)
            query="insert into data_anggota (nama, jenis_kelamin, tanggal_lahir, alamat, bergabung) values"+str(data)
            cur.execute(query)
            con.commit()
            mb.showinfo("Sukses", "Berhasil Menambah Anggota baru dengan nama : "+smnama+" ke Database..!!", parent=root)
            print(waktu()+' - '+"User ["+datUser+"] Menambah Anggota baru dengan nama : "+smnama+" ke Database...")
            tutup()
            
        elif jk.get()=="cewe":
            smjk='Perempuan'
            data=(smnama, smjk, smtgllahir, smalamat, smjoin)
            query="insert into data_anggota (nama, jenis_kelamin, tanggal_lahir, alamat, bergabung) values"+str(data)
            cur.execute(query)
            con.commit()
            mb.showinfo("Sukses", "Berhasil Menambah Anggota baru dengan nama : "+smnama+" ke Database..!!", parent=root)
            print(waktu()+' - '+"User ["+datUser+"] Menambah Anggota baru dengan nama : "+smnama+" ke Database...")
            tutup()
        else :
            mb.showwarning("Warning!!", "Jenis Kelamin "+jk.get()+" Tidak di kenali,\nSilahkan ketik cowo untuk Laki-Laki atau cewe untuk perempuan..!!", parent=root)
            print(waktu()+' - '+"User ["+datUser+"] Salah menginputkan jenis Kelamin, System Error...")
            root.destroy()
    ##==========================================
    ##Seting Frame
    f=Frame(root,bg=abang)
    f2=Frame(root)
    f3=Frame(root,bd=10)
    f.pack(fill=BOTH)
    f2.pack(fill=BOTH)
    f3.pack(fill=BOTH)

    ##Isi Frame

    
    
    Label(f, text="Tambah Anggota", font="Forte 15", fg='white', bg=abang).pack()
    head = Label(f2,text=' Silahkan Isi data\t:')
    anggota = Label(f2,text=' ID\t\t:')
    anggotas=Entry (f2,width=45)
    anggotas.insert(INSERT, str(sekarang+1))
    nama = Label(f2,text=' Nama\t\t:')
    namas=Entry (f2,width=45)
    namas.focus_set()
    jkelamin = Label(f2,text=' Jenis kelamin\t:')
    jk=Entry (f2,width=45)
    cewe=Label(f2,text="Ketik Cowo Untuk Laki-Laki,\nAtau Cewe Untuk Perempuan, huruf kecil semua")
    #pengarangs=Entry (root,width=45)
    tgllahir = Label(f2,text=' Tgl Lahir\t:')
    tgllahirs=Entry (f2,width=45)
    tgllahirs.insert(INSERT, tanggal())
    alamat = Label(f2,text=' Alamat\t\t:')
    alamats=Entry (f2,width=45)
    tgljoin = Label(f2,text=' Tgl Bergabung\t:')
    tgljoins=Entry (f2,width=45)
    tgljoins.insert(INSERT, tanggal())
    tbsimpan=Button(f3,text='Simpan',command=simpan, width=10)

    #tampilan
    head.grid(row=1, column=1)
    anggota.grid(row=2,column=1)
    anggotas.grid(row=2,column=2)
    nama.grid(row=3,column=1)
    namas.grid(row=3,column=2)
    jkelamin.grid(row=4,column=1)
    jk.grid(row=4,column=2)
    cewe.grid(row=5,column=2)
    #pengarangs.grid(row=4,column=2)
    tgllahir.grid(row=6,column=1)
    tgllahirs.grid(row=6,column=2)
    alamat.grid(row=7,column=1)
    alamats.grid(row=7,column=2)
    tgljoin.grid(row=8,column=1)
    tgljoins.grid(row=8, column=2)
    tbsimpan.pack()
##=================================================================================================================================##
## Form Tambah Buku
def tambahbuku(datUser):
    root=Tk()
    lebar = 400
    tinggi = 260
    setTengahX = (root.winfo_screenwidth()-lebar)//2
    setTengahY = (root.winfo_screenheight()-tinggi)//2
    root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
    root.resizable(False, False)
    cur.execute('select * from data_buku')
    baru=cur.fetchall()
    sekarang=len(baru)

    ##Local Variabel
    self=root
    left=LEFT
    ##Fungtion
    def tutup():
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Menutup Tambah Buku...")
    def simpan():
        #smid=int(bukus.get())
        #smid=' '
        smjudul=juduls.get()
        smpengarang=pengarangs.get()
        smtterbit=int(tterbits.get())
        smpenerbit=npenerbits.get()
        smjmbuku=int(jbukus.get())
        smlokasi=lokasis.get()
        data=(smjudul, smpengarang, smtterbit, smpenerbit, smjmbuku, smlokasi)
        query="insert into data_buku (judul, pengarang, th_terbit, penerbit, jumlah, lokasi) values"+str(data)
        cur.execute(query)
        con.commit()
        mb.showinfo("Sukses", "Berhasil Menambah Buku "+smjudul+" ke Database..!!", parent=root)
        print(waktu()+' - '+"User ["+datUser+"] Menambah Buku "+smjudul+" ke Database...")
        tutup()
    root.protocol("WM_DELETE_WINDOW", tutup) 
    ##==========================================
    ##Seting Frame
    f=Frame(root,bg=abang)
    f2=Frame(root,bd=10)
    f3=Frame(root,bd=10)
    f.pack(fill=BOTH)
    f2.pack(fill=BOTH, expand=YES)
    f3.pack(fill=BOTH, side=BOTTOM)
    
    Label(f, text="Tambah Buku", font="Forte 15", fg='white', bg=abang).pack()
    
    ##Isi Frame
    head = Label(f2,text=' Silahkan Isi data\t:')
    buku = Label(f2,text=' ID\t\t:')
    bukus=Entry (f2,width=45)
    bukus.insert(INSERT, str(sekarang+1))
    judul = Label(f2,text=' Judul Buku\t:')
    juduls=Entry (f2,width=45)
    juduls.focus_set()
    pengarang = Label(f2,text=' Pengarang Buku\t:')
    pengarangs=Entry (f2,width=45)
    tterbit = Label(f2,text=' Tahun Terbit\t:')
    tterbits=Entry (f2,width=45)
    npenerbit = Label(f2,text=' Nama Penerbit\t:')
    npenerbits=Entry (f2,width=45)
    jbuku = Label(f2,text=' Jumlah Buku\t:')
    jbukus=Entry (f2,width=45)
    lokasi = Label(f2,text=' Lokasi Buku\t:')
    lokasis=Entry (f2,width=45)
    tbsimpan=Button(f3,text='Simpan',command=simpan, width=10)

    #tampilan
    head.grid(row=1, column=1)
    buku.grid(row=2,column=1)
    bukus.grid(row=2,column=2)
    judul.grid(row=3,column=1)
    juduls.grid(row=3,column=2)
    pengarang.grid(row=4,column=1)
    pengarangs.grid(row=4,column=2)
    tterbit.grid(row=5,column=1)
    tterbits.grid(row=5,column=2)
    npenerbit.grid(row=6,column=1)
    npenerbits.grid(row=6,column=2)
    jbuku.grid(row=7,column=1)
    jbukus.grid(row=7, column=2)
    lokasi.grid(row=8,column=1)
    lokasis.grid(row=8, column=2)
    tbsimpan.pack()
    
##=================================================================================================================================##
## Form About
def aboutus(datUser):
    root=Tk()
    root.resizable(False, False)
    def tutup():
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Menutup About Us...")
    def cp():
        programer(datUser)
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Menutup About Us...")
        print(waktu()+' - '+"User ["+datUser+"] Membuka Contact Person...")
    def komponen():
        ##Seting Frame
        f=Frame(root,bg=abang)
        f2=Frame(root)
        f3=Frame(root,bd=10)
        f.pack(fill=BOTH)
        f2.pack(fill=Y)
        f3.pack(fill=Y, expand=YES,side=BOTTOM)
        ## Isi frame
        Label(f,text='Selamat Datang',font=('Forte',16,),fg='white',bg=abang).pack()
        Label(f,text='=== di Perpustakaan Terpadu (E-Perpus) ===',font=('Calibri',12),fg='white',bg=abang).pack()
        #Label(f2,text=' ',font=('Calibri',12)).pack()
        Label(f2,text='perpustakaan terpadu adalah',font=('Calibri',12)).pack()
        Label(f2,text='suatu unit kerja yang berupa tempat',font=('Calibri',12)).pack()
        Label(f2,text='mengumpulkan, menyimpan dan memelihara',font=('Calibri',12)).pack()
        Label(f2,text='koleksi pustaka baik buku-buku ataupun',font=('Calibri',12)).pack()
        Label(f2,text='bacaan lainnya yang diatur, diorganisasikan',font=('Calibri',12)).pack()
        Label(f2,text='dan diadministrasikan dengan cara tertentu',font=('Calibri',12)).pack()
        Label(f2,text='untuk memberi kemudahan dan digunakan secara',font=('Calibri',12)).pack()
        Label(f2,text='kontinu oleh pemakainya sebagai informasi.',font=('Calibri',12)).pack()
        Button(f3, text='Contact Person', width=15, command=cp).pack()
        Button(f3, text='OK', width=15, command=tutup).pack()
    def konfigurasi():
        lebar = 360
        tinggi = 330
        setTengahX = (root.winfo_screenwidth()-lebar)//2
        setTengahY = (root.winfo_screenheight()-tinggi)//2
        root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        komponen()
    konfigurasi()##memuat konfigurasi
##=================================================================================================================================##
## Menu UTama
def Menuutama(datUser,datPassword, title):
    print(waktu()+' - '+"User ["+datUser+"] telah login ke system")
    root=Tk()
    ##Local Variabel
    cur.execute('select * from data_pengunjung')
    pengunjung=cur.fetchall()
    now=len(pengunjung)
    
    ##Fungtion
    def tambahuserwindow():
        tambahuser(datPassword,datUser)
    def gantipasswindow():
        gantipas(datPassword,datUser)
    def gantinamawindow():
        gantinama(datPassword,datUser)
    def logout():
        root.destroy()
        print(waktu()+' - '+"User ["+datUser+"] Telah Keluar dari System...")
        Main()
    def Tutup():
        root.destroy()
        print(waktu()+' - '+"Disconnecting from Database...")
        print(waktu()+' - '+"Disconnecting from localhost...")
        print(waktu()+' - '+"Stoping Tkinter Module...")
        print(waktu()+' - '+"Stoping Pymysql Module...")
    def tentangwindow():
        tentangapp(datUser)
        print(waktu()+' - '+"User ["+datUser+"] Membuka Tentang Aplikasi...")
    def bantuanwindow():
        bantuan(datUser)
        print(waktu()+' - '+"User ["+datUser+"] Membuka Bantuan...")
    def daftarbukuwindow():
        tampilbuku(datUser)
        print(waktu()+' - '+"User ["+datUser+"] Membuka Daftar Buku...")
    def lihatpinjamanwindow():
        lihatpinjaman(datUser)
        print(waktu()+' - '+"User ["+datUser+"] Membuka Daftar Pinjaman Buku...")
    def kembalianbukuwindow():
        lihatkembali(datUser)
        print(waktu()+' - '+"User ["+datUser+"] Membuka Daftar Pengembalian Buku...")
    def kembalibukuwindow():
        kembalibuku(datUser)
        print(waktu()+' - '+"User ["+datUser+"] Membuka Pengembalian Buku...")
    def pinjambukuwindow():
        pinjambuku(datUser)
        print(waktu()+' - '+"User ["+datUser+"] Membuka Peminjaman Buku...")
    def carianggotawindow():
        carianggota(datUser)
        print(waktu()+' - '+"User ["+datUser+"] Membuka Pencarian Anggota...")
    def caribukuwindow():
        caribuku(datUser)
        print(waktu()+' - '+"User ["+datUser+"] Membuka Pencarian Buku...")
    def daftaranggotawindow():
        tampilanggota(datUser)
        print(waktu()+' - '+"User ["+datUser+"] Membuka Daftar Anggota...")
    def tambahbukuwindow():
        tambahbuku(datUser)
        print(waktu()+' - '+"User ["+datUser+"] Membuka Tambah Buku...")
    def tambahanggotawindow():
        tambahanggota(datUser)
        print(waktu()+' - '+"User ["+datUser+"] Membuka Tambah Anggota...")
    def aboutuswindow():
        aboutus(datUser)
        print(waktu()+' - '+"User ["+datUser+"] Membuka About Us...")
    def jam():
        import time
        a=time.localtime()
        hr=a.tm_hour
        mn=a.tm_min
        return ('{}:{}'.format(hr,mn))
    def tglmenu():
        from datetime import datetime
        sekarang=datetime.now()
        tahun=sekarang.year
        bulan=sekarang.month
        hari=sekarang.day
        return("{}/{}/{}".format(hari, bulan, tahun))
    
    ##Komponen utama
    def komponen():
        ## Deklarasi kan apa yang di pakai di komponen
        f=Frame(root,bg=abang)
        f.pack(fill=BOTH)
        FrameTombol = Frame(root, bd=10,bg=abang)
        FrameTombol.pack(fill=BOTH)
        mainFrame = Frame(root, bd=10, bg=abang)
        mainFrame.pack(fill=BOTH, expand=YES)
        statusFrame = Frame (root,bd=1)
        statusFrame.pack(fill=BOTH, side=BOTTOM)
        menubar = Menu(root)
        def judul():
            Label(f, text="Selamat Datang", font="Algerian 15 bold", fg='white', bg=abang).pack()
            Label(f, text="Perpustakaan Terpadu", font="Broadway 20", fg='white', bg=abang).pack()
            Label(f, text="(E-Perpus)", font="Broadway 18", fg='white', bg=abang).pack()
            Label(f, text="Alamat : Jl Bahureksa No 1 Kajen, Kota Pekalongan, Jawa Tengah", font="Calibri 12", fg='white', bg=abang).pack()
        def tombol():
            Button(FrameTombol,text='Tambah Buku',heigh=3,bg='white',command=tambahbukuwindow).pack(fill=BOTH,expand=YES, side=LEFT)
            Button(FrameTombol,text='Cari Buku',heigh=3,bg='white',command=caribukuwindow).pack(fill=BOTH,expand=YES, side=LEFT)
            Button(FrameTombol,text='Tambah Anggota',heigh=3,bg='white',command=tambahanggotawindow).pack(fill=BOTH,expand=YES, side=LEFT)
            Button(FrameTombol,text='Cari Anggota',heigh=3,bg='white',command=carianggotawindow).pack(fill=BOTH,expand=YES, side=LEFT)
            Button(FrameTombol,text='Peminjaman Buku',heigh=3,bg='white',command=pinjambukuwindow).pack(fill=BOTH,expand=YES, side=LEFT)
            Button(FrameTombol,text='Pengembalian Buku',heigh=3,bg='white',command=kembalibukuwindow).pack(fill=BOTH,expand=YES, side=LEFT)
        def isi():
            def hapus():
                cur.execute('select * from data_pengunjung')
                baru=cur.fetchall()
                sekarang=len(baru)
                #cur.execute('select * from data_pengunjung')
                #baru=cur.fetchall()
                #sekarang=len(baru)
                imnamas.delete(0, END)
                imalamats.delete(0, END)
                imnos.delete(0, END)
                imids.delete(0, END)
                imids.insert(INSERT, str(sekarang+1))
            def barisbaru():
                cur.execute('select * from data_pengunjung')
                akd=cur.fetchall()
                akdaja=len(akd)
                tampilid=Entry(daftarframe)
                tampilnama=Entry(daftarframe)
                tampilalamat=Entry(daftarframe)
                tampilno=Entry(daftarframe)
                tampiltgl=Entry(daftarframe)

                tampilid.grid(row=akdaja, column=0, sticky=W)
                tampilid.insert(0,str(smid))
                tampilnama.grid(row=akdaja, column=1, sticky=W)
                tampilnama.insert(0,str(smnama))
                tampilalamat.grid(row=akdaja, column=2, sticky=W)
                tampilalamat.insert(0,str(smalamat))
                tampilno.grid(row=akdaja, column=3, sticky=W)
                tampilno.insert(0,str(smno))
                tampiltgl.grid(row=akdaja, column=4, sticky=W)
                tampiltgl.insert(0,str(smtgl))
                hapus()
            def simpan():
                global smid
                smid=imids.get()
                global smnama
                smnama=imnamas.get()
                global smalamat
                smalamat=imalamats.get()
                global smno
                smno=imnos.get()
                global smtgl
                smtgl=imtgls.get()
                data=(smnama,smalamat,smno,smtgl)
                query="insert into data_pengunjung (nama, alamat, no, tanggal) values"+str(data)
                cur.execute(query)
                con.commit()
                mb.showinfo("Sukses", "Berhasil Menambah pengunjung "+smnama+" ke Daftar Pengunjung..!!", parent=root)
                print(waktu()+' - '+"User ["+datUser+"] Menambah "+smnama+" ke Daftar Pengunjung...")
                barisbaru()
                
            tambahframe = Frame(mainFrame, bd=8)
            tambahframe.pack(side=LEFT,fill=BOTH)
            daftarframe = Frame(mainFrame)
            daftarframe.pack(fill=BOTH,expand=YES)
            ##Input
            ## Var Tambahan
            tgljoin=str(tanggal())+' , '+str(jam())
            #################
            judul=Label(tambahframe, text='Silahkan Masukan Data Pengunjung :')
            imid=Label(tambahframe,text='No')
            imids=Entry(tambahframe, width=35)
            imids.insert(INSERT, str(now+1))
            imnama=Label(tambahframe,text='Nama')
            imnamas=Entry(tambahframe, width=35)
            imalamat=Label(tambahframe,text='Alamat')
            imalamats=Entry(tambahframe, width=35)
            imno=Label(tambahframe,text='No Hp')
            imnos=Entry(tambahframe, width=35)
            imtgl=Label(tambahframe,text='Tanggal Bergabung')
            imtgls=Entry(tambahframe, width=35)
            imtgls.insert(INSERT, tgljoin)
            imjarak=Label(tambahframe,text=' ')
            imsimpan=Button(tambahframe, width=29, text='Simpan',command=simpan)

            #config
            judul.grid(row=0,sticky=W)
            imid.grid(row=1,sticky=W)
            imids.grid(row=2,sticky=W)
            imnama.grid(row=3,sticky=W)
            imnamas.grid(row=4,sticky=W)
            imalamat.grid(row=5,sticky=W)
            imalamats.grid(row=6,sticky=W)
            imno.grid(row=7,sticky=W)
            imnos.grid(row=8,sticky=W)
            imtgl.grid(row=9,sticky=W)
            imtgls.grid(row=10,sticky=W)
            imjarak.grid(row=11,sticky=W)
            imsimpan.grid(row=12,sticky=W)
            ##Tampil
            tmid=Label(daftarframe,text='No. ')
            tmjudul=Label(daftarframe,text='Nama Anggota')
            tmpengarang=Label(daftarframe,text='Alamat')
            tmtterbit=Label(daftarframe,text='No Hp')
            tmtgl=Label(daftarframe,text='Tanggal')
            ##Config
            tmid.grid(row=0,column=0,sticky=W)
            tmjudul.grid(row=0,column=1,sticky=W)
            tmpengarang.grid(row=0,column=2,sticky=W)
            tmtterbit.grid(row=0,column=3,sticky=W)
            tmtgl.grid(row=0,column=4,sticky=W)
            ##Perulangan Menampilkan DB
            for i in range(len(pengunjung)):
                for j in range(len(pengunjung[i])):
                    teks=Entry(daftarframe)
                    teks.grid(row=i+1,column=j)
                    teks.insert(END,pengunjung[i][j])
                    
        def statusbar():
            cur.execute('select * from data_anggota')
            anggota=cur.fetchall()
            infoFrame=Frame(statusFrame)
            infoFrame.pack(side=LEFT)
            tglframe=Frame(statusFrame)
            tglframe.pack(side=RIGHT,fill=BOTH)
            cur.execute('select * from data_buku')
            buku=cur.fetchall()
            Label(tglframe, text="Tanggal : "+tanggal()).pack()
            Label(infoFrame, text="Login Sebagai : "+datUser).pack(side=LEFT)
            Label(infoFrame, text="| Total Pengunjung : "+str(len(pengunjung))).pack(side=LEFT)
            Label(infoFrame, text="| Total Anggota : "+str(len(anggota))).pack(side=LEFT)
            Label(infoFrame, text="| Total Buku : "+str(len(buku))).pack(side=LEFT)
        def menulist():
            file = Menu(menubar, tearoff=0)
            file.add_command(label="About Us",command=aboutuswindow)
            file.add_command(label="Tambah Pengguna",command=tambahuserwindow)
            #file.add_command(label="Pengaturan")
            file.add_separator()
            file.add_command(label="Ganti Username",command=gantinamawindow)
            file.add_command(label="Ganti Password",command=gantipasswindow)
            file.add_command(label="Log Out",command=logout)
            file.add_command(label="Keluar",command=Tutup)
            menubar.add_cascade(label="File", menu=file)
            buku = Menu(menubar, tearoff=0)
            buku.add_command(label="Tambah Buku", command=tambahbukuwindow)
            buku.add_command(label="Lihat Daftar Buku", command=daftarbukuwindow)
            buku.add_command(label="Cari Buku",command=caribukuwindow)
            buku.add_separator()
            buku.add_command(label="Lihat Peminjaman Buku",command=lihatpinjamanwindow)
            buku.add_command(label="Lihat Pengembalian Buku",command=kembalianbukuwindow)
            menubar.add_cascade(label="Kelola Buku", menu=buku)
            anggota = Menu(menubar, tearoff=0)
            anggota.add_command(label="Tambah Anggota", command=tambahanggotawindow)
            anggota.add_command(label="Lihat daftar Anggota", command=daftaranggotawindow)
            anggota.add_command(label="Cari Anggota",command=carianggotawindow)
            menubar.add_cascade(label="Kelola Anggota", menu=anggota)
            bantuan = Menu(menubar, tearoff=0)
            bantuan.add_command(label="Bantuan",command=bantuanwindow)
            bantuan.add_separator()
            bantuan.add_command(label="Tentang Aplikasi",command=tentangwindow)
            menubar.add_cascade(label="Bantuan", menu=bantuan)
            root.config(menu=menubar)
        menulist()
        judul()
        tombol()
        isi()
        statusbar()
    def init():
        lebar = 850
        tinggi = 525
        setTengahX = (root.winfo_screenwidth()-lebar)//2
        setTengahY = (root.winfo_screenheight()-tinggi)//2
        root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        root.title=(title)
        root.protocol("WM_DELETE_WINDOW", Tutup) 
        #self.parent.resizable(False, False)
        komponen()
    init()
##============================================##
## Preparing System ##
##============================================##    

##============================================##
##Menghubungkan Databases
##============================================##

print(' ')
print(waktu()+' - '+'Connecting to Database...')
global status
try :
    con = db.connect(db="proyek", user="root", passwd="",host="localhost",port=3306,autocommit=True);
    cur = con.cursor()
    cur.execute('select * from admin')
    print(waktu()+' - '+'Connected to Localhost Server...')
    print(' ')
    print('=========================================')
    print(waktu()+' - '+'Starting Log Service...')
    print('=========================================')
    print(' ')
    print('=========================================')
    print('Tanggal di Server : '+str(tanggal()))
    print('=========================================')
    print(' ')
    Main()
    mainloop()
    status=1
except :
    print(waktu()+' - '+'Failed to Localhost Server...')
    mb.showerror("Error!!","Gagal menghubungkan ke Database\nCek kembali koneksi anda..!!",parent=Main())
       
    status=0
