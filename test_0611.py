import streamlit as st

st.title("日向坂おすすめ楽曲診断 ♪💙")



mood = st.radio("**⛅ 今のあなたの気分に近いのは？**", ["ときめきたい", "癒されたい", "背中を押してほしい"])
vibe = st.radio("**🎀 今聴きたい曲の雰囲気は？**", ["ふわふわ", "きらきら"])
situ = st.slider("**💙 どんな時に聴きたい？ 【頑張る〜まったり】**", 0, 100, 50)

if st.button("あなたにぴったりの一曲を診断 ♪"):
    song = "君しか勝たん"
    comment = "ポップでかわいい、元気をもらえる曲♪"
    mv_url = "https://youtu.be/Z59HsgPVbWY?si=XDg2QyX_S7wVMgYQ"

    if mood == "ときめきたい" and vibe == "きらきら":
        if situ <= 50:
            song = "キュン"
            comment = "きらきら輝く恋のドキドキを感じるデビュー曲！"
            mv_url = "https://youtu.be/K5HPhoqyO4U?si=k5djIxgqUxUoKQnc"
        else:
            song = "ドレミソラシド"
            comment = "爽やかなメロディにときめき全開の１曲♪"
            mv_url = "https://youtu.be/qsureA57fEo?si=xvpDgG2Z-NMZxue9"

    elif mood == "ときめきたい" and vibe == "ふわふわ":
        if situ >= 50:
            song = "JOYFUL LOVE"
            comment = "優しいメロディで包み込む、心温まる１曲♬"
            mv_url = "https://youtu.be/mbXtz9zGB_E?si=uXhb8_dleplV_cFS"
        else:
            song = "君はハニーデュー"
            comment = "甘くて柔らかな恋の気持ちがはじける１曲！"
            mv_url = "https://youtu.be/wRzPuptA6yw?si=UJzXkyvdK57XGUtc"

    elif mood == "癒されたい" and vibe == "きらきら":
        if situ >= 50:
            song = "アザトカワイイ"
            comment = "とってもかわいくて明るい元気がもらえる癒しソング！♬"
            mv_url = "https://youtu.be/m-FRFhvM1EA?si=DTO7pUyugnftOVhY"
        else:
            song = "Am I ready?"
            comment = "ときめきはじける心地良い１曲"
            mv_url = "https://youtu.be/vYKRIwJGRKk?si=qBP8xbpSlO-cNRm8"

    elif mood == "癒されたい" and vibe == "ふわふわ":
        if situ >= 50:
            song = "JOYFUL LOVE"
            comment = "優しいメロディで包み込む、心温まる１曲♬"
            mv_url = "https://youtu.be/mbXtz9zGB_E?si=uXhb8_dleplV_cFS"
        else:
            song = "ブルーベリー&ラズベリー"
            comment = "爽やかで甘酸っぱい気分にぴったりの４期生楽曲！"
            mv_url = "https://youtu.be/lV_Boxqp-ak?si=kyHbf4TcguXWuVke"


    elif mood == "背中を押してほしい" and vibe == "ふわふわ":
        if situ >= 50:
            song = "青春の馬"
            comment = "力強いメロディで未来へ踏み出す勇気をくれる１曲！"
            mv_url = "https://youtu.be/hZQzmzXjJB0?si=DRGks0Vup-XB4q9q"
        else:
            song = "世界にはThank you!が溢れている"
            comment = "感謝と希望にあふれ、前向きになれる応援ソング！"
            mv_url = "https://youtu.be/Tl51xNHeP4g?si=_YxRYzdMcOcgUhgJ"


    elif mood == "背中を押してほしい" and vibe == "きらきら":
        if situ >= 50:
            song = "ってか"
            comment = "リズミカルでポジティブなエネルギーあふれる応援歌"
            mv_url = "https://youtu.be/pZDqElqNW34?si=iRAQGtYiE8Uwz-n2"
        else:
            song = "ソンナコトナイヨ"
            comment = "力強く背中を押してくれる心強いメッセージソング"
            mv_url = "https://youtu.be/7njC5lgL61c?si=64bmfvotLu2DUgSN"


    st.subheader(f"今日のおすすめの曲：{song}")
    st.write(comment)
    st.markdown(f"[MVを観る]({mv_url})", unsafe_allow_html=True)
