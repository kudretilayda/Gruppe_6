# Gruppe_6
my first repository
This is my first GitHub project

# Digitaler Kleiderschrank - Group 6 Software Internship from the Hochschule der Medien

## Project Overview

### Project Name
Digitaler Kleiderschrank


### Built With
This project utilizes several robust technologies and programming languages:
- **[React](https://reactjs.org/)** - A JavaScript library for creating user interfaces.
- **[Python](https://www.python.org/)** - Version 3.10, a versatile programming language suited for a variety of applications.
- **[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)** - Essential for adding dynamic and interactive elements to web pages.
- **[Node.js](https://nodejs.org/en/)** - Version 20, facilitates server-side JavaScript execution.

## Getting Started

### Prerequisites
Ensure you have the following installed and set up:
- **API Key:** You will need an API Key to access certain project features.
- **Git:** Ensure [Git](https://git-scm.com/downloads) is installed on your machine for version control.
- **Node.js and Python:** Both [Node.js](https://nodejs.org/en/) and [Python](https://www.python.org/downloads/) should be installed.


### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/kudretilayda/Gruppe_6
      ```
3. Install project dependencies:
      ```sh
      pip install -r requirements.txt
      npm install react-scripts
      npm install @mui/material @emotion/react @emotion/styled
      ```
   
### Set up Gcloud
Choose one of the following options to set up Gcloud:
#### 1. Option
* **Set up your Gcloud account**: Follow the guidelines in the document ["Deployment on GCP WS 20-21"](URL-to-PDF) for detailed instructions.

#### 2. Option
1. **Set up a new project**: Initialize a new project by visiting [Google Cloud Console](https://console.cloud.google.com).
2. **Install Gcloud SDK**: Follow the instructions on the [Gcloud SDK installation page](https://cloud.google.com/sdk/docs/install?hl=de) to install the SDK.
3. Connect your Google Account
4. Set up a database in Cloud SQL
5. Create database within the database instance
6. Create an Bucket.
7. import the dumnpfile at "mysql/SQL-DUMP-v4.sql" into your bucket in Gcloud
8. Import SQL file into database instance
9. Connect to database with gcloud
      ```sh
     gcloud sql connect sopra-db-g07 --user=root --quiet
      ```
10. Activate "Cloud SQL"" API in Gcloud
11. Create an app in Gcloud App Engine
12. Install necessary Gcloud components:
      ```sh
      gcloud components install app-engine-python
      ```
13. Deploy your backend from the "src" directory:
      ```sh
      gcloud app deploy
      ```
14. Open your backend in a browser:
      ```sh
      gcloud app browse
      ```
15. copy your backend URL.
16. Deploy your frontend:
      ```sh
      gcloud app deploy
      ```
17. Open your frontend in a browser:
      ```sh
      gcloud app browse
      ```
18. Deploy dispatch.yaml:
       ```sh
      gcloud app deploy dispatch.yaml
      ```
19. Verify that the application is running properly.

### Authors
Group 6 - Software Internship participants
- Verena Böhner
- Moreno Contieri
- Kudret Kilic
- Aliaksei Lakhmakou
- Sertan Sepin
- Marsel Vadlja
