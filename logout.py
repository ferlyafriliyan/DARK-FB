import os,sys



Dvanmeploph = """
cd $HOME
rm -rf $HOME/DARk-FB
termux-change-repo
git clone https://github.com/Dvanmeploph/DARK-FB
cd DARK-FB
"""

print(" |-->Tunggu Sebentar Sedang Update Script....")
os.system(Dvanmeploph)
print(' |')
print(' |')
print(' |-->Update Script Sudah Selesai...')
print(' |-->Silahkan Jalankan Perintah Ini : python run.py')
os.sys.exit()
