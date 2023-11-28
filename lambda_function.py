# -*- coding: utf-8 -*-
"""
Date: 2023/11/14
Author: @1chooo(Hugo ChunHo Lin)
E-mail: hugo970217@gmail.com
Version: v0.1.0
"""

import os
import json
from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.models import MessageEvent
from linebot.models import TextMessage
from linebot.models import ImageMessage
from linebot.models import TextSendMessage
from linebot.models import ImageSendMessage
from linebot.models import VideoSendMessage
from linebot.exceptions import InvalidSignatureError

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

def lambda_handler(event, context):
    @handler.add(MessageEvent, message=TextMessage)
    def handle_text_message(event):

        event_text = event.message.text

        if event_text == "Hello":
            reply_messages = [
                TextSendMessage(
                    text=f'World'
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想知道 AWS 創辦故事":
            reply_messages = [
                TextSendMessage(
                    text=f'當然！AWS（Amazon Web Services）是由亞馬遜公司於2006年推出的雲端運算平台。創辦人Jeff Bezos意識到雲端運算的巨大潛力，於是啟動了AWS的發展。AWS最初的目標是為企業提供可靠、可擴展、經濟實惠的雲端解決方案。這個決策後來改變了整個科技業的格局，使得任何人都能夠在全球運行低成本的應用程序，可見Jeff Bezos的願景和堅持對AWS的成功起到了關鍵作用！'
                ),
                TextSendMessage(
                    text=f'AWS的創辦故事始於2003年，當時亞馬遜公司的Jeff Bezos意識到他們在建設強大的內部基礎設施方面取得了不錯的進展！而這個基礎設施可以成為一個強大的雲端運算平台，能夠為其他企業提供服務。於是在2006年，AWS正式推出，開始提供雲端服務。AWS的成功與其開放性、靈活性和不斷創新的企業文化有關，而這一切都源於Jeff Bezos對技術和未來的敏銳洞察力。'
                ),
                TextSendMessage(
                    text=f'AWS的創辦故事始於2003年，當時亞馬遜公司內部建立了一個團隊，專注於改進其基礎設施。Jeff Bezos意識到這個內部基礎設施的潛力，可以成為一個革命性的雲端運算平台。在隨後的幾年中，這個團隊努力開發和改進AWS服務，並在2006年正式向公眾推出。AWS的創立使得企業能夠更有效地運行他們的應用程序，並在全球範圍內擁有更大的影響力。'
                ),
                TextSendMessage(
                    text=f'AWS的故事開始於2003年，當時亞馬遜公司的Jeff Bezos和他的團隊認識到他們所擁有的龐大基礎設施可以成為一個有力的雲端運算平台。在幾年的努力和創新後，他們於2006年推出了AWS，這個平台重新定義了企業和開發者如何運行應用程序的方式。而Jeff Bezos的願景是建立一個開放、可靠且可擴展的雲端解決方案，這種精神在AWS的成功中得到了完美的體現。'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/jeff_bezos.jpeg",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/jeff_bezos.jpeg",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想知道 AWS 提供的業務":
            reply_messages = [
                TextSendMessage(
                    text=f'當然！AWS（Amazon Web Services）提供多樣化的雲端運算服務，包括計算、儲存、資料庫、機器學習、人工智慧、物聯網、區塊鏈等。舉例來說，EC2提供虛擬伺服器，S3提供無限儲存空間，RDS提供受管理的資料庫服務，而AI服務如Lex和Polly則能讓你輕鬆整合語音和自然語言處理功能。AWS致力於為客戶提供完整、可擴展且高度安全的雲端解決方案。'
                ),
                TextSendMessage(
                    text=f'AWS 提供一系列豐富的雲端運算服務，包括運算、儲存、資料庫、機器學習、分析等多個領域。EC2允許您運行虛擬伺服器，S3提供可擴展的物件儲存，DynamoDB是一個高效能、全受管的NoSQL資料庫，而 SageMaker 則是一個強大的機器學習平台。AWS的服務範疇非常廣泛，能夠滿足各種不同業務需求。'
                ),
                TextSendMessage(
                    text=f'AWS 提供多元的雲端運算服務，以滿足不同產業的需求。這包括了計算、儲存、資料庫、機器學習、分析等領域。例如，Lambda允許您運行不需要管理伺服器的程式碼，Glacier提供低成本的長期儲存解決方案，而 Comprehend 則能夠分析文件中的自然語言。AWS不斷擴展其服務組合，以滿足客戶不斷演進的技術需求。'
                ),
                TextSendMessage(
                    text=f'AWS 提供全球最全面的雲端運算服務，覆蓋了基礎設施、應用程式和業務流程的方方面面。您可以使用EC2運行虛擬伺服器，透過S3輕鬆擴展儲存，使用RDS建立受管理的資料庫，還可以利用Athena進行資料查詢。AWS的多樣性和高度可靠性確保您可以找到符合您業務需求的解決方案。'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/aws_services.png",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/aws_services.png",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想知道 AWS 的16項領導力準則":
            reply_messages = [
                TextSendMessage(
                    text=f'AWS的領導力準則是他們企業文化的基石，共有16項準則。這包括「我們注重客戶的需求，並持續努力超越他們的期望」，以及「我們追求卓越，而不是接受現狀」。其他準則涵蓋了如何培養創新、擁抱變革、強調效率等價值觀。這些準則體現了AWS對於追求卓越和客戶滿意度的承諾。'
                ),
                TextSendMessage(
                    text=f'AWS的16項領導力準則是塑造他們文化的核心價值觀。其中包括「我們注重客戶的需求，並不斷努力超越他們的期望」，以及「我們追求卓越，而不是接受現狀」。這些準則還強調了團隊合作、創新、效率和對變革的開放態度。AWS的領導力準則激勵著員工發揮最佳表現，並持續挑戰自己。'
                ),
                TextSendMessage(
                    text=f'AWS的16項領導力準則反映了他們對卓越和創新的不懈追求。其中包括「我們注重客戶的需求，並持續努力超越他們的期望」，以及「我們追求卓越，而不是接受現狀」。這些準則強調了客戶導向、不斷學習、積極態度等價值觀，構建了一個積極向上的工作環境。'
                ),
                TextSendMessage(
                    text=f'AWS的領導力準則是他們文化的支柱，引導著團隊走向成功。這16項準則包括「我們注重客戶的需求，並持續努力超越他們的期望」，以及「我們追求卓越，而不是接受現狀」。其他準則涵蓋了創新、效率、擁抱變革等核心價值觀。AWS的領導力準則體現了他們對建立卓越企業文化的承諾。'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/aws_leadership.jpg",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/aws_leadership.jpg",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想知道 AWS 未來的發展方向":
            reply_messages = [
                TextSendMessage(
                    text=f'AWS 未來的發展方向將繼續聚焦在提供更強大、更靈活的雲端運算服務，持續投資於人工智慧（AI）、機器學習（ML）、物聯網（IoT）等前沿技術，以滿足不斷變化的企業需求。同時，AWS 將強化數據安全、可靠性和可擴展性，致力於為客戶提供最佳的雲端解決方案。'
                ),
                TextSendMessage(
                    text=f'AWS 未來的發展方向包含了在新興技術領域的深入投資，例如人工智慧、機器學習、區塊鏈等。同時，也將繼續提升雲端基礎設施的效能、安全性和可擴展性，以滿足客戶不斷擴大的需求。AWS 的目標是持續推動科技創新，為全球企業提供最先進的雲端解決方案。'
                ),
                TextSendMessage(
                    text=f'AWS 未來將繼續引領雲端運算的發展，專注於提供更多元的服務和解決方案。將深入探索人工智慧、機器學習、數據分析等領域，並進一步優化雲端基礎設施的性能和安全性。同時，AWS 將持續推動環保和可持續發展的倡議，以建立更可靠的雲端生態系統。'
                ),
                TextSendMessage(
                    text=f'AWS 未來的發展方向將繼續聚焦於創新和技術前沿，計劃進一步擴展在人工智慧、機器學習和數據分析等領域的投資，以提供更強大的雲端解決方案。同時，AWS 將不斷優化其服務，以滿足客戶在數位轉型過程中的需求，並推動雲端技術的不斷演進。'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/aws_future.jpg",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/aws_future.jpg",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想了解 AWS LINE BOT 開發團隊":
            reply_messages = [
                TextSendMessage(
                    text=f'嗨！👋 歡迎加入 AWS Educate 校園大使的 Line bot！\n在這裡，我會與你分享 AWS 的最新資訊、實用技巧、活動消息，以及 AWS Educate 的精彩內容。如果你對雲端運算、技術創新有興趣，那你來對地方啦！有什麼問題都歡迎隨時問我，我會盡力提供協助。一起來開啟雲端科技之旅吧！💡✨'
                ),
                TextSendMessage(
                    text=f'哈囉！歡迎加入 AWS Educate 校園大使的 Line bot！我是你的 AWS 小幫手，將帶你探索 Amazon Web Services 的無限可能。AWS 不僅是全球最大的雲端服務提供商，更是科技創新的引領者。我將與你分享 AWS 的最新消息、實用技巧，還有 AWS Educate 專屬的學習資源。有任何問題或想知道更多，隨時向我發問吧！一同啟程，體驗 AWS 的魅力吧！🚀💻'
                ),
                TextSendMessage(
                    text=f'嗨！歡迎來到 AWS Educate 校園大使的 Line bot！我是你的 AWS 智慧小幫手，將陪你一同踏上雲端運算的冒險之旅。AWS 提供豐富多元的雲端服務，從運算到儲存，應有盡有。這裡我將與你分享 AWS 的最新資訊、技巧，以及 AWS Educate 的專屬學習機會。如果你對雲端技術充滿好奇，就讓我們一同開拓未知領域吧！🌐🔍'
                ),
                TextSendMessage(
                    text=f'你好！歡迎來到 AWS Educate 校園大使的 Line bot！我是你的 AWS 導覽員，將帶你遨遊在 Amazon Web Services 的世界。AWS 不僅提供強大的雲端運算平台，還為你提供了無限的創新可能。我會與你分享 AWS 的最新動態、技術見解，以及 AWS Educate 獨家的學習體驗。有什麼問題都歡迎詢問，讓我們一同迎接科技的挑戰吧！🌟💡'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/aws_educate.png",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/aws_educate.png",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想了解如何成為 AWS Educate 校園大使":
            reply_messages = [
                TextSendMessage(
                    text=f'成為AWS Educate校園大使是一個很讚的機會👍 首先，你可以積極參與AWS Educate舉辦的各種活動，像是技術工作坊、職涯分享會等。接著，你可以在招募面試時展示你的參與證明或心得感想，相信這是一個很加分的特點唷！希望你能抓住這個機會，參與這令人難忘的計劃！'
                ),
                TextSendMessage(
                    text=f'要成為AWS Educate校園大使，首先你可以積極參與AWS Educate舉辦的大小活動，確保你充分了解AWS雲端運算和相關技術。接著，你可以查看AWS Educate官方Facebook or Instagram，或向AWS Educate校園大使詢問招募的相關資訊。藉由積極參與和展示你對AWS的熱情，你將很有機會成為一位AWS Educate校園大使唷！'
                ),
                TextSendMessage(
                    text=f'如果你有興趣成為AWS Educate校園大使，建議你可以定期關注AWS Educate的社群與活動內容，以便瞭解校園大使計劃的最新消息。通常，AWS Educate校園大使計劃會定期開放申請，你可以提交相應的申請資料，包括個人介紹、對AWS的興趣、報名動機。相信加入這個計劃，將成為你學生時期的一段難忘回憶唷！'
                ),
                TextSendMessage(
                    text=f'成為AWS Educate校園大使的第一步，可以先從探索AWS的學習資源和相關技術開始。接著，你可以多多留意AWS Educate校園大使社群發佈的貼文，查找申請和加入的相關資訊。如果你的學校尚未有AWS Educate校園大使，你也可以主動聯繫AWS Educate團隊，了解如何成為推動者並提名自己或其他有興趣的同學參與，希望你能在這個過程中有所收穫！'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/become_ambassader.jpg",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/become_ambassader.jpg",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        else:
            reply_messages = [
                TextSendMessage(
                    text=f'{event_text}'
                ),
            ]
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )


    try:
        # get X-Line-Signature header value
        signature = event['headers']['x-line-signature']

        # get request body as text
        body = event['body']
        handler.handle(body, signature)
    except InvalidSignatureError:
        return {
            'statusCode': 502,
            'body': json.dumps("Invalid signature. Please check your channel access token/channel secret.")
        }
    return {
        'statusCode': 200,
        'body': json.dumps("Hello from Lambda!")
    }
