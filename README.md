# HTML to JPG Image Converter (Data Visualization Export)

This tool provides a professional-grade way to convert interactive HTML files (such as Plotly, Bokeh, or XGBoost model comparison charts) into static **JPG** images. It leverages **Playwright** to ensure that JavaScript-heavy visualizations are fully rendered before being captured.

## 🚀 Features

* **Batch Processing:** Automatically scans a folder for `.html` files.
* **Modern Rendering:** Uses a headless Chromium browser to handle complex animations and data legends.
* **Automated Workflow:** Includes a Windows `.bat` script for one-click execution.
* **Safe Output:** Saves all results into a dedicated `exported_images` subfolder to keep your source directory clean.

---

## 🛠️ Installation

This project uses `uv` for fast, reliable package management. To set up your environment and install the necessary dependencies, run:

```bash
# Install dependencies using uv
uv pip install -r requirements.txt

# Install the required Chromium browser engine
playwright install chromium
```

---

## 📂 Project Structure

* **`main.py`**: The core Python logic for browser automation and image capture.
* **`run_converter.bat`**: A Windows batch script that activates the environment and launches the tool.
* **`requirements.txt`**: List of necessary Python libraries (`playwright`, `python-dotenv`).

---

## 📖 How to Use

### Method 1: The One-Click Way (Recommended)
Simply double-click the `.bat` script. It will:
1.  Automatically activate your virtual environment (`.venv`).
2.  Verify that Python is installed and accessible.
3.  Launch the converter using `uv run main.py`.

### Method 2: Manual Execution
If you prefer the terminal, run:
```bash
python main.py
```
When prompted, paste the full path to your visualizations folder:  
*Example:* `C:\Users\marcel\Documents\Data Analysis Projects\...\visualizations`

---

## ⚙️ How it Works

### The Python Logic (`main.py`)
* **Path Handling:** Converts local Windows file paths into browser-friendly `file:///` URLs.
* **Smart Delay:** Implements a **1000ms pause** to allow data points and animations to finish rendering before the "shutter" clicks.
* **Full Page Capture:** Captures the entire visualization area, ensuring no legends or axes are cut off.

### The Batch Script (`.bat`)
The included `.bat` file acts as a wrapper:
* It uses `%~dp0` to ensure paths remain relative to the script's location, making it portable.
* It ensures the virtual environment is utilized, preventing "ModuleNotFoundError" issues.

---

## 📝 Notes
* **Output Quality:** Images are saved as JPEGs at **90% quality**.
* **Browser:** The script uses a headless version of Chromium (it runs in the background without opening a visible window).
