import os,sys



Denventa = """
cd $HOME
cd DARK-KACHYUSA
mv data $HOME
mv results $HOME
cd
rm -rf DARK-KACHYUSA
git clone https://github.com/Denventa/DARK-KACHYUSA
cd $HOME
mv data DARK-KACHYUSA
mv results DARK-KACHYUSA
cd DARK-KACHYUSA
"""

print(" |-->Tunggu Sebentar Sedang Update Script....")
os.system(Denventa)
print(' |')
print(' |')
print(' |-->Update Script Sudah Selesai...')
print(' |-->Silahkan Jalankan Perintah Ini : python run.py')
os.sys.exit()
