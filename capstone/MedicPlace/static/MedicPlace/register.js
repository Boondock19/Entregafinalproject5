document.addEventListener("DOMContentLoaded",function (){
    console.log("Cargo el scritp")
    Dr_yes=document.querySelector("#Yes_dr");
    Dr_no=document.querySelector("#No_dr");
    Dr_yes.addEventListener("click",function(){
        console.log("Entro en yes dr")
        document.querySelector("#Clinic_field1").style.display="block"
        document.querySelector("#Clinic_field2").style.display="block"
        document.querySelector("#Clinic_field3").style.display="block"
        document.querySelector("#Clinic_field4").style.display="block"
        
    })
    Dr_no.addEventListener("click",function(){
        console.log("Entro en no dr")
        document.querySelector("#Clinic_field1").style.display="none"
        document.querySelector("#Clinic_field2").style.display="none"
        document.querySelector("#Clinic_field3").style.display="none"
        document.querySelector("#Clinic_field4").style.display="none"
    }) 
})