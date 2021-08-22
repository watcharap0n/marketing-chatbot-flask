from linebot.models import ImagemapArea, ImagemapSendMessage, BaseSize, MessageImagemapAction, URIImagemapAction


def mango_products():
    template_image = ImagemapSendMessage(
        base_url='https://sv1.picz.in.th/images/2020/12/02/j3VUfR.png',
        alt_text='products',
        base_size=BaseSize(height=1600, width=1040),
        actions=[
            MessageImagemapAction(
                text='@ERPSoftware',
                area=ImagemapArea(
                    x=350, y=248, width=1037, height=400
                )
            ),
            MessageImagemapAction(
                text='@NewFeature',
                area=ImagemapArea(
                    x=49, y=1108, width=294, height=294
                )
            ),
            MessageImagemapAction(
                text='@Optional',
                area=ImagemapArea(
                    x=759, y=1148, width=280, height=280
                )
            ),
            URIImagemapAction(
                link_uri='https://www.mangoconsultant.com/th/mango-anywhere-software',
                area=ImagemapArea(
                    x=164, y=1421, width=863, height=200
                )
            ),
            URIImagemapAction(
                link_uri='https://www.mangoconsultant.com/th/mango-anywhere-software',
                area=ImagemapArea(
                    x=366, y=1118, width=280, height=280
                )
            ),
            MessageImagemapAction(
                text='@Business',
                area=ImagemapArea(
                    x=511, y=720, width=400, height=400
                )
            )
        ])
    return template_image
