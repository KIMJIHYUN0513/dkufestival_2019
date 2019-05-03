const livestream = document.querySelector('.livestream');
const NewestPost = "{{NewestPost}}";


function loadLivestream(NewestPost) {
    console.log(NewestPost);
    setTimeout((NewestPost) => {
        livestream.innerText = NewestPost;
    }, 1000);
}





function init() {
    loadLivestream();
}


init();