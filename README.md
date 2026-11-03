# Đề tài 7 — Phân cụm khách hàng bằng K-Means

## Mục tiêu
Xây dựng hệ thống phân nhóm khách hàng tự động từ dữ liệu hành vi mua sắm, sử dụng thuật toán K-Means. Từ kết quả phân cụm, rút ra đặc trưng từng nhóm và đề xuất chiến lược phục vụ phù hợp.

---

## Dữ liệu — Hành vi mua sắm mô phỏng

| Thuộc tính | Giá trị |
|-----------|---------|
| Số khách hàng | 300 |
| Số đặc trưng | 5 |
| Nhãn thực (dùng để kiểm tra) | 4 nhóm ẩn |
| Kích thước file | < 50 KB |
| Nguồn | Dữ liệu tự sinh (seeded random) |
| Yêu cầu Internet | **Không** |

### Mô tả các đặc trưng

| Cột | Kiểu | Ý nghĩa |
|-----|------|---------|
| `customer_id` | int | Mã khách hàng |
| `age` | int | Tuổi (18–70) |
| `annual_income` | float | Thu nhập hàng năm (triệu VND) |
| `spending_score` | float | Điểm chi tiêu (0–100, do hệ thống tính) |
| `purchase_freq` | int | Số lần mua trong năm |
| `avg_transaction` | float | Giá trị trung bình mỗi giao dịch (triệu VND) |

> **Lưu ý:** Dữ liệu được sinh bằng `random_seed=42`. Nhóm cần mô tả rõ quy tắc sinh trong báo cáo để đảm bảo tái lập được kết quả.

---

## Cài đặt và sinh dữ liệu

```bash
pip install scikit-learn pandas matplotlib numpy
python download_data.py
```

Script sinh file `data/customers.csv` với 300 khách hàng, in thống kê mô tả, và kiểm tra tính hợp lệ.

---

## Thuật toán bắt buộc

| Phương án | Thư viện | Ghi chú |
|----------|---------|---------|
| **K-Means** | `sklearn.cluster.KMeans` | Thuật toán chính |
| **Phương pháp khuỷu tay (Elbow)** | thủ công | Chọn số cụm K tối ưu |
| **Hệ số Silhouette** | `sklearn.metrics.silhouette_score` | Đánh giá chất lượng cụm |

### Quy trình bắt buộc

1. **Khám phá dữ liệu (EDA)**: thống kê mô tả, phân phối từng đặc trưng, ma trận tương quan
2. **Tiền xử lý**: chuẩn hóa đặc trưng bằng `StandardScaler`
3. **Chọn K**: vẽ đường Elbow (inertia vs K từ 2 đến 10), tính Silhouette Score
4. **Huấn luyện K-Means**: với K tối ưu đã chọn, `random_state=42`
5. **Phân tích cụm**: tính giá trị trung bình từng đặc trưng theo cụm, đặt tên nhóm

---

## Kết quả bắt buộc phải có

| Hạng mục | Yêu cầu |
|---------|---------|
| Biểu đồ Elbow | Inertia theo số cụm K (2–10) |
| Bảng Silhouette | Silhouette Score cho ít nhất 3 giá trị K khác nhau |
| Scatter plot 2D | Trực quan hóa cụm sau khi giảm chiều bằng PCA (2 thành phần) |
| Bảng đặc trưng cụm | Giá trị trung bình của từng cụm cho tất cả đặc trưng |
| Nhận xét chiến lược | Mô tả ≥ 1 hành động kinh doanh cụ thể cho mỗi nhóm khách hàng |

---

## Phân công gợi ý (3 ngày — 3 thành viên)

| Thành viên | Ngày 1 | Ngày 2 | Ngày 3 |
|-----------|--------|--------|--------|
| SV 1 | Tải dữ liệu, EDA, thống kê mô tả, biểu đồ phân phối | Tiền xử lý, chuẩn hóa, kiểm tra outlier | Viết báo cáo (phần dữ liệu & EDA) |
| SV 2 | Nghiên cứu thuật toán K-Means (lý thuyết) | Cài đặt K-Means, Elbow, Silhouette | Viết báo cáo (phần thuật toán & kết quả) |
| SV 3 | Chuẩn bị môi trường, nghiên cứu PCA | PCA + scatter plot, bảng đặc trưng cụm | Đặt tên nhóm, viết nhận xét chiến lược, chuẩn bị demo |

---

## Điểm cộng

- So sánh với **phân cụm phân cấp (Agglomerative Clustering)**: vẽ dendrogram, so sánh kết quả
- Thử **DBSCAN** (`sklearn.cluster.DBSCAN`) và nhận xét ưu điểm khi dữ liệu có nhiễu
- Trực quan hóa 3D bằng `matplotlib` với 3 đặc trưng quan trọng nhất

---

## Nền tảng lý thuyết liên quan

- Chương 11 (Mạng neuron): Thuật toán K-Means dùng khoảng cách Euclidean, tương tự cách neuron cạnh tranh trong **mạng Kohonen (SOM)**
- Chương 12 (Mô hình xác suất): Gaussian Mixture Model (GMM) là phiên bản xác suất của K-Means — có thể đề cập trong phần mở rộng

---

## Cấu trúc file nộp

```
project7_customer_segmentation/
├── README.md
├── download_data.py
├── data/
│   └── customers.csv
└── notebook.ipynb     ← file chính nộp kết quả
```

---

## Tiêu chí đánh giá nhanh

| Tiêu chí | Điểm |
|---------|------|
| EDA đầy đủ (≥ 4 biểu đồ + ma trận tương quan) | /2 |
| Chọn K có lý luận (Elbow + Silhouette) | /2 |
| Trực quan hóa cụm rõ ràng (PCA scatter) | /2 |
| Phân tích đặc trưng từng cụm + đặt tên | /2 |
| Nhận xét chiến lược kinh doanh | /1 |
| Điểm cộng (Hierarchical / DBSCAN / 3D plot) | +1 |
| **Tổng** | **/10** |
