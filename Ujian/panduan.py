class PanduanDaurUlang:
    def __init__(self):
        # Inisialisasi atribut panduan
        self.panduan = {
            "Plastik": "Cuci bersih dan pisahkan plastik keras dan lunak.",
            "Kertas": "Pisahkan kertas berminyak atau basah.",
            "Kaca": "Pisahkan kaca dari material lainnya.",
            "Logam": "Cuci bersih logam sebelum didaur ulang.",
            "Organik": "Gunakan untuk membuat kompos."
        }

    def tampilkan_panduan(self):
        # Pastikan atribut self.panduan digunakan di sini
        panduan_str = ""
        for jenis, tips in self.panduan.items():
            panduan_str += f"### {jenis}\\n- {tips}\\n\\n"
        return panduan_str
