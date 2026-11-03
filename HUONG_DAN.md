# HƯỚNG DẪN THỰC HIỆN VÀ THANG ĐIỂM
## Đề tài 7 — Phân cụm khách hàng bằng K-Means
**Học phần: TRÍ TUỆ NHÂN TẠO VÀ HỌC MÁY — Mã số: D101TN6**  
Trường Đại học KTCN Long An · Khoa Công nghệ

---

## 1. Thông tin chung

| Hạng mục | Thông tin |
|---------|-----------|
| Số thành viên nhóm | **3 sinh viên** |
| Thời gian thực hiện | **3 ngày** kể từ ngày nhận đề tài |
| Hình thức đánh giá | Notebook chạy được + báo cáo ngắn + demo trực tiếp + hỏi đáp |
| Trọng số | Theo quy định của giảng viên phụ trách học phần |

> **Lưu ý:** Điểm mỗi sinh viên = Điểm nhóm × Hệ số đóng góp cá nhân (0,7 – 1,1), xác định qua bảng phân công công việc và kết quả trả lời câu hỏi tại buổi báo cáo.

---

## 2. Thang điểm tổng quát (/10)

| Thành phần | Trọng số | Nội dung đánh giá |
|-----------|---------|-------------------|
| **A. Phân tích và khám phá dữ liệu (EDA)** | 20% | Thống kê mô tả, biểu đồ phân phối, ma trận tương quan, nhận xét có ý nghĩa |
| **B. Tiền xử lý và lựa chọn đặc trưng** | 15% | Chuẩn hóa đúng cách, lý giải lựa chọn đặc trưng |
| **C. Cài đặt K-Means và chọn K** | 25% | Elbow curve, Silhouette Score, lý giải chọn K tối ưu |
| **D. Trực quan hóa và phân tích cụm** | 20% | Scatter plot PCA, bảng đặc trưng trung bình từng cụm, đặt tên nhóm |
| **E. Hướng ứng dụng thực tế** | 10% | Đề xuất hành động kinh doanh cụ thể cho ít nhất mỗi cụm |
| **F. Báo cáo và demo** | 10% | Notebook sạch, giải thích rõ từng bước, demo chạy được |
| **G. Đóng góp cá nhân** | Hệ số | Bảng phân công + trả lời hỏi đáp |

---

## 3. Rubric chi tiết

| Tiêu chí | Trọng số | Tốt (8,5 – 10) | Đạt (5,0 – 8,4) | Chưa đạt (< 5,0) |
|---------|---------|---------------|----------------|-----------------|
| **A. EDA** | 20% | ≥ 4 biểu đồ rõ ràng; ma trận tương quan có nhận xét; phát hiện được đặc điểm nổi bật của dữ liệu | Có biểu đồ và thống kê cơ bản nhưng thiếu nhận xét hoặc thiếu một số biểu đồ quan trọng | Chỉ in ra `df.describe()` không có biểu đồ hoặc nhận xét |
| **B. Tiền xử lý** | 15% | Chuẩn hóa bằng `StandardScaler`, giải thích lý do; kiểm tra và xử lý giá trị ngoại lai nếu có | Chuẩn hóa được nhưng không giải thích; chưa kiểm tra ngoại lai | Không chuẩn hóa hoặc đưa dữ liệu thô vào K-Means |
| **C. K-Means + chọn K** | 25% | Vẽ Elbow curve, tính Silhouette Score cho ≥ 3 giá trị K; lý giải rõ ràng vì sao chọn K tối ưu | Có Elbow hoặc Silhouette nhưng không cả hai; lý giải sơ sài | Chọn K tùy tiện không có cơ sở, không có đồ thị đánh giá |
| **D. Trực quan + phân tích** | 20% | Scatter plot PCA màu theo cụm rõ ràng; bảng so sánh đặc trưng trung bình từng cụm; mỗi cụm được đặt tên và mô tả tính cách | Có scatter plot và bảng trung bình nhưng không đặt tên cụm hoặc mô tả còn mờ nhạt | Không có biểu đồ trực quan hóa cụm; kết quả không thể hiểu được |
| **E. Hướng ứng dụng** | 10% | Đề xuất ≥ 1 hành động kinh doanh cụ thể (ví dụ: loại ưu đãi, kênh liên lạc, chiến dịch marketing) cho từng nhóm khách hàng, có gắn với đặc trưng cụm | Nêu được ứng dụng nhưng chung chung, chưa gắn với kết quả phân cụm | Không đề cập ứng dụng hoặc sao chép nội dung không liên quan |
| **F. Báo cáo & demo** | 10% | Notebook có tiêu đề từng phần, code sạch, chạy lại từ đầu không lỗi; demo giải thích kết quả được khi hỏi | Notebook chạy được nhưng thiếu giải thích; có lỗi nhỏ khi chạy lại | Notebook không chạy được; không demo được |

> **Ghi chú:** Nhóm sao chép nguyên mã nguồn từ nguồn khác mà không trích dẫn sẽ bị điểm 0 toàn bộ đề tài.

---

## 4. Yêu cầu cụ thể

### Dữ liệu
- Sử dụng file `data/customers.csv` sinh bằng `python download_data.py` (300 khách hàng, 5 đặc trưng, không cần Internet).
- Mô tả rõ trong báo cáo: số dòng, số cột, ý nghĩa từng đặc trưng, `random_seed` dùng để sinh dữ liệu.

### Thuật toán bắt buộc

| Bước | Yêu cầu |
|------|---------|
| Chuẩn hóa | `StandardScaler` từ `sklearn.preprocessing` |
| Chọn K | Elbow curve (inertia vs K từ 2 đến 10) **và** Silhouette Score |
| Phân cụm | `KMeans(n_clusters=K_tối_ưu, random_state=42, n_init=10)` |
| Trực quan hóa | PCA 2D scatter plot màu theo nhãn cụm |
| Phân tích | Bảng giá trị trung bình từng đặc trưng theo cụm + đặt tên nhóm |

### Kết quả bắt buộc phải có trong notebook

| # | Hạng mục | Mô tả |
|---|---------|-------|
| 1 | Biểu đồ phân phối | Histogram hoặc boxplot cho từng đặc trưng |
| 2 | Ma trận tương quan | Heatmap với `seaborn.heatmap` |
| 3 | Elbow curve | Inertia vs K (2–10) |
| 4 | Bảng Silhouette | Silhouette Score cho ít nhất K = 2, 3, 4, 5 |
| 5 | Scatter plot PCA | 2D scatter, màu theo cụm, có legend |
| 6 | Bảng đặc trưng cụm | Giá trị trung bình từng cụm, rõ ràng, có đơn vị |
| 7 | Tên và mô tả nhóm | Ít nhất 1 dòng mô tả đặc điểm và hành động đề xuất cho mỗi cụm |

---

## 5. Yêu cầu về báo cáo ngắn

Viết trực tiếp trong **notebook** (các cell Markdown), không cần nộp file Word/PDF riêng. Cấu trúc tối thiểu:

| Mục | Nội dung |
|-----|---------|
| 1. Giới thiệu bài toán | Bài toán phân cụm là gì, tại sao hữu ích trong kinh doanh |
| 2. Mô tả dữ liệu | Nguồn gốc, số dòng/cột, ý nghĩa từng đặc trưng, thống kê mô tả |
| 3. Phương pháp | Nguyên lý K-Means, cách chọn K, vai trò của chuẩn hóa và PCA |
| 4. Kết quả và phân tích | Số cụm chọn, đặc điểm từng cụm, biểu đồ, bảng so sánh |
| 5. Hướng ứng dụng | Đề xuất hành động cụ thể cho từng nhóm khách hàng |
| 6. Kết luận | Tóm tắt ngắn: kết quả chính, hạn chế, hướng phát triển |

> Toàn bộ biểu đồ và bảng phải có tiêu đề và nhãn trục. Mọi kết quả số phải tái lập được khi chạy lại notebook.

---

## 6. Yêu cầu demo

- Notebook chạy lại **từ đầu đến cuối không lỗi** trước buổi báo cáo.
- Mỗi thành viên trình bày **ít nhất một phần** và phải trả lời được câu hỏi về phần mình đảm nhận.
- Thời lượng demo: **10 – 15 phút** (ngắn gọn hơn đồ án lớn).

---

## 7. Phân công gợi ý và tiến độ

| Ngày | Thành viên 1 | Thành viên 2 | Thành viên 3 |
|------|-------------|-------------|-------------|
| **Ngày 1** | Chạy `download_data.py`, EDA (biểu đồ phân phối, heatmap tương quan) | Nghiên cứu lý thuyết K-Means; viết mục 3 (Phương pháp) trong notebook | Cài môi trường, nghiên cứu PCA, chuẩn bị phần chuẩn hóa |
| **Ngày 2** | Hoàn thiện EDA, xử lý ngoại lai nếu có | Cài đặt Elbow + Silhouette, chạy K-Means K = 2…10 | PCA scatter plot, bảng đặc trưng trung bình từng cụm |
| **Ngày 3** | Đặt tên cụm, viết mục 5 (Ứng dụng) | Viết kết luận, kiểm tra notebook chạy lại sạch | Chuẩn bị demo, luyện tập thuyết trình |

---

## 8. Danh mục sản phẩm nộp

| Tệp | Mô tả |
|-----|-------|
| `notebook.ipynb` | Notebook Jupyter đầy đủ, có thể chạy lại |
| `data/customers.csv` | File dữ liệu (sinh bởi `download_data.py`) |
| Bảng phân công | Ghi rõ từng thành viên phụ trách phần nào (chèn vào cuối notebook) |

> Đặt tên file theo mẫu: `DeTai7_Nhom<số>_notebook.ipynb`

---

## 9. Điểm cộng

| Hạng mục | Điểm cộng tối đa |
|---------|-----------------|
| So sánh với Agglomerative Clustering (vẽ dendrogram) | +0,5 |
| Thử DBSCAN và nhận xét ưu điểm so với K-Means | +0,5 |
| Trực quan hóa 3D (3 đặc trưng quan trọng nhất) | +0,5 |
| Tổng điểm cộng tối đa | **+1,0** (điểm cuối tối đa 10) |

---

*Long An, năm 2026 — Giảng viên phụ trách: Lê Ngọc Bảo Trân*
