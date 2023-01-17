//https://api.telegram.org/bot5638633198:AAHhjPxdjq6_XgaoKAqMUcxY9oMFf05SPxU/sendMessage?chat_id=-862216614&text=Halo%0AJuga&parse_mode=html

//Nama%20%3A%20xxx%0ANomor%20WhatsApps%20%3A%20xxx%0AEmail%20%3A%20xxx%0AMobil%20%3A%20xxx%0ATanggal%20%3A%20xxx%0APengemudi%20%3A%20xxx%0ALokasi%20Penjemputan%20%3A%20xxx%0ALokasi%20Tujuan%20%3A%20xxx%0A

function kirimPesan() {
  var nama = document.getElementById("nama");
  var wa = document.getElementById("wa");
  var email = document.getElementById("email");
  var mobil = document.getElementById("mobil");
  var tanggal = document.getElementById("tanggal");
  var sopir = document.getElementById("sopir");
  var lokasi_penjemputan = document.getElementById("lokasi_penjemputan");
  var lokasi_tujuan = document.getElementById("lokasi_tujuan");

  var gabungan =
    "Ada%20pesanan%20masuk%20!%0ASegera%20konfirmasi%20!%0A%0A" +
    "Nama%20%3A%20" +
    nama.value +
    "%0ANomor%20WhatsApps%20%3A%20" +
    wa.value +
    "%0AEmail%20%3A%20" +
    email.value +
    "%0AMobil%20%3A%20" +
    mobil.value +
    "%0ATanggal%20%3A%20" +
    tanggal.value +
    "%0APengemudi%20%3A%20" +
    sopir.value +
    "%0ALokasi%20Penjemputan%20%3A%20" +
    lokasi_penjemputan.value +
    "%0ALokasi%20Tujuan%20%3A%20" +
    lokasi_tujuan.value;

  var token = "5638633198:AAHhjPxdjq6_XgaoKAqMUcxY9oMFf05SPxU";
  var grub = "-862216614";
  var kontak = "";

  $.ajax({
    url: `https://api.telegram.org/bot${token}/sendMessage?chat_id=${grub}&text=${gabungan}&parse_mode=html`,
    method: `POST`,
  });
}
