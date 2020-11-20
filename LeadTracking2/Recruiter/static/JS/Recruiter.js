function MarkArchive() {
    var message = [];
    $("#HomeStudentTable input[type=checkbox]:checked").each(function () {
        var row = $(this).closest("tr")[0];
        message.push(row.cells[0].innerHTML);
    });
    if (messages.length > 0) {
        for (car i=0;i<messages.length;i++) {
            console.log(messages[i]);
        }
    }
    else {
        alert("Please select student's to mark archive")
    }
}