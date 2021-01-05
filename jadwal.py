import time
import random
import os


os.system('clear')

nanya = ("\033[0;36mLIAT JADWAL DAN TUGASMU\033[0m")
print(nanya.center(106,'='))
tugas =("""
	\033[0;32mbuat jadwal tugasmu!\033[0m (ex: tugas)""")
print(tugas)
hari = ("""
	\033[0;32mliat jadwal sekarang\033[0m(ex: nama hari ini)""")
print(hari)
print '\n'
choice = raw_input ("\033[33;1minput your choice: \033[0m\033[0;32m")

print '\n'
if choice == ("senin"):
	print "\033[0;36m=====================\033[0m\033[0;32m\033[0;32m |\033[0m jadwal hari \033[33;1m SENIN \033[0m  adalah sebagai berikut \033[0;32m |\033[0m\033[0;36m=====================\033[0m"
	print("""
		pukul \033[0;32m 07:00\033[0m  ---> MATEMATIKA (U)
		pukul \033[0;32m 08:00\033[0m  ---> B. INGGRIS
		pukul \033[0;32m 09:30\033[0m  ---> PKWU
		pukul \033[0;32m 10:30\033[0m ---> B. JAWA""")
	print '\n'
	time.sleep(2)
	senin1 = ['kamu pasti bisa ayo semangat hari senin!! masih ada 4 hari lagi', 'aku tau kamu bosan belajarlah dan kamu akan tau bahwa sukses itu tak pernah bosan', 'semangat buat kamu yang pjj, semoga cepet kelar tugasnya yahh', 'senin itu asyik lohh, jangan di buat pusing rilex aja yah']
	print("\033[0;36mmotivasi hari ini: \033[0m" +random.choice(senin1))
	print '\n'
elif choice == ("selasa"):
	print "\033[0;36m=====================\033[0m\033[0;32m\033[0;32m |\033[0m jadwal hari \033[33;1m SELASA \033[0m  adalah sebagai berikut \033[0;32m |\033[0m\033[0;36m=====================\033[0m"
	print("""
		pukul \033[0;32m 07:00\033[0m ---> MATEMATIKA (P)
		pukul \033[0;32m 08:00\033[0m ---> B. INDONESIA
		pukul \033[0;32m 09:30\033[0m ---> SENI BUDAYA
		pukul \033[0;32m 10:30\033[0m ---> EKONOMI""")
	print '\n'
	time.sleep(2)
	selasa1 = ['yeay tinggal 3 hari lagi ko. ga kerasa yah cepet banget', 'TETAP SEMANGT!!!', 'kamu tuh kuat. iyah kamu', 'coba deh jangan terlalu fokus kpd satu hal', 'buat sesuatu yang menarik pasti kamu akan bahagia']
	print("\033[0;36mmotivasi hari ini: \033[0m" +random.choice(selasa1))
	print '\n'
elif choice == ("rabu"):
	print "\033[0;36m=====================\033[0m\033[0;32m\033[0;32m |\033[0m jadwal hari \033[33;1m RABU \033[0m  adalah sebagai berikut \033[0;32m |\033[0m\033[0;36m=====================\033[0m"
	print("""
		pukul \033[0;32m 07:00\033[0m ---> FISIKA
		pukul \033[0;32m 08:00\033[0m ---> PAI
		pukul \033[0;32m 09:30\033[0m ---> S. INDONESIA
		pukul \033[0;32m 10:30\033[0m ---> PPKN""")
	print '\n'
	time.sleep(2)
	rabu1 = ['YEAYYY.. tinggal 2 hari. wahh kamu kuat yah', 'jangan kasih kendor', 'sukses masih diatas maka buatlah sukses itu ada di depanmu', 'jaga kesehatan yahh']
	print("\033[0;36mmotivasi hari ini: \033[0m" +random.choice(rabu1))
	print '\n'
elif choice == ("kamis"):
	print "\033[0;36m=====================\033[0m\033[0;32m\033[0;32m |\033[0m jadwal hari \033[33;1m KAMIS \033[0m  adalah sebagai berikut \033[0;32m |\033[0m\033[0;36m=====================\033[0m"
	print("""
		pukul \033[0;32m 07:00\033[0m ---> PJOK
		pukul \033[0;32m 08:00\033[0m ---> KIMIA
		pukul \033[0;32m 09:30\033[0m ---> BIOLOGI
		""")
	print '\n'
	time.sleep(2)
	kamis1 = ['SEMANGAT TINGGAL 1 HARI LAGI LOHH', 'NAH ITU KAMU MAMPU', 'belajarlah seolah penderitaan akan membunuhmu!!!', 'BANGKIT, BERJUANG, GAPAI MIMPI MU', 'JANGAN SIA-SIAKAN APA YANG ORANG TUAMU BERI!']
	print("\033[0;36mmotivasi hari ini: \033[0m" +random.choice(kamis1))
	print '\n'
elif choice == ("jumat"):
	print "\033[0;36m=====================\033[0m\033[0;32m\033[0;32m |\033[0m jadwal hari \033[33;1m JUMAT \033[0m  adalah sebagai berikut \033[0;32m |\033[0m\033[0;36m=====================\033[0m"
	print("""
		pukul \033[0;32m 07:00\033[0m ---> BK
		pukul \033[0;32m 08:00\033[0m  ---> TIK
		""")
	print '\n'
	time.sleep(2)
	jumat1 = [' UDAH DI UJUNG HARI NIH, BESOK SIAP-SIAP REFRESHING YAHH', 'HORREY', 'INI ADALAH HARI MEMBAHAGIAKAN LOHH', 'ISTIRAHAT YANG CUKUP, DAN JANGAN LUPA AKAN KE SUKSESANMU YAHH', 'KAMU ADALAH ORANG KUAT DALAM MENTAL, YA KAMU JUGA HARUS YAKIN']
	print("\033[0;36mmotivasi hari ini: \033[0m" +random.choice(jumat1))

	print '\n'

elif choice == ("tugas") :
	print "\033[33;1m coming soon\033[0m "
else:
	print "\033[31;1m no choice definied\033[0m"
	print '\n'


