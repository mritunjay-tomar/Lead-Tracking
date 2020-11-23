function RedirectToURL(url) {
    window.location = url
}

function MarkArchive() {
    var message = [];
    $("#HomeStudentTable input[type=checkbox]:checked").each(function () {
        var row = $(this).closest("tr")[0];
        message.push(row.cells[0].innerHTML);
    });
    if (message.length > 0) {
        var URL = $("#ArchiveURL").attr("data-url");
        URL = URL.concat("?studentIDs=");
        for (var i=0;i<message.length;i++) {
            if (i == 0) {
                URL = URL.concat(message[i])
            }
            URL = URL.concat("&".concat(message[i]));
        }
        RedirectToURL(URL);
    }
    else {
        alert("Please select student's to mark archive");
    }
}

function RemoveStudentFromArchive() {
    var message = [];
    $("#HomeStudentTable input[type=checkbox]:checked").each(function () {
        var row = $(this).closest("tr")[0];
        message.push(row.cells[0].innerHTML);
    });
    if (message.length > 0) {
        var URL = $("#RemoveArchiveURL").attr("data-url");
        URL = URL.concat("?studentIDs=");
        for (var i=0;i<message.length;i++) {
            if (i == 0) {
                URL = URL.concat(message[i])
            }
            URL = URL.concat("&".concat(message[i]));
        }
        RedirectToURL(URL);
    }
    else {
        alert("Please select student's to remove from archive records");
    }
}