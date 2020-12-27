document.addEventListener("DOMContentLoaded",function(){
    get_comment=document.querySelector("#edit-comment");
    get_comment_id=get_comment.getAttribute("data-comment-id");
    comment_content=document.querySelector(`#comment-content-${get_comment_id}`);
    comment_textarea=document.querySelector(`#comment-textarea-${get_comment_id}`);
    comment_content_edit=document.querySelector(`#edit-comment-content-${get_comment_id}`)
    get_comment.addEventListener("click",function(){
        if (get_comment.textContent=="Edit") {
            comment_content.style.display="none"
            comment_content_edit.style.display="none"
            comment_textarea.style.display="block"
            get_comment.textContent="Save"
        } else if (get_comment.textContent="Save") {
            content=comment_textarea.value
            edit_comment(get_comment_id,content)
            comment_content.style.display="none"
            comment_textarea.style.display="none"
            comment_content_edit.style.display="block"
            get_comment.textContent="Edit"
        }
        
        
    })
    
    function edit_comment(id,content){
        form= new FormData;
        form.append("content",content);
        fetch(`/Article_edit_comment/${id}`,{
            method:"POST",
            body:form,
        })
        .then((res) => res.json())
        .then((res) => {
            comment_content_edit.textContent=res.content
            
        })  
    }
    

})