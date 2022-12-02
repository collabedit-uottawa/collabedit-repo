
function applyEdit() {
    $.ajax({
        type: "POST",
        url: "~/editor.py",
        data: { param: "test"}
    }).done(function( o ) {
        // do something
    });
}

function trim() {
    var video = document.getElementById('video');
    video.src = "edits/videoTrim.mp4"
}

function qualityResize() {
    var video = document.getElementById('video');
    video.src = "edits/videoResize.mp4"
}

function qualitySpeed() {
    var video = document.getElementById('video');
    video.src = "edits/videoSpeed.mp4"
}

function changeAudio() {
    var video = document.getElementById('video');
    video.src = "edits/videoAudio.mp4"
}

function saving() {
    window.alert("Edits saved");
}

function loadVideo() {
    document.location.href = "video.html";
}
