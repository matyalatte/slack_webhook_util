import requests, json

class SlackWebhook:
    def __init__(self, url):
        self.url=url

    def notify(self, message):
        if message=="" or (type(message) is not str):
            raise ValueError("'message' should be a string of more than one character!")

        payload = {
            'text': message
        }

        r = requests.post(self.url, data=json.dumps(payload))

#テスト用
if __name__=="__main__":
    url="ここにWebhook URLを記入する"

    slack_webhook = SlackWebhook(url)

    slack_webhook.notify("テストだよ")

        