function animation() {
    var elem = document.getElementById("frame"); 
    var pos = 0;
    var id = setInterval(frame, 5);
    function frame() {
        if (pos == 350) {
            clearInterval(id);
        } else {
            pos--; 
            elem.style.left = pos + 'px'; 
        }
    }
}