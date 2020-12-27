document.addEventListener("DOMContentLoaded",function (){
    Dr_rate=document.querySelector("#Dr_rate");
    Num_Dr_rate=document.querySelector("#Num_of_rates")
    rate_btn=document.querySelectorAll(".btn-rate")
    rate_btn.forEach(element => {
        Get_dr=element.getAttribute("data-btn_id");
        element.addEventListener("click",function(){
            
            btn_value=element.getAttribute("data-value");
            form= new FormData();
            form.append("value", btn_value);
            fetch(`Rate_Dr/${Get_dr}`,{
                method:"POST",
                body:form,
            })
            .then((res)=>res.json())
            .then((res) =>{
                Dr_rate.textContent=res.rate
                Num_Dr_rate.textContent=res.num_of_rates
            })
            document.getElementById("btn-1").disabled=true;
            document.getElementById("btn-2").disabled=true;
            document.getElementById("btn-3").disabled=true;
            document.getElementById("btn-4").disabled=true;
            document.getElementById("btn-5").disabled=true;
        })
    });
})