var updtaebtns = document.getElementsByClassName("update-cart")

for(i=0;i<updtaebtns.length;i++) {
    updtaebtns[i].addEventListener('click',function(){
        var itemid = this.dataset.item
        var action = this.dataset.action
        console.log('itemid :',itemid,'action :',action)
        updateuseritem(itemid,action)
    })
}




function updateuseritem(itemid,action){
    console.log('user is authenticated,sending data ..')

    var url='/updateitem/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'itemid':itemid,'action':action})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        location.reload
        console.log(`data :`,data)
    })
}