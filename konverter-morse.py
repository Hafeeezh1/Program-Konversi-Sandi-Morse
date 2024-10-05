# Dictionary untuk mapping huruf ke kode Morse
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', 
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Reverse dictionary untuk decoding Morse ke teks
reverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

# Fungsi untuk mengubah teks menjadi kode Morse
def teks_ke_morse(teks):
    morse_code = ''
    for huruf in teks.upper():
        if huruf in morse_code_dict:
            morse_code += morse_code_dict[huruf] + ' '
        else:
            morse_code += '? '  # Jika karakter tidak dikenali
    return morse_code.strip()

# Fungsi untuk mengubah kode Morse menjadi teks
def morse_ke_teks(morse):
    teks = ''
    morse_kata = morse.split(' ')
    for kode in morse_kata:
        if kode in reverse_morse_code_dict:
            teks += reverse_morse_code_dict[kode]
        else:
            teks += '?'  # Jika kode Morse tidak dikenali
    return teks

# Program utama
while True:
    print("\nAplikasi Konversi Teks - Morse")
    print("1. Ubah teks menjadi kode Morse")
    print("2. Ubah kode Morse menjadi teks")
    print("3. Keluar")
    pilihan = input("Pilih opsi (1/2/3): ")

    if pilihan == '1':
        teks = input("Masukkan teks: ")
        hasil = teks_ke_morse(teks)
        print(f"Kode Morse: {hasil}")
    elif pilihan == '2':
        morse = input("Masukkan kode Morse (gunakan spasi antar huruf, '/' untuk spasi antar kata): ")
        hasil = morse_ke_teks(morse)
        print(f"Teks: {hasil}")
    elif pilihan == '3':
        print("Terima kasih telah menggunakan aplikasi ini!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")