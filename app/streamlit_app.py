import streamlit as st
import pandas as pd
from vi_plot_lib import create_plot

def open_file():
    file = st.file_uploader("CSVファイルをアップロード", type="csv")

    if file is not None:
        df = pd.read_csv(file)
        columns = df.columns.tolist()

        x_label = st.selectbox("X軸に使う列名を選んでください", columns)
        y_labels = st.multiselect("Y軸に使う列名を選んでください", columns)

        if len(y_labels) > 0:
            x_label_custom = st.text_input("X軸ラベル", "X軸")
            y_label_custom = st.text_input("Y軸ラベル", "Y軸")

            x_min = st.number_input("X最小", value=float(df[x_label].min()))
            x_max = st.number_input("X最大", value=float(df[x_label].max()))
            y_min = st.number_input("Y最小", value=float(df[y_labels[0]].min()))
            y_max = st.number_input("Y最大", value=float(df[y_labels[0]].max()))

            log_scale = st.radio("対数スケール", ("なし", "X軸", "Y軸", "両方"))
            log_x = "X軸" in log_scale
            log_y = "Y軸" in log_scale

            font_size = st.slider("フォントサイズ", 6, 24, 12)

            # 🔥 config設計
            config = {
                "x": x_label,
                "y": y_labels,
                "label": {
                    "x": x_label_custom,
                    "y": y_label_custom
                },
                "range": {
                    "x": [x_min, x_max],
                    "y": [y_min, y_max]
                },
                "scale": {
                    "x": "log" if log_x else "linear",
                    "y": "log" if log_y else "linear"
                },
                "style": {
                    "font_size": font_size
                }
            }

            # ライブラリ呼び出し
            fig = create_plot(df, config)

            st.pyplot(fig)

st.title("CSVグラフ描画アプリ")
open_file()