#!/usr/bin/env python
# coding: utf-8

# # Commercial Lending service Email & document classification
# - Uses gpt-4o-mini to classify emails into Request Type, Sub Request Type and extract keyword.
# 

# In[1]:


get_ipython().system('pip install openai langchain_openai pdfplumber pytesseract pdf2image python-docx fpdf langchain')


# ## Import the libraries

# In[2]:


from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

import os
import openai
import json

import email
import pdfplumber
import pytesseract
from email import policy
from email.parser import BytesParser
from bs4 import BeautifulSoup
from PIL import Image
from pdf2image import convert_from_path
from docx import Document
from io import BytesIO
import json 
from datetime import datetime
import asyncio


# ## Configure the API key for using the Open API and set the local directory as the input source to process the documents.

# In[3]:


folder_path = "C:\\Users\\Jayaprakash\\hackathon\\input-dataset"

openai.api_key = "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"
os.environ["OPENAI_API_KEY"] = openai.api_key


# ### Extract text from an email in EML format, including its attachments.

# In[4]:


def extract_email_text(eml_file_path):
    with open(eml_file_path, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)

    subject = msg["subject"]
    body = None

    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain":
                body = part.get_payload(decode=True).decode(errors="ignore")
            elif content_type == "text/html":
                soup = BeautifulSoup(part.get_payload(decode=True), "html.parser")
                body = soup.get_text()
    else:
        body = msg.get_payload(decode=True).decode(errors="ignore")

    return subject, body

# Extract text from PDF.
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

# Extract text from images using OCR
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text.strip()

# Extract text from DOCX files
def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])
    
# Extract text from text file
def extract_text_from_file(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the content of the file
            content = file.read()
        return content
    except FileNotFoundError:
        return "The file was not found."
    except IOError:
        return "An error occurred while reading the file."

# Process email with attachments
def process_email_with_attachments(eml_file_path, attachment_dir="attachments"):
    subject, body = extract_email_text(eml_file_path)

    # Create a directory to store attachments if it doesn't exist
    os.makedirs(attachment_dir, exist_ok=True)

    # Extract attachments
    with open(eml_file_path, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)

    attachment_texts = []
    for part in msg.walk():
        content_disposition = part.get("Content-Disposition")
        if content_disposition and "attachment" in content_disposition:
            filename = part.get_filename()
            attachment_path = os.path.join(attachment_dir, filename)

            with open(attachment_path, "wb") as file:
                file.write(part.get_payload(decode=True))

            if filename.endswith(".pdf"):
                attachment_texts.append(extract_text_from_pdf(attachment_path))
            elif filename.endswith(".docx"):
                attachment_texts.append(extract_text_from_docx(attachment_path))
            elif filename.endswith((".png", ".jpg", ".jpeg")):
                attachment_texts.append(extract_text_from_image(attachment_path))

    return {
        "subject": subject,
        "body": body,
        "attachments_text": attachment_texts
    }


# In[5]: Remove Duplicates in the Directory


def removeDuplicates(dict):
    new_dict = {}
    seen_values = set()
    
    for key, value in dict.items():
        if value not in seen_values:
            new_dict[key] = value
            seen_values.add(value)
    return new_dict


# ### Schema for extracting the request type, sub-request type, and keywords in JSON format.

# In[6]:



functions = [
    {
        "name": "classify_email",
        "description": "Classifies the email into a request type and sub-request type",
        "parameters": {
            "type": "object",
            "properties": {
                "request_type": {
                    "type": "string",
                    "description": "The high-level category of the request"
                },
                "sub_request_type": {
                    "type": "string",
                    "description": "The specific sub-category under the request type"
                },
               "keywords": {
            "type": "array",
            "description": "Top key words",
            "items": {
              "type": "string"
            }
          }
            },
            "required": ["request_type", "sub_request_type", "keywords"]
        }
    }
]


# In[7]:

def get_chat_completions(user_input, functions):

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=user_input,
        functions=functions,
        function_call="auto"
    )
    # Extract the function call result
    return response.choices[0].message


# In[9]:


def initialize_conversation(email_text):
    predefined_request_types = """
    Request Types:
    - Adjustment: the term "Adjustment" refers to any modification or correction made to the terms or conditions of a loan or credit facility. This could involve changes to the amount of the loan, interest rates, repayment schedules, or other terms that affect how the loan is structured or managed. Adjustments can occur for various reasons, and they are typically done to accommodate the borrower’s financial situation or to ensure compliance with the bank's policies and regulations.
    - AU Transfer: AU Transfer refers to the process of transferring funds or assets related to a loan or financial transaction, typically within an Australian (AU) banking environment. The term AU Transfer may be used in several specific ways, often related to both inbound and outbound transactions. Below is an explanation of how AU Transfer might function in the banking domain, particularly in the context of lending services.
    - Closing Notice: Closing Notice is a formal notification issued to the borrower when the loan is about to be fully paid off, settled, or when the lender is closing or concluding the loan account. This notice serves as a confirmation and summary of the loan's final status, and it typically occurs after the borrower has made the final payment or fulfilled all terms of the loan agreement.

                      The Closing Notice is an essential document in the life cycle of a loan because it marks the official end of the loan contract and provides clarity on the loan’s closure.(Sub Request Type: Reallocation Fees, Amendment Fees, Reallocation Principal )
    - Commitment Change:  Commitment Change refers to a formal modification or adjustment made to the terms or conditions of a credit facility or loan agreement. These changes can occur after the initial loan approval and are typically made to better align with the borrower’s financial situation, the market environment, or the lender's internal policies. Commitment changes can affect various aspects of the loan, such as the loan amount, interest rate, repayment schedule, collateral requirements, or the overall terms of the agreement.(Sub Request Type: Cashless Roll, Decrease, Increase)
    - Fee Payment: Fee Payment refers to the process by which a borrower pays fees associated with a loan or credit facility. These fees are typically charged by the bank for various administrative, service, or processing tasks related to the loan. Fees can be either one-time charges or recurring, and they are typically outlined in the loan agreement.

                   Fee Payments are an important aspect of loan servicing, as they represent additional costs beyond the principal loan amount and interest rate.(Sub Request Type: Ongoing Fee, Letter of Credit Fee)
    - Money Movement-Inbound: Money Movement - Inbound refers to the process by which funds are received or deposited into a bank’s system, typically related to the repayment of a loan or credit facility. This movement involves incoming cash flows from the borrower or a third party, such as a guarantor, investor, or another financial institution. These funds may be used to pay down the loan balance, pay interest, or settle any associated fees.

                              The Inbound Money Movement process is a key part of loan servicing and collections in commercial banking, ensuring that repayments are properly applied to the borrower’s account and that the loan balance is correctly adjusted.(Subtypes: Principal, Interest, Principal + Interest, Principal+Interest+Fee)
    - Money Movement-Outbound: Money Movement - Outbound refers to the process by which funds are disbursed or transferred out of the bank to the borrower or a third party. It generally refers to the flow of money from the bank to a borrower or recipient, either as a loan disbursement, a payment to a vendor or service provider, or a transfer related to the loan agreement.

                   This outbound movement of funds is an essential part of the lending process, as it represents the fulfilment of the bank’s obligation to provide the agreed-upon funds to the borrower or other stakeholders. (Subtypes: Timebound, Foreign Currency)
    """

    classification_prompt = f"""
    Below are the predefined request categories:

    {predefined_request_types}
 
    You are an AI assistant. Please analyse the following email and classify it into one of the categories **Request Type**, **Sub Request Type**.
    Then extract key information such as deal name ,expiration date, amount etc with its values.
    Include key information with value from given content.

    Email:
    "{email_text}"

    Ensure the classification follows the provided categories. If the email does not match any, return "Unknown".
    Provide the classification and extracted key information details in JSON format.
    """
    return [{"role": "system", "content": "You are a subject matter expert in Commercial Bank Lending Service teams who classifies emails based on predefined request types and sub-request types."},
            {"role": "user", "content": classification_prompt}]


# In[ ]:


async def processDirectory(directory):
    processed_emails = {}
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path): 
            if filename.endswith(".pdf"):
                processed_email = extract_text_from_pdf(file_path)
            elif (filename.endswith(".docx")):
                processed_email = extract_text_from_docx(file_path)
            elif filename.endswith((".msg", ".eml")):
                processed_email = process_email_with_attachments(file_path)
            elif filename.endswith((".png", ".jpg", ".jpeg")):
                processed_email = extract_text_from_image(file_path)
                
            processed_emails[filename] = processed_email
    print (f"input file count: {len(processed_emails)}")
    processed_emails = removeDuplicates(processed_emails)
    print (f"after removing duplicats file count: {len(processed_emails)}")

    classification_results = await processDataAsync(processed_emails)
    if not os.path.isdir("results"): 
        os.makedirs("results") 
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    base_filename = "results/classification_results"
    # Create a unique filename by appending the timestamp
    unique_filename = f"{base_filename}_{timestamp}.json"
    with open(unique_filename, "w") as outfile: 
        json.dump(classification_results, outfile)


# In[ ]:


async def processData(filename, data): 
    print (f"processing: {filename}")
    conversation = initialize_conversation(data)
    email_classification = get_chat_completions(conversation, functions)
    email_classification_json = email_classification.function_call.arguments
    print (f"completed processing: {filename}")
    return filename, email_classification_json
    
async def processDataAsync(processed_emails):
    tasks = [processData(filename, data) for filename, data in processed_emails.items()]
    results = await asyncio.gather(*tasks)
    result_dict = dict(results)
    return result_dict


# In[ ]:


await processDirectory("C:\\Users\\Jayaprakash\\hackathon\\input-dataset")

