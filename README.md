# 🎓 Student Performance Prediction (Dự đoán Sinh viên Đậu/Trượt)

## 📌 Giới thiệu dự án
Dự án này là một bài toán **Phân loại nhị phân (Binary Classification)**. Mục tiêu của nhóm là xây dựng và đánh giá các mô hình Machine Learning để dự đoán khả năng qua môn (Đậu/Trượt) của sinh viên dựa trên các chỉ số học tập.

* **Label (Biến mục tiêu):** `passed` (Pass / Fail)
* **Features (Đặc trưng):** Giờ học, Chuyên cần, Điểm giữa kỳ, Số bài tập đã nộp.
* **Quy mô dữ liệu:** 200 - 500 sinh viên.

## 👥 Thành viên & Phân công nhiệm vụ (Branch)

| Thành viên | Nhiệm vụ trọng tâm | Tên nhánh làm việc (Branch) |
| :--- | :--- | :--- |
| **Nguyễn Trường Lân** | Thu thập, kiểm tra và làm sạch dữ liệu. | `task1-data-cleaning` |
| **Vũ Ngọc Yến Trâm** | Khám phá dữ liệu (EDA), phân tích và chọn feature. | `task2-eda-features` |
| **Đàm Đình Hiệp** | Chia tập Train/Test, xây Baseline model & Decision Tree. | `task3-decision-tree` |
| **Trần Tuấn Hiệp** | Chuẩn hóa dữ liệu (Scaling) & Logistic Regression. | `task4-logistic-regression` |

> **Quy ước chung cho cả nhóm:** Phần đánh giá mô hình, chạy test dự đoán thử nghiệm và làm slide thuyết trình sẽ được cả 4 thành viên cùng họp lại để thực hiện ở Ngày 3.

## 📁 Cấu trúc thư mục dự án

```text
Student-Performance-Prediction/
│
├── student_data.csv/               # Chứa dữ liệu (không push file data lớn lên Git)
│  
├── notebooks/              # Nơi chứa các file code Jupyter Notebook (.ipynb)
│   ├── 01_Data_Cleaning.ipynb     
│   ├── 02_EDA_and_Features.ipynb 
│   ├── 03_Baseline_DecisionTree.ipynb 
│   └── 04_Logistic_Regression.ipynb 
│
├── docs/       # Nơi chứa slide thuyết trình, biểu đồ, báo cáo
│
└── README.md  # File tổng quan dự án
