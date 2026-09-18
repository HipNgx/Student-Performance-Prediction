# 🎓 Student Performance Prediction (Dự đoán Sinh viên Đậu/Trượt)

## 📌 Giới thiệu dự án
Dự án này là một bài toán **Phân loại nhị phân (Binary Classification)**. Mục tiêu của nhóm là xây dựng và đánh giá các mô hình Machine Learning (Decision Tree & Logistic Regression) để dự đoán khả năng qua môn (Đậu/Trượt) của sinh viên dựa trên các chỉ số học tập.

* **Label (Biến mục tiêu):** `passed` (0: Trượt, 1: Đậu)
* **Features (Đặc trưng):** Giờ học, Chuyên cần, Điểm giữa kỳ, Số bài tập đã nộp.
* **Quy mô dữ liệu:** 395 sinh viên (Dataset đã được làm sạch hoàn chỉnh).

## 👥 Thành viên & Phân công nhiệm vụ (Branch)
*Lưu ý: Không ai được push code trực tiếp lên nhánh `main`. Mọi người tạo nhánh riêng theo tên dưới đây và mở Pull Request (PR) để gộp code.*

| Thành viên | Nhiệm vụ trọng tâm | Tên nhánh làm việc (Branch) |
| :--- | :--- | :--- |
| **Nguyễn Trường Lân** | Thu thập, kiểm tra và làm sạch dữ liệu. | `task1-data-cleaning` |
| **Vũ Ngọc Yến Trâm** | Khám phá dữ liệu (EDA), phân tích tương quan. | `task2-eda-features` |
| **Đàm Đình Hiệp** | Chia tập Train/Test, xây Baseline model & Decision Tree. | `task3-decision-tree` |
| **Trần Tuấn Hiệp** | Chuẩn hóa dữ liệu (Scaling) & Logistic Regression. | `task4-logistic-regression` |

> **Quy ước chung cho cả nhóm:** Phần đánh giá mô hình, chạy test dự đoán thử nghiệm và làm slide thuyết trình sẽ được cả 4 thành viên cùng họp lại để thực hiện ở Ngày 3.

## 📁 Cấu trúc thư mục dự án (Cập nhật thực tế)

```text
Student-Performance-Prediction/
│
├── data/
│   └── student_data.csv                # Dữ liệu quy mô 395 sinh viê
│
├── notebooks/
│   ├── predict_passed_or_fail.py       # Code phân tích trung bình Đậu/Trượt 
│   ├── 03_Baseline_DecisionTree.ipynb  # Code mô hình Cây quyết định
│   └── 04_Logistic_Regression.ipynb    # Code chuẩn hóa & Logistic Regression
│
├── docs/                               # Nơi chứa slide thuyết trình, biểu đồ, báo cáo
│
└── README.md                           # File tổng quan dự án (File này)
