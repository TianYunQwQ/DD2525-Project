/*
	Citation: https://developer.chrome.com/docs/extensions/mv3/getstarted/
			: https://developer.chrome.com/docs/extensions/mv3/messaging/
*/

chrome.runtime.onConnect.addListener(function(port){
	chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
		let url = tabs[0].url;

		// 发送当前URL给内容脚本
		let postmsg = {"url": url};
		port.postMessage(postmsg);
		
		// 设置地理位置权限为允许
		// Citation: https://chrome-apps-doc2.appspot.com/extensions/contentSettings.html
    	chrome.contentSettings['location'].set({
            primaryPattern: '<all_urls>',
            setting: 'allow'
        });
	}); //query
});

