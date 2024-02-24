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