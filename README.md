# YouTube Downloader (Advanced)

This is an advanced YouTube downloader built in Python, offering enhanced functionality and modular design. The application supports both graphical and command-line operations, making it versatile for various use cases.

## Features

- **Cross-platform Support**: Compatible with Linux, Windows, and macOS.
- **Database Integration**: Uses SQLite (`info.db`) to store download history.
- **Notification System**:
  - Windows notifications (`windows_notification.py`).
  - macOS notifications (`mac_os_notification.py`).
- **Customizable Themes**: Located in the `theme` directory.
- **Shell Script for Linux**: (`tubefetch.sh`) simplifies download tasks on Linux systems.
- **Modular Design**: Functions are divided into utilities, notifications, and SQL operations for easy maintenance.

## Project Structure

```plaintext
idea/                  # Development files or notes
__pycache__/           # Compiled Python bytecode
assets/                # Contains assets like images or icons for the application
theme/                 # Themes and customization files
venv/                  # Virtual environment (recommended for dependencies)
__init__.py            # Package initializer
info.db                # SQLite database for storing download history
launcher.py            # Entry point for launching the application
mac_os_notification.py # macOS notification integration
main.py                # Main application logic
menu_spawn.py          # Code to spawn menus or GUI components
notify.py              # Notification handler
sql.py                 # SQL database interactions
tubefetch.sh           # Shell script for Linux users
utils.py               # Utility functions
windows_notification.py# Windows notification integration
```

## Requirements

- Python 3.7 or higher
- SQLite (pre-installed with Python)

### Python Libraries
The required Python libraries are:
- `tkinter`
- `sqlite3`
- `subprocess`
- `os`
- `sys`
- `shutil`
- `platform`

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/advanced-yt-downloader.git
cd advanced-yt-downloader
```

### Step 2: Set Up Virtual Environment (Optional but Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate    # On Windows
```

### Step 3: Install Dependencies
Ensure the required libraries are installed:
```bash
pip install -r requirements.txt
```

### Step 4: Configure Themes (Optional)
Customize the application appearance using files in the `theme/` directory.

## Usage

### Linux Users
- Run the shell script:
```bash
./tubefetch.sh
```

### Windows/macOS Users
- Launch the application using the `launcher.py` file:
```bash
python launcher.py
```

### Key Files
- **Main Application**: `main.py`
- **Menu Control**: `menu_spawn.py`
- **Notifications**:
  - macOS: `mac_os_notification.py`
  - Windows: `windows_notification.py`
- **Database Operations**: `sql.py`
- **Utilities**: `utils.py`

## Notes
- Ensure the `info.db` file is writable for proper functioning of the database.
- For Linux users, make `tubefetch.sh` executable:
```bash
chmod +x tubefetch.sh
```
- Notification support requires OS-specific dependencies.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
