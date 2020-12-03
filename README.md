# slack_webhook_util
utils for slack webhook<br>
<br>
<img src="https://raw.githubusercontent.com/matyalatte/slack_webhook_util/main/image.png" width="320px"><br>
SlackのIncoming Webhookでメッセージを送るためのスクリプトです。<br>
スクリプトの実行状況等を通知するために作成しました。<br>
テキストの送信のみに対応したシンプルなスクリプトとなっています。<br>
<br>
※LINE Notifyでも同様の通知が行えます。LINE Notyfy用のスクリプトは<a href="https://github.com/matyalatte/line_notify_util">こちら</a><br>

## ファイル一覧
- slack_webhook.py: python用のスクリプト。SlackWebhook("Webhook URL").notify("文字列")でメッセージを送れる。
- slack_webhook.gs: GAS用のスクリプト。slack_webhook_notify("文字列")でメッセージを送れる。URLにWebhook URLを記入して使う。
- slack_webhook.bat: curlでSlackにメッセージを送る
<br>

## Incoming Webhookの使い方について
Webhook URLの取得方法等、Incoming Webhookの使い方については以下のサイトを参考にしてください。<br>
<a href="https://qiita.com/ik-fib/items/b4a502d173a22b3947a0">
SlackのIncoming Webhooksを使い倒す - Qiita
</a>
