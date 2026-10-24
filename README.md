\# Unified Business Hub



\## Project Description



Unified Business Hub is a centralized business management platform designed for small-business owners who operate one or multiple businesses. The application will connect existing business software, such as QuickBooks, Toast, and Square, into one dashboard. It will also use artificial intelligence to extract information from invoices and receipts, organize financial records, and help owners monitor revenue, expenses, and overall business performance.



\## Project Status



\*\*Status:\*\* Planning and initial development. The repository structure and project requirements are being established.



\## Planned Features



\- Centralized dashboard for multiple businesses

\- Integration with existing POS and accounting systems

\- AI-powered invoice and receipt processing

\- Financial reporting and analytics

\- AI-assisted business insights



\## Module 6 — Capstone Checkpoint



\### Application Status



The Unified Business Hub is a Streamlit application designed to help small-business owners manage business information in one place.



The current working version focuses on supplier invoice management.



\### Completed User Stories



\- \*\*US1 — Save invoices:\*\* As a business owner, I can enter supplier information, invoice number, date, amount, and description and save the invoice.

\- \*\*US2 — Search invoices:\*\* As a business owner, I can search previously saved invoices by vendor or invoice number.

\- \*\*Data persistence:\*\* Invoice records are saved locally in JSON format and remain available after restarting the application.

\- \*\*Dashboard:\*\* The application displays recorded invoice counts and expenses.



\### In Progress



\- Improving dashboard reporting and financial summaries.

\- Preparing the application for SQLite storage.

\- Developing the invoice upload and AI extraction workflow.



\### Not Started



\- QuickBooks and Toast integrations.

\- Payroll and inventory management.

\- Multi-business management.

\- Advanced financial reporting.

\- User authentication and permissions.



\### Scope Changes



The original proposal described a centralized platform integrating multiple business-management systems.



For the Module 6 checkpoint, the scope has been reduced to a working invoice-management application. This allows the team to demonstrate two complete user stories and persistent data before expanding into AI extraction and external integrations.



The invoice upload interface is visible, but automatic document extraction is not yet implemented.



\### Running the Application



1\. Clone the repository.

2\. Open the project directory.

3\. Create and activate a Python virtual environment.

4\. Install dependencies using `python -m pip install -r requirements.txt`.

5\. Start the application using `python -m streamlit run app.py`.

6\. Open the local address displayed by Streamlit.



No API credentials are required for the current functionality. Invoice data is stored locally in `data/invoices.json`, which is excluded from Git.



\### AI Use Disclosure



ChatGPT was used to assist with application structure, Streamlit interface development, JSON storage, search functionality, documentation, and troubleshooting. The application was run and tested locally.

