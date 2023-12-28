function openNote() {
    document.querySelector('#notes').style.display = "grid";
    document.querySelector('#music').style.display = "none";
}
function openMusic() {
    document.querySelector('#notes').style.display = "none";
    document.querySelector('#music').style.display = "grid";
}

// hamburger menu

let menu = document.getElementById("navLinks");
let hamburgerIcon = document.getElementById('hamburgerIcon');
// if (menu) {
//     menu.style.maxHeight = "0px";
// }
function openMenu() {
    if (menu.style.display == "none") {
        menu.style.display = "flex";
    } else {
        menu.style.display = "none";
    }
}