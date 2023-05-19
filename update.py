import os,sys



Dvanmeploph = """
cd $HOME
cd DARK-FB
mv data $HOME
mv results $HOME
cd
rm -rf DARK-FB
git clone https://github.com/Itsmeafriliyan/DARK-FB
cd $HOME
mv data DARK-FB
mv results DARK-FB
cd DARK-FB
"""

print(" |-->Tunggu Sebentar Sedang Update Script....")
os.system(Dvanmeploph)
print(' |')
print(' |')
print(' |-->Update Script Sudah Selesai...')
print(' |-->Silahkan Jalankan Perintah Ini : python main.cpp')
os.sys.exit()
