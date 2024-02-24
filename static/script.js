const noRefresh = (e) => {
    e.preventDefault();
};
function downloadNote() {
    var topic = document.querySelector('#topic').value;
    var classNotesContent = document.querySelector('.generated-notes').innerText;
    var blob = new Blob([classNotesContent], { type: 'text/plain' });
    var url = window.URL.createObjectURL(blob);
    var link = document.createElement('a');
    link.download = `${topic}notes.txt`;
    link.href = url;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    window.URL.revokeObjectURL(url);
}

const openNotes = () => {
    document.querySelector("#music").style.display = "none";
    document.querySelector("#notes").style.display = "grid";
}
const openMusic = () => {
    document.querySelector("#notes").style.display = "none";
    document.querySelector("#music").style.display = "grid";
}

<<<<<<< HEAD
// Nav Bar open close
const hamburgerBtn = document.querySelector('#hamburger');
const navBar = document.querySelector('.nav-links');

if (window.innerWidth < 600) {
    navBar.style.display = "none";
}
else {
    navBar.style.display = "flex";
}

// navBar.style.display = "none";

hamburgerBtn.addEventListener('click', () => {
    if (navBar.style.display == "none") {
        navBar.style.display = "flex";
    } else {
        navBar.style.display = "none";
    }
});
=======
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
>>>>>>> cb89d8ca93c1c8e05f15145a02dded4664d066c0
