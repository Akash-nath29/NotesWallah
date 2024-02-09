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

// Profile Links List
let btn = document.getElementById("profile-pic");
let profile_links = document.getElementById("profile-links");

profile_links.style.maxHeight = '0px';

btn.addEventListener('click', () => {
    if (profile_links.style.maxHeight == '0px') {
        profile_links.style.maxHeight = '500px';
    }
    else {
        profile_links.style.maxHeight = '0px';
    }
})