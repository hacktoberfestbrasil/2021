class Hewan (nama: String, berat: Float, berbulu: Boolean, umur: Int) {

     val nama: String
     val weight: Float
     val berbulu: Boolean
     val umur: Int

     init {
         this.nama = nama
         this.weight = if (berat <= 0) 0.1F else berat
         this.berbulu = berbulu
         this.umur = if (umur < 0) 0 else umur
     }

     fun info(){
         println("Nama: $nama \nBerat: $weight \nHewan Berbulu: $berbulu \nUmur: $umur")
     }
}

fun main(){
   val beta = Hewan("empus", 2.4F,true,1)
   beta.info()
}
