# Streamlitライブラリをインポート
import streamlit as st
import random
import time


# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('Streamlitのサンプルアプリ')

# テキスト入力ボックスを作成し、ユーザーからの入力を受け取る
user_input = st.text_input('あなたの名前を入力してください')

# ボタンを作成し、クリックされたらメッセージを表示
if st.button('挨拶する'):
    if user_input:  # 名前が入力されているかチェック
        st.success(f'🌟 こんにちは、{user_input}さん! 🌟')  # メッセージをハイライト
    else:
        st.error('名前を入力してください。')  # エラーメッセージを表示

# スライダーを作成し、値を選択
number = st.slider('好きな数字（10進数）を選んでください', 0, 100)

# 補足メッセージ
st.caption("十字キー（左右）でも調整できます。")

# 選択した数字を表示
st.write(f'あなたが選んだ数字は「{number}」です。')

# 選択した数値を2進数に変換
binary_representation = bin(number)[2:]  # 'bin'関数で2進数に変換し、先頭の'0b'を取り除く
st.info(f'🔢 10進数の「{number}」を2進数で表現すると「{binary_representation}」になります。 🔢')  # 2進数の表示をハイライト
teki=1000
mikata=100

st.header("TRPG")

if st.button('1d100'):
    random_num=random.randint(1,100)
    with st.spinner("ダイスロール中!"):
          time.sleep(1)
    st.write(f'生成された乱数:{random_num}')
    
if random_num<=5:
        st.write('クリティカル!') 
        damage=100
        teki-=damage
        
       
     
elif 5<random_num<=50:
        st.write('成功!')  
        damage=50
        teki-=damage
        
       
        
elif 50<random_num<95:
        damage=0
        st.write('失敗!')
        teki-=damage
        
elif random_num>=95:
        st.write('ファンブル!')     
        damage=10
        mikata-=damage
        
        
st.write(f'敵の残り体力は{teki}だ！')  
teki=max(0,teki)  
st.write(f'味方の残り体力は{mikata}だ！') 
mikata=max(0,mikata)  
