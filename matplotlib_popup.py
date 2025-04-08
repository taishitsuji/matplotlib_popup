import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import japanize_matplotlib
import matplotlib
from matplotlib import font_manager

# 日本語フォントと英数字フォントを分けて設定
prop_japanese = font_manager.FontProperties(fname="C:/Windows/Fonts/MSPGOTHIC.TTC")
prop_english = font_manager.FontProperties(fname="./fonts/times.ttf")

# グローバル変数
fig, ax1 = None, None
line_plots = []

# CSVファイルをアップロードする関数
def open_file():
    file = st.file_uploader("CSVファイルをアップロード", type="csv")
    if file is not None:
        # CSVファイルを読み込む
        df = pd.read_csv(file)

        # ヘッダー（列名）を取得
        columns = df.columns.tolist()

        # 軸ラベル設定
        x_label = st.selectbox("X軸に使う列名を選んでください", columns)
        y_labels = st.multiselect("Y軸に使う列名を選んでください（複数選択可）", columns)

        if len(y_labels) > 0:
            # ラベルを自分で設定するオプション
            x_label_custom = st.text_input("X軸ラベル", "X軸")
            y_label_custom = st.text_input("Y軸ラベル", "Y軸")

            # 描画範囲の設定（最大最小値に上限なし）
            x_min = st.number_input("X軸の最小値", value=float(df[x_label].min()))
            x_max = st.number_input("X軸の最大値", value=float(df[x_label].max()))
            y_min = st.number_input("Y軸の最小値", value=float(df[y_labels[0]].min()))
            y_max = st.number_input("Y軸の最大値", value=float(df[y_labels[0]].max()))

            # 対数スケールのオプション
            log_scale = st.radio("対数スケールを使用しますか？", ("なし", "X軸", "Y軸", "両方"))
            log_x = "X軸" in log_scale
            log_y = "Y軸" in log_scale

            # 凡例の文字サイズを設定
            font_size = st.slider("凡例の文字サイズ", min_value=6, max_value=24, value=12)

            # グラフ描画
            plot_graph(df, x_label, y_labels, x_label_custom, y_label_custom, x_min, x_max, y_min, y_max, log_x, log_y, font_size)

# グラフ描画関数
def plot_graph(df, x_label, y_labels, x_label_custom, y_label_custom, x_min, x_max, y_min, y_max, log_x, log_y, font_size):
    global fig, ax1, line_plots

    if fig is None or ax1 is None:
        # 新規に図を作成
        fig, ax1 = plt.subplots(figsize=(10, 6))
    else:
        # 既存のグラフをクリア
        for line in line_plots:
            line.remove()
        ax1.clear()

    # 軸ラベルの設定
    ax1.set_xlabel(x_label_custom, fontproperties=prop_english, fontsize=font_size)  # X軸ラベル
    ax1.set_ylabel(y_label_custom, color="k", fontproperties=prop_english, fontsize=font_size)  # Y軸ラベル

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']

    # 複数のY軸データをプロット（点を使わず、線だけ）
    line_plots = []
    for i, y_label in enumerate(y_labels):
        line = ax1.plot(df[x_label], df[y_label], color=colors[i % len(colors)], label=y_label)  # 自動で色を変える
        line_plots.append(line[0])  # プロットした線を保存

    # 描画範囲を設定
    ax1.set_xlim(x_min, x_max)
    ax1.set_ylim(y_min, y_max)

    # 対数スケールを設定（必要に応じて）
    if log_x:
        ax1.set_xscale('log')
    if log_y:
        ax1.set_yscale('log')

    # x軸メモリの数字を直線に表示（回転を0度）
    plt.xticks(rotation=0, fontproperties=prop_english, fontsize=font_size)  # X軸の数字
    plt.yticks(fontproperties=prop_english, fontsize=font_size)  # Y軸の数字

    ax1.grid(True)

    # 凡例を表示（凡例のフォントサイズを変更）
    ax1.legend(loc="best", fontsize=font_size, prop=prop_english)  # 凡例のサイズも統一

    fig.tight_layout()


    # Streamlit上にグラフを表示
    st.pyplot(fig)

    # 画像保存ボタン
    save_name = st.text_input("保存する画像名を入力してください", "plot_image")
    save_path = st.text_input("保存先のパスを入力してください", "C:/Users/310Lab_PC/Desktop/")  # 例: デスクトップに保存

    if st.button("画像を保存"):
        # 画像保存先のパスと名前を結合
        img_path = f"{save_path}/{save_name}.png"
        fig.savefig(img_path)  # 画像を保存
        st.success(f"画像が保存されました: {img_path}")

# タイトル表示
st.title("CSVグラフ描画アプリ")

# CSVファイルの読み込みボタン
open_file()















