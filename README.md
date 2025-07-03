# 🚀 ISP Speedtest Dashboard

A Python project that collects real internet speed data using the Speedtest CLI and visualizes key ISP performance metrics like download speed, upload speed, and ping in a sleek Streamlit dashboard. Perfect for monitoring your internet connection over time!

## 🛠️ Features

- **Automated speed test data collection** - Run tests programmatically and collect data consistently
- **Persistent data storage** - Stores results with timestamps in CSV format for historical analysis
- **Interactive dashboard** - Real-time charts showing download/upload speeds and ping over time
- **Easy deployment** - Simple, easy-to-run Python scripts with minimal setup

## 📋 Requirements

- Python 3.7+
- Required packages:
  - `speedtest-cli`
  - `pandas`
  - `streamlit`
  - `matplotlib`

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/klejvi-rekaj/isp-speedtest-dashboard.git
   cd isp-speedtest-dashboard
   ```

2. **Install required packages**
   ```bash
   pip install speedtest-cli pandas streamlit matplotlib
   ```

3. **Collect speed test data**
   ```bash
   python collect_speedtest.py
   ```

4. **Launch the dashboard**
   ```bash
   streamlit run isp_kpis.py
   ```

## 📊 Screenshots
![Screenshot 2025-07-03 210743](https://github.com/user-attachments/assets/a262ca71-847d-4bd9-baa0-cdd679455adb)
![Screenshot 2025-07-03 210808](https://github.com/user-attachments/assets/9f003f3d-0016-4d69-938b-c18f4c2d1e96)
![Screenshot 2025-07-03 210822](https://github.com/user-attachments/assets/233eb03f-5412-4515-8c78-d143bfc98f3c)


## 🎯 Usage

### Data Collection
The `collect_speedtest.py` script automatically runs internet speed tests and saves the results to a CSV file with timestamps. Run this script multiple times to build up historical data for more meaningful visualizations.

### Dashboard
The Streamlit dashboard (`isp_kpis.py`) provides:
- Interactive line charts showing speed trends over time
- Real-time metrics display
- Historical performance analysis
- Export capabilities for further analysis

## 💡 About

This project showcases automation, data collection, and real-time visualization skills using Python — great for ISP performance monitoring and portfolio demonstration!

### Key Skills Demonstrated
- **Data Collection**: Automated CLI tool integration
- **Data Storage**: CSV file handling and timestamp management
- **Data Visualization**: Interactive charts with Streamlit and Matplotlib
- **Web Applications**: Dashboard creation and deployment

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Fork the repository
- Create a feature branch
- Submit a pull request
- Report issues or suggest improvements

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📫 Contact

Created by **Klejvi Rekaj**

Feel free to reach out for questions or feedback!

- 📧 Email: klejvi.rekaj@gmail.com
---

⭐ If you found this project helpful, please give it a star!
