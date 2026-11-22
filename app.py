"""Streamlit dashboard: streamlit run app.py"""
from pathlib import Path
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from src.analysis import run

ROOT=Path(__file__).parent
st.set_page_config(page_title='Wine UCI - Mini Project',layout='wide')
st.title('🍇 Wine UCI – Dashboard phân loại mẫu')
st.caption('Dữ liệu Wine (UCI). Phân tích và mô hình minh họa phục vụ bài thực hành Công nghệ số nâng cao.')
file=ROOT/'data/wine_clean.csv'
report=ROOT/'results/Bao_cao_khoa_hoc_Wine_UCI.pdf'
if not file.exists() or not report.exists():
    with st.spinner('Đang chạy phân tích và xuất PDF ...'):
        run()
df=pd.read_csv(file)
a,b,c=st.columns(3)
a.metric('Số mẫu',len(df));b.metric('Số đặc trưng',len(df.columns)-1);c.metric('Số nhóm',df.target.nunique())
st.subheader('Dữ liệu mẫu')
st.dataframe(df.head(20),use_container_width=True)
features=[x for x in df.columns if x!='target']
x=st.selectbox('Chọn trục X',features,index=features.index('alcohol') if 'alcohol' in features else 0)
y=st.selectbox('Chọn trục Y',features,index=features.index('color_intensity') if 'color_intensity' in features else 1)
fig,ax=plt.subplots(figsize=(8,4.3))
for cls,g in df.groupby('target'):
    ax.scatter(g[x],g[y],label=f'Nhóm {cls}',alpha=.75)
ax.set(xlabel=x,ylabel=y,title=f'{x} và {y} theo nhóm');ax.legend()
st.pyplot(fig)
st.subheader('Biểu đồ và kết quả đã xuất')
chart=st.selectbox('Xem hình', ['class_distribution.png','feature_scatter.png','confusion_matrix.png'])
st.image(str(ROOT/'results'/chart),use_container_width=False)
with open(report,'rb') as f:
    st.download_button('📄 Tải báo cáo PDF',f.read(),file_name=report.name,mime='application/pdf')
with open(ROOT/'data/wine_clean.csv','rb') as f:
    st.download_button('⬇️ Tải dữ liệu đã xử lý',f.read(),file_name='wine_clean.csv',mime='text/csv')
if st.button('🔄 Chạy lại toàn bộ phân tích & PDF'):
    run();st.rerun()
st.caption('Dữ liệu UCI Wine. Các kết quả mô hình chỉ dùng để minh họa bài thực hành, không phải tuyên bố khoa học tổng quát.')
