# 📊 Production Loss Management System

A **Production Loss Management System** built using **Python, Streamlit, SQLite, and Plotly** to monitor daily production, analyze losses, and generate interactive reports for manufacturing environments.

This project was developed to simplify production tracking, visualize performance, and provide insights into production efficiency through an easy-to-use dashboard.

---

## 🚀 Features

### 📋 Production Management
- Add new production records
- View all production records
- Search records by:
  - Date
  - Shift
  - Operator
  - Record ID

### 📈 Production Analysis
- Overall Production Summary
- Shift-wise Production Analysis
- Production Efficiency Calculation
- Interactive Charts
- KPI Metrics

### 📄 Reports
- Daily Report
- Weekly Report
- Custom Date Range Report

### 📊 Dashboard
- Interactive Streamlit UI
- Plotly Visualizations
- Production KPIs
- Shift Comparison Charts
- Responsive Layout

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Logic |
| Streamlit | Dashboard UI |
| SQLite | Database |
| SQL | Data Queries |
| Plotly | Interactive Charts |
| Pandas | Data Processing |
| Datetime | Date Handling |

---

## 📁 Project Structure

```
ProductionLossManagementSystem/
│
├── app.py
├── database.py
├── analysis.py
├── reports.py
├── charts.py
├── config.py
├── requirements.txt
│
├── database/
│   └── production.db
│
├── assets/
│
├── pages/
│
└── utils/
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/ProductionLossManagementSystem.git
```

### 2. Go to Project Folder

```bash
cd ProductionLossManagementSystem
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Application

```bash
streamlit run app.py
```

---

## 🗄️ Database

The project uses **SQLite** for storing production records.

Sample fields:

| Field | Description |
|------|-------------|
| ID | Record ID |
| Date | Production Date |
| Shift | A / B / C |
| Target | Target Production |
| Actual | Actual Production |
| Reason | Production Loss Reason |
| Operator | Operator Name |

---

## 📊 Dashboard Includes

- Total Production
- Total Target
- Production Efficiency
- Shift-wise Production
- Daily Reports
- Weekly Reports
- Production Comparison
- Interactive Bar Charts

---


## 📌 Future Improvements

- User Authentication
- Export Reports to Excel
- Export Reports to PDF
- Monthly Dashboard
- Yearly Dashboard
- Machine-wise Analysis
- Department-wise Analysis
- Dark Mode
- Cloud Deployment

---

## 💡 Learning Outcomes

Through this project, I learned:

- Python Project Structure
- SQLite Database Management
- SQL Queries
- Streamlit Dashboard Development
- Plotly Data Visualization
- Data Analysis
- KPI Calculation
- Report Generation
- CRUD Operations

---

## 👨‍💻 Author

**Sunny Singh**

B.Tech Computer Science Engineering

Lovely Professional University

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
