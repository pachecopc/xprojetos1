
const elValue = document.querySelector(".value")
const elBtn = document.querySelector(".btn")
const elNotasCem = document.querySelector(".notasCem")
const elNotasCinquenta = document.querySelector(".notasCinquenta")
const elNotasDez = document.querySelector(".notasDez")
const elReset = document.querySelector("reset")

elBtn.addEventListener("click", (event) =>{
 event.preventDefault()

 elNotasCem.textContent =""
 elNotasCinquenta.textContent =""
 elNotasDez.textContent =""

 const value = Number(elValue.value)

 if(value == "" || isNaN(value)){
   alert("Informe um número!:)")
   return
 }

 if(value % 10 != 0 ){
     alert("nao tem nota")
     elNotasCem.classList.add("none")
     elNotasCinquenta.classList.add("none")
     elNotasDez.classList.add("none")
     
     
    
     return
 }

 const notasCem = parseInt(value / 100)
 let resto = value % 100
 const notasCinquenta = parseInt(resto / 50)
 resto = resto % 50
 const notasDez = parseInt(resto / 10)

 elNotasCem.classList.add("none")
 elNotasCinquenta.classList.add("none")
 elNotasDez.classList.add("none")

if(notasCem > 0){
 elNotasCem.classList.remove("none")
 elNotasCem.textContent = notasCem + " Notas de 100,00"
}

if(notasCinquenta > 0){
 elNotasCinquenta.classList.remove("none")
 elNotasCinquenta.textContent = notasCinquenta + " Notas de 50,00"
}

if(notasDez > 0){
 elNotasDez.classList.remove("none")
 elNotasDez.textContent = notasDez + " Notas de 10,00"
}

})