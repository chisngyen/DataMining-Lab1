# Yêu cầu Đồ án 1: Tiền xử lý dữ liệu
**Môn học:** Khai thác dữ liệu và ứng dụng (CSC14004)

## 1. Mục tiêu và Hình thức
- **Mục tiêu:** Thực hiện quy trình tiền xử lý dữ liệu bài bản (Làm sạch, Thống kê, Pipeline, Phân tích tác động).
- **Hình thức:** Làm việc theo nhóm 2-5 thành viên.
- **Công cụ:** Python (Jupyter Notebook), các thư viện: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `scipy`, `statsmodels`, `opencv-python`, `nltk`/`spacy`, `missingno`, `imbalanced-learn`.

---

## 2. Nội dung chi tiết (4 Phần)

### Phần 1: Tiền xử lý dữ liệu ảnh (Bắt buộc - 25%)
- **Dữ liệu:** Ít nhất 5 lớp, 5.000 ảnh.
- **Thống kê:** Pixel distribution, class imbalance, duplicate detection (pHash), contrast/brightness.
- **Kỹ thuật & Ablation Study:**
    - Resize (3 kích thước, đo SSIM/PSNR).
    - Color space (3 loại, PCA explained variance).
    - Normalization (4 phương pháp, KS test).
    - Data Augmentation (>= 5 phép biến đổi, t-SNE visualization).
- **Nâng cao:** Phân tích PCA đặc trưng ảnh, Edge detection (Sobel, Canny).

### Phần 2: Tiền xử lý dữ liệu bảng (Bắt buộc - 25%)
- **Dữ liệu:** >= 10 thuộc tính, >= 10.000 records, tỉ lệ thiếu >= 5%.
- **EDA chuyên sâu:** Shapiro-Wilk/D’Agostino test, correlation heatmap, missing data matrix, MCAR test.
- **Kỹ thuật:**
    - Imputation (5 chiến lược, đo RMSE).
    - Outlier detection (4 phương pháp: IQR, Z-score, Isolation Forest, LOF, DBSCAN).
    - Scaling (Min-Max, Z-score, Robust, Quantile).
    - Encoding (Target, Binary, Frequency).
    - Lựa chọn đặc trưng (Statistical tests, Model-based, PCA/t-SNE/UMAP).
- **Nâng cao:** SMOTE/ADASYN xử lý mất cân bằng.

### Phần 3: Tiền xử lý dữ liệu văn bản (Chọn 1 trong 2: Phần 3 hoặc 4 - 20%)
- **Dữ liệu:** >= 10.000 mẫu, >= 2 nhãn.
- **Text EDA:** Độ dài (Mann-Whitney U test), Word cloud, Zipf law.
- **Kỹ thuật:** Pipeline chuẩn hóa, Tokenization (4 chiến lược), Stopwords, Stemming/Lemmatization.
- **Vectorization:** BoW, TF-IDF, Word2Vec.
- **Nâng cao:** Sentence Transformer (MiniLM).

### Phần 4: Tiền xử lý dữ liệu chuỗi thời gian (Chọn 1 trong 2: Phần 3 hoặc 4 - 20%)
- **Dữ liệu:** >= 2 năm, tần suất cao (ngày/giờ).
- **Phân tích:** Time plot (trend, season), ACF/PACF, Rolling statistics.
- **Kỹ thuật:** Imputation (4 phương pháp), Stationarity tests (ADF, KPSS, PP), Decomposition (STL), Feature extraction (sin/cos, holidays), Anomaly detection.
- **Nâng cao:** Granger Causality.

---

## 3. Quy cách nộp bài và Đánh giá (30%)
- **Mã nguồn:** Jupyter Notebook sạch, có chú thích, tỉ lệ AI <= 30%.
- **Báo cáo:** File PDF >= 20 trang (Tóm tắt, Phân tích so sánh, Thảo luận, Phân công).
- **Cấu trúc thư mục:**
    ```text
    Group_ID/
    |-- README.md
    |-- requirements.txt
    |-- data/ (raw & processed)
    |-- notebooks/ (01_EDA_image, 02_preprocessing_image, ..)
    |-- docs/ (Report.pdf)
    ```
- **Tiêu chí chấm:** Đúng kỹ thuật, phân tích sâu, đo lường định lượng và lý giải được lựa chọn.
