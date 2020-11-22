{% load static %}

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
        var URL = "";
        for (var i=0;i<message.length;i++) {
            if (i == 0) {
                URL.concat(message[i]);
            }
            URL.concat("&".concat(message[i]));
        }
        RedirectToURL("{% url 'Recruiter:mark-student-archive' %}?studentIDs=".concat(URL));
    }
    else {
        alert("Please select student's to mark archive");
    }
}