function confirmBeforeDelete(url) {
    var action = confirm ("Please confirm deleting the student");
    if (action == true) {
        RedirectToURL(url);
    }
}

function RedirectToURL(url) {
    window.location = url
}