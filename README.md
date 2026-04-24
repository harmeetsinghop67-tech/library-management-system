📚 Library Management System (Python)

A simple command-line based Library Management System built using Python. This project allows users to manage books efficiently by adding, viewing, issuing, and returning them, along with automatic fine calculation for late returns.

🚀 Features
➕ Add new books to the library
📖 View all available books
📕 Issue books to students with a return deadline
🔄 Return books and calculate late fines
💰 Fine system based on delay duration
🧾 Tracks issued books with date and student details
🛠️ Tech Stack
Python 🐍
Built-in libraries (datetime)
Console-based interface
📂 Project Structure
library-management-system/
│
├── main.py        # Main program file
└── README.md      # Project documentation
⚙️ How It Works
Run the program
Choose options from the menu:
Add Book
Show Available Books
Issue Book
Return Book
System updates records dynamically
Fine is calculated automatically if the book is returned late
💸 Fine Calculation Logic
₹10 per day for first 7 days
₹20 per day for next 7 days
₹60 per day after 14 days
▶️ How to Run
python main.py
📸 Sample Menu
========================================
 LIBRARY MANAGEMENT SYSTEM
========================================
1. Add Book
2. Show Available Books
3. Issue Book
4. Return Book
5. Exit
========================================
🎯 Future Improvements
GUI version using Tkinter or PyQt
Database integration (SQLite/MySQL)
User authentication system
Book search & category features
🤝 Contributing

Feel free to fork this repo and improve the project. Pull requests are welcome!

📜 License

This project is open-source and available under the MIT License.
