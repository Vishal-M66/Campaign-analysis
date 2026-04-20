# Campaign-analysis
An intelligent marketing analytics platform that helps businesses analyze campaign performance, discover best send times, compare AI vs Manual campaigns, create user personas, and optimize engagement.

# Project Overview
This project is designed to automate campaign analytics using data science and machine learning techniques. It allows users to upload campaign datasets (CSV/Excel) and generates insights such as:

✅ Best sending times by timezone  
✅ AI vs Manual campaign comparison  
✅ Open / Click / Delivery rate analytics  
✅ User persona segmentation  
✅ Dashboard reports  
✅ Actionable recommendations  

# Features

# 📂 Data Upload
- Upload campaign CSV files
- Supports structured marketing datasets

# 📊 Analytics Dashboard
- Total campaigns analyzed
- Open rates
- Click-through rates
- Delivery rates
- Conversion insights

#🌍 Timezone Optimization
Find best sending hours based on:

- EST
- IST
- GMT
- AEDT
- Custom user timezones

# AI vs Manual Comparison
Measure performance of:

- AI-generated campaigns
- Manually created campaigns

# User Persona Generator
Segment users into personas like:

- Morning Professionals
- Evening Shoppers
- Mobile Users
- Low Engagement Users

### 📈 Reports
- Downloadable PDF reports
- CSV summary exports
- 
## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3

### Backend
- Python
- Flask

### Data Analysis
- Pandas
- NumPy
- Scikit-learn

### Visualization
- Plotly
- Matplotlib

### Database
- SQLite / MySQL


## 📁 Project Structure

```bash
campaign_optimizer/
│── app.py
│── requirements.txt
│── uploads/
│── static/
│── templates/
│   ├── index.html
│   └── dashboard.html
│── reports/
│── models/

📊 Sample Insights Generated
Best send time in EST: 8 PM
Best send time in IST: 11 AM
AI campaigns outperform manual by 15%
Mobile users show highest open rates
