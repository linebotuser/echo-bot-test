from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    FlexMessage,
    FlexBubble,
    FlexImage,
    FlexMessage,
    FlexBox,
    FlexText,
    FlexIcon,
    FlexButton,
    FlexSeparator,
    FlexContainer,
    URIAction,
    Emoji,
    VideoMessage,
    AudioMessage,
    LocationMessage,
    StickerMessage,
    ImageMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
import json
import os
app = Flask(__name__)

configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
line_handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'
@line_handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    text = event.message.text
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
#------------------------------------------------------------------------------------------------------------------------------以下中文版 
        if text == '大溪節趣':#中文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                )
            )
        elif text == 'DIY體驗活動':#大溪節趣/DIY
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )

            
#==================================================================================================================================
        elif text == '溪光之旅':#中文richmenu介面1
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == '我想去!':#溪光之旅/2p
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '我想吃!':#溪光之旅/2p
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '我想住!':#溪光之旅/2p
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
#====================================================================================================================================            
        elif text == '溪遊記':#中文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == '體驗新事物':#溪遊記/心理測驗/體驗新事物
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == '參加傳統的文化活動':#溪遊記/心理測驗/體驗新事物/參加傳統的文化活動
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == '參加自然景觀之旅':#溪遊記/心理測驗/體驗新事物/參加自然景觀之旅
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '待在熟悉地方':#溪遊記/心理測驗/待在熟悉地方
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == '適當獨旅放鬆身心':#溪遊記/心理測驗/待在熟悉地方/適當獨旅放鬆心情
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '與親人出遊共度溫馨時光':#溪遊記/心理測驗/待在熟悉地方/與親人出遊共度溫馨時光
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
#=====================================================================================================================================================
        elif text == '玩轉大溪':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="https://aaaaerggngoi.my.canva.site/")]
                )
            )
        
        
#------------------------------------------------------------------------------------------------------------------------------以下日文版            
        elif text == '季節の活動':#日文richmenu介面/大溪節趣
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == 'DIY体験活動':#大溪節趣/DIY日文版
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
#=====================================================================================================================================    
        elif text == '溪の観光地':#日文richmenu介面/溪光之旅
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '行きたいです!':#溪光之旅/2part
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )    
#==========================================================================================================================================
        elif text == '渓遊記':#日文richmenu介面/溪遊記
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == '新しいことを体験する':#日文richmenu介面/溪遊記/新しいことを体験する
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == '伝統的な文化活動に参加する':#日文richmenu介面/溪遊記/伝統的な文化活動に参加する
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == '慣れた場所で過ごす':#日文richmenu介面/溪遊記/慣れた場所で過ごす
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == '自然景観の旅に出かける':#日文richmenu介面/溪遊記/自然景観の旅に出かける
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '一人旅で心身をリフレッシュ':#日文richmenu介面/溪遊記/一人旅で心身をリフレッシュ
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '家族と一緒に温かい時間を過ごす':#日文richmenu介面/溪遊記/家族と一緒に温かい時間を過ごす
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
#======================================================================================================
        elif text == '大溪を遊び尽くす':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="https://aaaaaffffu.my.canva.site/")]
                )
            )
#------------------------------------------------------------------------------------------------------------------------------以下英文版
        elif text == 'SeasonalEvents':#英文richmenu介面/大溪節趣
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == 'DIYExperienceActivities':#大溪節趣/DIYu英文版    
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
#====================================================================================================================================         
        elif text == 'DaxiAttractions':#英文richmenu介面/溪光之旅
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == 'Iwnattogo!':#溪光之旅/2p英文版
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
           
        elif text == 'PlayAroundDaxi':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="https://aaaaaffffu.my.canva.site/sssuuuyyy")]
                )
            )
        
#===============================================================================================================================================================       
        elif text == 'DaxiTravelogue':#英文richmenu介面/溪遊記1111111111
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == 'Experiencingnewthings':#英文richmenu介面/溪遊記/2222222222222
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == 'Joinculturalactivities':#英文richmenu介面/溪遊記/333333333333
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == 'Goonanaturallandscapetour':#英文richmenu介面/溪遊記/3333333333333
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == 'Relaxonasolotrip':#英文richmenu介面/溪遊記/3333333333333333333
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == 'Enjoywarmmomentswithfamily':#英文richmenu介面/溪遊記/33333333333333333
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == 'Stayinginfamiliarplaces':#英文richmenu介面/溪遊記/2222222222222222
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
#-------------------------------------------------------------------------------------------------------------------------FOR TEST USE
        elif text == 'Test':
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )  
            
        elif text == '我想了解大溪觀光季節':
            # 靜態圖片 URL
            url = f"{request.url_root.rstrip('/')}/static/22.jpg"
            app.logger.info("Generated URL: " + url)
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        ImageMessage(original_content_url=url, preview_image_url=url),
                        TextMessage(text="關於大溪觀光季節\n可以點擊下列連結獲取更多資訊:\nhttps://www.tycg.gov.tw/ActiveMonthList.aspx?n=8&sms=7883#")
                    ]
                )
            )
        elif text == 'DaxiTourismSeason':
            url = f"{request.url_root.rstrip('/')}/static/11.jpg"
            app.logger.info("Generated URL: " + url)
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        ImageMessage(original_content_url=url, preview_image_url=url),
                        TextMessage(text="About the Daxi sightseeing season. More information can be found at the following link:\nhttps://www.tycg.gov.tw/ActiveMonthList.aspx?n=8&sms=7883#")
                    ]
                )
            )
        elif text == '大渓観光シーズン':
            url = f"{request.url_root.rstrip('/')}/static/33.jpg"
            app.logger.info("Generated URL: " + url)
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        ImageMessage(original_content_url=url, preview_image_url=url),
                        TextMessage(text="大渓観光シーズンについて。 詳細については、次のリンクを参照してください:\nhttps://www.tycg.gov.tw/ActiveMonthList.aspx?n=8&sms=7883#")
                    ]
                )
            )
        elif text == 'Podcast':#英文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '心理測驗':#英文richmenu介面/溪遊記/3333333333333333333
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == 'PersonalityTest':#英文richmenu介面/溪遊記/3333333333333333333
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '心理テスト':#英文richmenu介面/溪遊記/3333333333333333333
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
           
        else:
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=event.message.text)]
                )
            )
            
if __name__ == "__main__":
    app.run()