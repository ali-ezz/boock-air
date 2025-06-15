# ✈️ Airline Ticket Booking System

A Python-based console application that allows users to book, cancel, and manage airline tickets, while providing admin control over flights, tickets, and logs.

---

## 🧭 Overview

This command-line system simulates an online flight booking platform with features for both **users** and **administrators**. It supports seat selection, payment simulation, flight management, and ticket generation using file-based storage.

---

## 👥 Roles & Key Features

### 🧑‍💼 Admin
- View all registered flights  
- Add, delete, or modify flights  
- View all events on the system (site activity logs)  
- Generate e-tickets for users

### 👤 User
- Sign up & log in  
- Book or cancel a flight (cancellation applies a fine)  
- Choose a seat during booking  
- Simulate payment by credit card  
- Edit personal account data  
- View history of past and upcoming flights

---

## 🛠️ Tech Stack

- Python 3  
- File-based data storage (`.txt` files)  
- Command-Line Interface (CLI)

---

## 📁 File Structure

- `book_air.py` — the main logic of the system  
- `README.md` — this file  

---

## ▶️ How to Run

```bash
git clone https://github.com/ali-ezz/boock-air.git
cd boock-air
python main.py
