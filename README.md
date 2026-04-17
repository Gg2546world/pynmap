# Pynmap - Advanced Network & Port Scanner

A professional, modular network and port scanning tool built with Python. It features a structured architecture and utilizes multi-threading (Thread Pooling) to ensure high-speed performance and efficiency.

## 🚀 Features
- **Network Scanning (SN):** Discover active devices within a local network (subnet).
- **Port Scanning (SP):** Scan thousands of ports rapidly using a concurrent Thread Pool.
- **Service Detection:** Identifies common services (HTTP, SSH, etc.) associated with open ports.
- **Advanced Logging:** All operations and errors are documented in dedicated log files for debugging.
- **ANSI Color UI:** Clean, elegant, and readable terminal output with custom renderers.
- **Performance Tracking:** Built-in decorators to measure and display scan duration.

## 📂 Project Structure
The project follows a **Modular Architecture** to ensure maintainability:
- `scanner/`: Core logic for network and port discovery.
- `concurrency/`: Management of the Thread Pool executor.
- `ui/`: Terminal styling, ANSI colors, and cursor control.
- `config/`: Centralized logger and path configurations.
- `utils/`: Helper functions, IP validation, and custom decorators.

## 🛠️ Installation
```bash
# Clone the repository
git clone https://github.com/Gg2546world/pynmap.git

# Enter the project directory
cd pynmap

# Setup the script as system command
chmod +x setup.sh
./setup.sh
