
function changeFile(elem) {
    console.log('changeFile', elem, this);
    let files = elem.files;
    if (files.length == 0) {
        return;
    }
    let name = files[0].name;
    console.log('name', name);
    let elemFileName = document.getElementById('file-name');
    if (elemFileName) {
        elemFileName.innerHTML = name; 
    }
}
