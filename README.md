# Study-Case-AutomationExercises

This repository contains various **Study Cases for Test Automation** from https://automationexercise.com/, designed to demonstrate solutions for real-world challenges commonly found during automated test development. The goal is to apply best practices in test structure, design patterns, and reporting.

---

## ✨ **Key Features and Focus Areas**

- **Real-World Scenarios:** Simulates real testing environments and problems.  
- **Best Practices:** Application of the **Page Object Model (POM)** and **BDD philosophy** to ensure clean, maintainable, and scalable code.  
- **Resilience:** Focus on creating robust tests that handle synchronization and environmental issues (using WebDriver Manager and explicit waits).

---

## 🚀 **Technologies Used**

| Technology               | Description                                               |
|-------------------------|-----------------------------------------------------------|
| **Python**              | Primary automation language. |
| **Behave**              | BDD framework using Gherkin syntax. |
| **Selenium WebDriver**  | Browser automation API. |
| **WebDriver Manager**   | Automatic ChromeDriver management. |
| **Page Object Model (POM)** | Architectural pattern separating UI locators and logic. |

---

## 🏗️ **Architectural Structure (Advanced BDD)**

The project follows the **Single Responsibility Principle (SRP)** to maintain clean and modular code:

```
.
├── features/
│   ├── login/
│   │   └── register.feature   # BDD scenarios written in Gherkin
│   └── steps/                 # Step definitions (@given, @when, @then)
├── pages/                     # Page Object Model (Locators & UI interactions)
├── drivers/                   # WebDriver management
└── utils/                     # Helper utilities (Logger, Data Generator, etc.)
```

---

## 📋 **Prerequisites**

You must have:

- **Python 3.8+**  
- **Google Chrome** installed (webdriver-manager handles ChromeDriver automatically)

---

## 💻 **Installation & Setup**

### **1. Clone the Repository**

```bash
git clone https://github.com/RenzoDTavares/Study-Case-AutomationExercises.git
cd Study-Case-AutomationExercises
```

### **2. Create and Activate a Virtual Environment**

```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶️ **Running the Tests**

The project uses **Behave** as its test runner.

### **Run Specific Scenarios**

```bash
behave features/register/register.feature
```

### **Run by Tag**

```bash
behave --tags=@register
```

### **Verbose Output**

```bash
behave -v
```

---



