var URL = "ここにWebhook URLを記入する"
  
function slack_webhook_notify(m){
  var payload = {"text": m};
  
  var options =
   {
     "method"  : "post",
     "payload" : JSON.stringify(payload)
   };
 
   UrlFetchApp.fetch(URL, options);
}

function slack_test(){
    slack_webhook_notify("テストだよ");
}