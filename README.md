# 🕹️ Tic Tac Toe - Low Level Design Project

A clean, extensible, object-oriented implementation of the classic Tic Tac Toe game using Python.  
This project demonstrates strong understanding of **Low-Level Design (LLD)** principles including encapsulation, abstraction, modularity, and separation of concerns.

> This repo includes full source code, **HLD/LLD design documents**, and **UML diagrams**.

---

## 📌 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Design Overview](#design-overview)
  - [High-Level Design (HLD)](#high-level-design-hld)
  - [Low-Level Design (LLD)](#low-level-design-lld)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Extensibility Ideas](#extensibility-ideas)
- [License](#license)

---

## ✅ Features

- 🧱 Clean class design using OOP
- 🎯 HLD and LLD documentation included
- 🧩 UML class diagram included
- ✅ Move validation and winner detection
- 🧪 Easy to extend (e.g., AI player, 4x4 board)

---

## 🧰 Tech Stack

- Language: **Python 3.x**
- Diagram: [draw.io](https://draw.io), Mermaid (optional)
- IDE: VSCode / PyCharm

---

## 🧠 Design Overview

### 📐 High-Level Design (HLD)

The system is broken down into 3 core components:

- `Game` → Handles flow control and game logic
- `Board` → Manages 2D grid, move validation, winner checks
- `Player` → Represents individual players with symbols

📄 See: [`HLD/tic_tac_toe_hld.md`](HLD/tic_tac_toe_hld.md)

---

### 🧩 Low-Level Design (LLD)

- Follows SRP, encapsulation, and modularity
- Classes:
  - `Player`
  - `Board`
  - `Game`
- Each class is unit-testable and extensible

📄 See: [`LLD/tic_tac_toe_uml.md`](LLD/tic_tac_toe_uml.md)  
📷 UML Diagram: ![Class Diagram](LLD/class_diagram.png)

---

## 🚀 Getting Started

### 🔧 Requirements
- Python 3.7 or above

### 🛠️ Setup

```bash
# Clone the repositor
