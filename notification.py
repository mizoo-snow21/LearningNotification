import slackweb

def notification_learning_result(url, message, last_loss, last_accuracy) -> None:
    """
    学習結果を通知する。
    
    parameters
    ----------
    url : string
        通知するIncomigWebhooksのurl。
    message : string
        通知したい文章。
    last_loss : float
        最後のepochのloss。
    last_accuracy : float
        最後のepochのaccuracy。
    """
    slack = slackweb.Slack(url="Your IncomigWebfooks APIKey")
    blocks = [{
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "{} /n loss: {:.4f} /n accuracy: {:.4f}".format(message, last_loss, last_accuracy)
        },
        "accessory": {
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": "Click"
            },
            "value": "click_me_123",
            "url": "Your page url",
            "action_id": "button-action"
        }
    }]
    slack.notify(blocks = blocks)

