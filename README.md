# Varsity Query

## Description
Varsity Query is a Q&A application for Zerodha Varsity Modules. The modules can be found [here](https://zerodha.com/varsity/modules/).

## Prerequisites
To run this application, you will need an API key. You can create your `OPENAI_API_KEY` [here](https://platform.openai.com/account/api-keys).

## Run Locally

To run the Varsity RAG Q&A application locally, follow these steps:

1. **Clone the GitHub Repository**
   - Clone the repository from GitHub using the following command:
     ```bash
     git clone https://github.com/iamsobasak/varsity_rag.git
     ```
   - Navigate to the project directory:
     ```bash
     cd varsity_rag
     ```

2. **Create a `.env` File**
   - Create a file named `.env` in the root directory of the project.
   - Add your `OPENAI_API_KEY` to the `.env` file in the following format:
     ```env
     OPENAI_API_KEY=your_api_key_here
     ```

3. **Install Requirements**
   - Install the required packages by running the following command:
     ```bash
     pip install -r requirements.txt
     ```

4. **Ingest Files**
   - Run the following command to execute the `ingest_files.py` script:
     ```bash
     python ingest_files.py
     ```

5. **Run the Application**
   - Start the application by running the following command:
     ```bash
     streamlit run home.py
     ```

This will launch the Varsity RAG Q&A application in your default web browser.

