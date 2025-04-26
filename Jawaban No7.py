def tentukan_usia(umur):
  """
  Menentukan kategori usia berdasarkan input umur.

  Args:
    umur: Umur seseorang (integer).

  Returns:
    Kategori usia ("Anak-anak", "Remaja", "Dewasa", atau "Lansia").
    Mengembalikan pesan error jika input bukan angka atau negatif.
  """
  try:
    umur = int(umur)  # Mengubah input ke integer
    if umur < 0:
      return "Umur tidak boleh negatif."
    elif umur < 12:
      return "Anak-anak"
    elif umur < 18:
      return "Remaja"
    elif umur < 60:
      return "Dewasa"
    else:
      return "Lansia"
  except ValueError:
    return "Input harus berupa angka."

# Contoh penggunaan
input_umur = input("Masukkan umur: ")
kategori = tentukan_usia(input_umur)
kategori
