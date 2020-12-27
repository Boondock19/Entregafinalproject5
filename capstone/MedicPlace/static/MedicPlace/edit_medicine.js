document.addEventListener("DOMContentLoaded",function(){
    edit_btn=document.querySelector("#edit-btn");
    medicine_id=edit_btn.getAttribute("data-Medicine-id");
    edit_form=document.querySelector(".edit-medicine");
    // Selecting edit inputs
    edit_name=document.querySelector(`#input-name-${medicine_id}`);
    edit_textarea=document.querySelector(`#textarea-${medicine_id}`);
    edit_Active_ingredient=document.querySelector(`#input-Active_ingredient-${medicine_id}`);
    edit_select=document.querySelector(`#input-type_medicine-${medicine_id}`);
    // Selecting page p tags
    p_name=document.querySelector(`#h1-name`);
    p_type=document.querySelector(`#p-type`);
    p_active_ingredient=document.querySelector(`#p-active_ingredient`);
    p_summary=document.querySelector(`#p-summary`);
    p_summary_edited=document.querySelector("#p-summary-edited")
    // Eventlistener edit btn
    edit_btn.addEventListener("click",function(){
        if (edit_btn.textContent=="Edit Entry"){
            edit_btn.textContent="Save Entry"
            // hidding p tags
            p_name.style.display="none";
            p_type.style.display="none";
            p_active_ingredient.style.display="none";
            p_summary.style.display="none";
            // showing edit fields
            edit_name.style.display="block";
            edit_form.style.display="block";
            edit_textarea.style.display="block";
            edit_Active_ingredient.style.display="block";
            edit_select.style.display="block";
        } else if (edit_btn.textContent=="Save Entry"){
            edit_name_edited=edit_name.value;
            summary_edited=edit_textarea.value;
            active_ingredient_edited=edit_Active_ingredient.value;
            type_medicine_edited=edit_select.value;
            edit_entry(medicine_id,edit_name_edited,type_medicine_edited,active_ingredient_edited,summary_edited)
            // hiding edit fields
            edit_name.style.display="none"
            edit_form.style.display="none";
            edit_textarea.style.display="none";
            edit_Active_ingredient.style.display="none";
            edit_select.style.display="none";
            // showing p tags
            p_name.style.display="block"
            p_type.style.display="block";
            p_active_ingredient.style.display="block";
            p_summary_edited.style.display="block";
            edit_btn.textContent="Edit Entry";
        }
    })
})

function edit_entry(id,name,type_medicine,active_ingredient,summary) {
    form= new FormData
    form.append("type_medicine",type_medicine)
    form.append("active_ingredient",active_ingredient)
    form.append("summary",summary)
    form.append("name",name)
    fetch(`/Edit_Medicine/${id}`,{
        method:"POST",
        body:form
    })
    .then((res) => res.json())
    .then((res) =>{
        p_name.textContent=res.name
        p_type.textContent=res.type_of_medicine;
        p_active_ingredient.textContent=res.active_ingredient;
        p_summary_edited.textContent=res.summary;
    })
}