# 🚀 Project Name

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---
## 🎯 Introduction
Many organizations receive numerous emails daily, and manually sorting and categorizing them can be time-consuming and error-prone.
LLM-MailOps aims to automate email classification and data extraction using GEN AI (LLMs), improving efficiency, accuracy and turnaround time. 
Also, minimizing the gate keeping activities.



## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
This project is inspired by the need to automate the processing and classification of large volumes of emails. Many organizations handle a high volume of emails daily, and manually sorting and categorizing them can be both time-consuming and prone to errors. By utilizing AI, this project seeks to streamline the process, enhancing both efficiency and accuracy.

## ⚙️ What It Does
This solution utilizes a Python program powered by the ChatGPT LLM model, which is based on predefined prompts. It reads the contents of emails and attachments, comprehends the context within the lending domain, and uses this understanding to classify emails. Additionally, it extracts key data attributes from both the emails and their attachments.

## 🛠️ How We Built It

We built this solution using a combination of **Python**, **ChatGPT**, and several **open-source packages** to handle email and file processing effectively. Here’s a breakdown of the components involved in building the solution:

1. **Python as the Core Programming Language**:
   - We chose **Python** as the primary language because of its simplicity, flexibility, and vast ecosystem of libraries for data processing, machine learning, and natural language processing (NLP).
   - Python allows for easy integration with external APIs (such as ChatGPT) and provides efficient ways to handle files, such as emails and attachments.

2. **ChatGPT for Natural Language Understanding**:
   - The heart of our email classification and data extraction lies in **ChatGPT**, a state-of-the-art language model. By using **predefined prompts**, we enable ChatGPT to understand and classify emails based on their content in the **lending domain**.
   - ChatGPT helps in interpreting the context of emails, distinguishing between different types of requests, and understanding the nuances of the lending process.
   - The model’s capability allows it to generate meaningful classifications and extract key information, such as loan requests, payment inquiries, or other relevant details.

3. **Open-Source Packages for File Processing**:
   - To handle different types of attachments and email formats, we integrated **several open-source libraries** into the system, including:
   
     - **`email` library**: Used for parsing `.eml` files to extract email headers, bodies, and attachments.
     - **`PyPDF2` and `pdfplumber`**: These packages allow us to extract text from PDF files that are often attached to emails, such as loan documents, contracts, or invoices.
     - **`python-docx`**: Used for processing `.docx` files and extracting text from Word documents attached to emails.
     - **`Pytesseract` (OCR)**: For extracting text from image files (e.g., JPEG or PNG) that may be attached to the emails, enabling the processing of scanned documents or screenshots.
   
   These open-source tools help us ensure that no matter the format of the email or attachment, we can extract and process the relevant information accurately.

4. **Predefined Prompts for Classification**:
   - We developed a set of **predefined prompts** that guide **ChatGPT** to understand and classify email content based on the lending domain context. These prompts ensure that the model focuses on the specific areas of interest, such as loan inquiries, payments, account details, or other types of financial requests.
   - The classification process involves identifying the type of request (e.g., loan application, payment dispute) and categorizing emails into sub-request types, making it easier to route them to the appropriate departments.

5. **Integration and Workflow**:
   - Once the email content and attachments are extracted, the processed data is passed through the **ChatGPT model** to classify the email.
   - The classification results are then used to extract **key data attributes**, such as customer names, loan amounts, dates, or other relevant financial data from the email and its attachments.
   - The system automatically organizes the emails into predefined categories, ensuring that important requests are handled promptly and accurately.

6. **Automation and Efficiency**:
   - By combining Python’s file handling capabilities with the power of **ChatGPT** and **open-source packages**, we built a fully automated email classification system.
   - The system not only classifies emails but also extracts critical data, reducing manual effort, increasing accuracy, and accelerating response times, especially in environments with high volumes of emails like commercial lending.

Through the use of **Python**, **ChatGPT**, and various open-source libraries, we’ve created a powerful and scalable solution that automates the email classification process in the **lending domain**, streamlining workflows and enhancing overall efficiency.

## 🚧 Challenges We Faced
Implementing an effective email classification system using Large Language Models (LLMs) comes with several challenges that need to be addressed to ensure accurate and efficient processing. Below are some of the key challenges faced during the development and how they were tackled:

1. **Identifying a Model That Classifies Requests Consistently**
Challenge: Identifying a model capable of consistently classifying requests across a wide range of email content was a major challenge. LLMs, such as ChatGPT, require carefully crafted prompts to understand the problem context in a generic yet business-specific manner.

Solution: We explored multiple predefined prompts to guide the model in classifying email content accurately. The prompts were tailored to suit the lending domain while keeping the language generic enough to handle various types of email requests. This iterative process of prompt fine-tuning ensured that the model understood and classified the requests correctly across different scenarios.

2. **Handling Vague or Ambiguous Emails**
Challenge: Many emails we processed were not straightforward, and users often expressed their requests in vague or unclear ways. For instance, an email might mention a general inquiry about "loan status" without providing enough context.

Solution: LLMs helped in understanding user intent and the underlying service request even when the email content was not clear. The language model was able to infer the correct request type (e.g., loan inquiry, payment dispute) based on subtle clues in the email body. This capability made it possible to accurately classify emails with ambiguous or vague content, ensuring that requests were processed appropriately.

3. **Processing Large Files with LLMs**
Challenge: The process of extracting and classifying information from large email attachments or lengthy email threads using LLMs could be time-consuming, especially when dealing with a high volume of incoming requests.

Solution: To address the performance bottleneck caused by large file processing, we adopted asynchronous processing. This approach enabled the system to process incoming email requests in parallel, significantly improving the throughput and reducing the overall time taken for processing. Asynchronous processing allowed us to handle multiple emails and attachments concurrently without causing delays in response time.

4. **Dealing with Duplicate Email Requests**
Challenge: Email requests from users often contained duplicate or repeated submissions. This redundancy could lead to unnecessary processing and potential confusion.

Solution: To prevent redundant processing and ensure that each unique request is handled efficiently, we implemented a duplicate request detection mechanism. The system checks incoming emails against previously processed requests, identifying duplicates based on key metadata (such as subject, timestamp, and user details). Duplicates are filtered out before processing, ensuring that each request is handled only once and reducing unnecessary load on the system.

5. **Continuous Model Improvement and Fine-Tuning**
Challenge: The model's ability to classify emails accurately depends on continuous improvement and fine-tuning, as the nature of email requests can evolve over time.

Solution: We have developed a feedback loop where the system learns from user interactions and manual corrections to refine its classification accuracy. By periodically retraining the model with new email samples and updated data, we ensure the system remains effective and accurate in handling various types of email requests.



## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/ewfx/gaied-innovators
   ```
2. Install dependencies  
   ```sh
   !pip install openai langchain_openai pdfplumber pytesseract pdf2image python-docx fpdf langchain
   ```
3. Run the project  
   ```sh
   python LLM-MailOps.py
   ```

## 🏗️ Tech Stack
### **Tech Stack Overview**

Below is an overview of the core technologies used in the project:

---

#### **1. Python - Core Language for Business Logic**

- **Role**: Python serves as the backbone of the solution, handling the **business logic** and integrating various components of the system. 
- **Why Python?**:
   - **Simplicity and Flexibility**: Python is chosen for its simplicity and readability, making it easier to write and maintain the codebase. It allows rapid development and quick iteration on the business logic.
   - **Extensive Libraries and Frameworks**: Python’s vast ecosystem of libraries and frameworks enables efficient file handling (email parsing, PDF extraction, etc.), integration with AI models, and real-time data processing. Libraries like `email`, `PyPDF2`, `python-docx`, and `pytesseract` help manage different email formats and attachments, while frameworks such as `asyncio` enable asynchronous processing for performance optimization.
   - **Integration with OpenAI API**: Python’s seamless integration with external APIs, like OpenAI, allows us to easily incorporate **ChatGPT** for NLP tasks. The **OpenAI Python SDK** simplifies interactions with the API, enabling the system to leverage the power of GPT-4 for tasks like email classification and data extraction.

---

#### **2. OpenAI GPT-4 (ChatGPT) - Natural Language Processing (NLP)**

- **Role**: The **OpenAI GPT-4 (ChatGPT)** model, specifically the **gpt-4o-mini** variant, is the engine behind the **natural language understanding** and **text classification** within the system.
- **Why GPT-4 (ChatGPT)?**:
   - **Advanced NLP Capabilities**: GPT-4 is a cutting-edge language model capable of understanding and generating human-like text. It is leveraged to classify emails, extract relevant data attributes, and infer the context of the email content in the **lending domain**.
   - **Predefined Prompts**: The model is used with predefined prompts that guide it to interpret and classify emails based on their content, ensuring alignment with business requirements. This is crucial for **automating email classification** and understanding user intent in different types of requests (e.g., loan applications, payment inquiries).
   - **Data Extraction**: Beyond classification, GPT-4 helps extract important data attributes such as customer details, loan amounts, transaction dates, and other critical information from both the email body and attachments. This allows the system to perform **automated data extraction** without requiring manual intervention.
   - **Language Flexibility**: The power of GPT-4 lies in its ability to handle a wide range of natural language expressions, making it suitable for processing **ambiguous, vague, or unstructured** email requests. It can infer intent and adapt to varying email structures, ensuring high accuracy even in challenging scenarios.
   
---

#### **3. Open-Source Packages for File Processing**

In addition to Python and GPT-4, we utilize several **open-source libraries** to process and extract data from different types of email attachments. These tools ensure that the system can handle a variety of formats and accurately extract relevant data.

- **`email` Library**: Used for parsing `.eml` files to extract the email body, headers, and attachments.
- **`PyPDF2` & `pdfplumber`**: These libraries are used to extract text from **PDF** attachments, such as loan contracts, invoices, and other financial documents.
- **`python-docx`**: This library is used for extracting text from **Word documents (.docx)** attached to emails.
- **`Pytesseract` (OCR)**: OCR technology is utilized to extract text from image attachments (e.g., JPG, PNG), making it possible to process scanned documents, screenshots, or other non-text content.
  
---

#### **4. Asynchronous Processing for Performance Optimization**

- **Role**: Asynchronous processing is used to manage the high volume of incoming email requests and their attachments efficiently.
- **Why Asynchronous Processing?**:
   - **Parallel Processing**: To handle large files and email attachments that may take longer to process, we adopted an **asynchronous model** to process incoming requests concurrently. This reduces wait times and enhances the system’s ability to scale.
   - **Efficiency**: By processing multiple email requests in parallel, the system can handle **bulk email processing** more efficiently, minimizing delays in response time.
  
---

### **How These Technologies Work Together**

1. **Email Parsing**: The Python `email` library processes incoming `.eml` files, extracting the subject, body, and attachments.
2. **File Handling and Data Extraction**: Open-source libraries like `PyPDF2`, `python-docx`, and `pytesseract` are used to extract text from different file types attached to the email, such as PDF, Word, and images.
3. **Natural Language Understanding**: The content, including both the email body and attachments, is passed through **ChatGPT (GPT-4)** for classification and data extraction. The model uses **predefined prompts** to classify the email into categories (e.g., loan inquiry, payment request) and extract relevant details.
4. **Asynchronous Processing**: For large volumes of requests and files, the system uses asynchronous processing to ensure that requests are handled concurrently, improving processing speed and performance.
5. **Duplicate Detection**: A mechanism is in place to detect and filter out duplicate requests, ensuring that each unique request is processed only once.

---


## 👥 Team
- **Ashok Nagabandi**
- **Bibaswan Padhy** 
- **Jayprakash Mahankali** 
- **Prathap Reddy Chitam**
