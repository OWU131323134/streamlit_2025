import streamlit as st
import pandas as pd
import datetime
import google.generativeai as genai
from io import BytesIO
from PIL import Image

# ページデザイン設定
st.set_page_config(
    page_title="My Cosme Advisor",
    page_icon="🧴",
    layout="wide"
)

# シンプルで洗練されたスタイルを適用
st.markdown("""
    <style>
    body, .main {
        background-color: #f9f9fb;
        font-family: 'Helvetica Neue', sans-serif;
    }
    h1, h2, h3 {
        color: #333333;
    }
    .stButton > button {
        background-color: #ffffff;
        color: #333;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 0.4em 1em;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #f0f0f0;
        border-color: #999;
    }
    .stTextInput > div > input, .stTextArea > div > textarea {
        background-color: #ffffff;
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

st.title("My Cosme Advisor")

# Gemini APIキーの安全な読み込み
if "gemini" in st.secrets and "api_key" in st.secrets["gemini"]:
    api_key = st.secrets["gemini"]["api_key"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash-lite")
else:
    model = None

# 初期化
if 'product_data' not in st.session_state:
    st.session_state['product_data'] = pd.DataFrame(columns=[
        '商品名', '使用開始日', '肌悩み', '満足度', 'コメント', '画像'
    ])

if 'wishlist' not in st.session_state:
    st.session_state['wishlist'] = []

# Gemini AI 応答関数
def get_gemini_advice(prompt):
    if model is None:
        return "Gemini APIキーが設定されていません。secrets.toml を確認してください。"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"エラーが発生しました: {e}"

# UI タブ（3タブ構成）
tab1, tab2, tab3 = st.tabs(["🧴 コスメ記録", "🧠 AIアドバイス", "📓 WISHリスト"])

# タブ1: コスメ記録・追加
with tab1:
    st.subheader("新しいコスメを記録")
    with st.form("add_form"):
        name = st.text_input("商品名")
        start_date = st.date_input("使用開始日", datetime.date.today())
        concern = st.selectbox("肌悩み", ['乾燥', '敏感', 'ニキビ', 'シミ', 'しわ', 'その他'])
        rating = st.slider("満足度（1:低〜5:高）", 1, 5, 3)
        comment = st.text_area("コメント")
        image_file = st.file_uploader("商品画像（任意）", type=["jpg", "jpeg", "png"])
        submitted = st.form_submit_button("追加する")

        if submitted:
            image_data = None
            if image_file:
                image = Image.open(image_file)
                buffered = BytesIO()
                image.save(buffered, format="PNG")
                image_data = buffered.getvalue()

            new_row = pd.DataFrame([{
                '商品名': name,
                '使用開始日': str(start_date),
                '肌悩み': concern,
                '満足度': rating,
                'コメント': comment,
                '画像': image_data
            }])
            st.session_state['product_data'] = pd.concat([st.session_state['product_data'], new_row], ignore_index=True)
            st.success("コスメ情報を追加しました")

    st.subheader("登録済みのコスメ一覧")
    df = st.session_state['product_data']
    if not df.empty:
        sort_option = st.selectbox("並び替え方法を選んでください", ["新しい順", "古い順", "満足度が高い順", "満足度が低い順"])

        if sort_option == "新しい順":
            df = df.sort_values(by="使用開始日", ascending=False)
        elif sort_option == "古い順":
            df = df.sort_values(by="使用開始日", ascending=True)
        elif sort_option == "満足度が高い順":
            df = df.sort_values(by="満足度", ascending=False)
        elif sort_option == "満足度が低い順":
            df = df.sort_values(by="満足度", ascending=True)

        for _, row in df.iterrows():
            with st.expander(f"{row['商品名']}（{row['使用開始日']}）"):
                st.markdown(f"**肌悩み：** {row['肌悩み']}")
                st.markdown(f"**満足度：** {'⭐' * int(row['満足度'])}")
                st.markdown(f"**コメント：** {row['コメント']}")
                if row['画像']:
                    st.image(row['画像'], width=150)
    else:
        st.info("コスメがまだ登録されていません。")

# タブ2: AIスキンケア相談
with tab2:
    st.subheader("Gemini AI にスキンケア相談")
    user_input = st.text_area("肌の状態・相談内容を入力：", placeholder="例：乾燥肌でおすすめのスキンケア商品は？")
    if st.button("アドバイスをもらう"):
        if user_input.strip():
            response = get_gemini_advice(user_input)
            st.success(response)
        else:
            st.warning("入力内容が空です。")

# タブ3: 購入予定リスト
with tab3:
    st.subheader("気になるコスメ")
    with st.form("wishlist_form"):
        new_item = st.text_input("商品名")
        reason = st.text_area("メモ")
        wish_img = st.file_uploader("商品画像（任意）", type=["jpg", "jpeg", "png"], key="wishlist_uploader")
        add_item = st.form_submit_button("追加")

        if add_item and new_item.strip():
            img_bytes = None
            if wish_img:
                img = Image.open(wish_img)
                buffer = BytesIO()
                img.save(buffer, format="PNG")
                img_bytes = buffer.getvalue()

            st.session_state['wishlist'].append((new_item, reason, img_bytes))
            st.success("WISHリストに追加しました")

    st.divider()
    for item, reason, img_data in st.session_state['wishlist']:
        with st.container():
            st.markdown(f"#### {item}")
            if reason:
                st.caption(reason)
            if img_data:
                st.image(img_data, width=150)
            st.markdown("---")
