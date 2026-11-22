# Mini-project: AI + Python sinh báo cáo khoa học từ dữ liệu Wine UCI

## Giới thiệu
Dự án thực hành Python: làm sạch dữ liệu Wine thật từ UCI, trực quan hóa, phân loại 3 nhóm bằng Logistic Regression, tự động tạo báo cáo PDF và dashboard Streamlit. Không tự tạo dữ liệu hay giả lập kết quả. Dữ liệu UCI Wine có **178 mẫu, 13 đặc trưng, 3 lớp**.

Nguồn dataset: https://archive.ics.uci.edu/dataset/109/wine  
Bản sao được lấy từ `sklearn.datasets.load_wine` và xuất thành `data/wine_uci.csv`.

## Cấu trúc
```
data/                Dữ liệu gốc và sau làm sạch (CSV)
src/analysis.py       Tiền xử lý, mô hình, biểu đồ và sinh PDF
results/              PDF, PNG, metrics.json, dự đoán
app.py                Dashboard Streamlit
requirements.txt      Thư viện cần thiết
LICENSE               MIT (áp dụng cho mã nguồn do nhóm viết)
```

## Cách chạy (VS Code)
1. Mở folder dự án trong VS Code, chọn Python interpreter (khuyến nghị Python 3.10–3.13).
2. Mở Terminal → `python -m pip install -r requirements.txt` (macOS có thể cần `python3`).
3. Mở `src/analysis.py`, bấm **Run Python File** để tạo lại ảnh, dự đoán, PDF.
4. Mở Terminal → `python -m streamlit run app.py`.
5. Mở URL Streamlit hiển thị trong Terminal (thường http://localhost:8501).

## Kết quả
- `results/Bao_cao_khoa_hoc_Wine_UCI.pdf`: báo cáo tự sinh.
- `results/*.png`: 3 hình trực quan hóa.
- `results/metrics.json`: kết quả đánh giá mô hình; dữ liệu chia huấn luyện/kiểm tra 75/25, stratified, seed 42.
- Dashboard tương tác chọn 2 biến, xem biểu đồ, tải PDF và CSV.

## Giới hạn
Tập dữ liệu nhỏ và kết quả phụ thuộc chia dữ liệu. Demo dùng duy nhất một lần train/test split, chưa kiểm định chéo. Logistic Regression dùng StandardScaler trong Pipeline.

## Giấy phép
**MIT** chỉ áp dụng cho mã nguồn và tài liệu do nhóm tạo. Dữ liệu gốc thuộc nguồn UCI và phải tuân theo điều khoản sử dụng/trích dẫn của nơi cung cấp; không được tự khẳng định dataset thuộc MIT. Xem `LICENSE`.

## GitHub
https://github.com/huynhnhattruong65/Wine-UCI-Mini-Project
