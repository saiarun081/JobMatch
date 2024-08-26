# JobMatch

## Motivation
JobMatch aims to revolutionize the job search process by providing personalized job recommendations tailored to each user's skills, experience, location, salary expectations, job type preferences, and desired company culture. In today's competitive job market, it can be challenging for job seekers to find opportunities that align with their specific criteria. JobMatch leverages advanced algorithms and cloud-based technologies to match candidates with relevant job openings, thereby streamlining the job search process and maximizing the chances of finding the perfect job fit.

## Importance of Finding the Right Job
Finding the right job is essential for individuals to achieve career satisfaction, personal growth, and financial stability. The ideal job not only matches the candidate's skills and experience but also aligns with their values, interests, and career aspirations. By focusing on roles that offer opportunities for professional development, work-life balance, and a positive company culture, individuals can enhance their job satisfaction, productivity, and overall well-being.

## System Architecture

![image](https://github.com/user-attachments/assets/2bb2c6b6-f3ec-4b42-9abc-5ba179812492)

### Tools & Technologies
- **Platform:** Amazon Web Services
- **Storage:** DynamoDB, S3
- **Compute Services:** Lambda Function
- **API Management:** AWS API Gateway
- **Frontend Web:** AWS Amplify
- **IDE:** Visual Studio Code
- **Programming Languages:** HTML, CSS, JavaScript, Python
- **Versioning:** GitHub

## Features
Our team has successfully developed and deployed a single-page responsive webpage called "Job Data" on AWS. Below are some features of our application:

- Users are greeted with an interface titled “Job Data” that has two buttons: “Fetch Job Descriptions” and “Select Job Title”.
- A table below the title displays columns for Job Title, Salary, Currency, Employee Residence, Experience Level, Company Size, Employment Type, Company Location, and JobmatchID.
- The table contains specific details about various job roles, including salary in USD and other relevant information.
- We have implemented an API in an AWS Lambda function that fetches the list of categories (unique values) from DynamoDB. This API is integrated and deployed on AWS API Gateway and used in the user interface development.
  
![image](https://github.com/user-attachments/assets/eec23e4b-c39e-4884-b4a9-404ab0cce1ca)

### User Interaction
- The dropdown menu labeled “Select Job Title” shows various job title options for filtering, including Data Engineer, Data Scientist, Research Engineer, and more.
  
![image](https://github.com/user-attachments/assets/36212575-1a14-4dc8-8936-c5e6d9c4b960)

- Upon clicking "Fetch Job Descriptions", a pop-up window prompts the user to enter a Job ID, enabling them to search or filter job listings based on a specific Job ID.
  
![image](https://github.com/user-attachments/assets/8a8340d9-d148-4567-854e-90c8edfdbcae)

- The job description matching the JobmatchID is displayed, providing key details such as salary, company size, and location.

![image](https://github.com/user-attachments/assets/f9ffdb19-df56-4f99-a591-e2a0fedcf939)

## Technical Details
### Steps Followed

#### Step 1: 
- In AWS S3, create a bucket and upload the CSV files. The dataset is large, so it was chunked into multiple CSV files.


![image](https://github.com/user-attachments/assets/2767feaf-cab0-46e2-b733-8f59ba986d03)

![image](https://github.com/user-attachments/assets/96116713-9a1c-4a26-99a6-817966ca0115)

#### Step 2: 
- Create a table called “jobmatchdata” in DynamoDB.

![image](https://github.com/user-attachments/assets/1b55f161-7f2c-43e9-8a5b-ed4b77f7961b)

![image](https://github.com/user-attachments/assets/d94c36e3-bdcd-470a-8d23-57e4b0f7338d)

![image](https://github.com/user-attachments/assets/6f68e8e6-9dd5-44cf-8b75-5cf9649f1f25)

- Write an AWS Lambda function called “jobmatchtodynamo” to read the CSV file and write the data to DynamoDB.

![image](https://github.com/user-attachments/assets/723be536-939a-43a1-a7c2-3d536916910a)

![image](https://github.com/user-attachments/assets/d3be5a6d-1cb9-4682-8905-de726bbaa240)

![image](https://github.com/user-attachments/assets/ede69f75-5c2f-44df-a25d-44fc456498f2)

![image](https://github.com/user-attachments/assets/e67f9854-fd7a-45df-974f-0c159f65b289)

![image](https://github.com/user-attachments/assets/9c811c8c-1c32-4cb4-bdd4-a4ec8e086302)

![image](https://github.com/user-attachments/assets/f18ddd6c-cae9-45fa-af3d-06281021008b)

#### Step 3: 
- Develop multiple APIs (Lambda functions) to meet the data requirements for the user interface:
  - `getAllJobDescriptions` - Fetch all job information from DynamoDB.
  - `getJobDescriptionByID` - Fetch data based on a specific JobmatchID.

 ![image](https://github.com/user-attachments/assets/15bc375a-72d6-47fd-b797-4fc935ec3a5b)

 ![image](https://github.com/user-attachments/assets/b9456bb0-466f-4498-b3f5-71152bd6ac0c)

![image](https://github.com/user-attachments/assets/bc600c38-25c6-406c-9964-efd2f47e832d)

![image](https://github.com/user-attachments/assets/e07cef01-be16-4479-8f19-591ce17d824f)

 ![image](https://github.com/user-attachments/assets/6d8bd83f-f42d-4248-bad7-6d5b1df96d30)

#### Step 4: 
- Configure permissions in IAM (Identity Access Management) to allow Lambda functions to invoke DynamoDB.

![image](https://github.com/user-attachments/assets/ad885d75-2ebc-418e-99bf-615ee311508d)

![image](https://github.com/user-attachments/assets/759fbc25-36cb-4b3d-85f4-d2f3f58cf9ab)

#### Step 5: 
- Expose the APIs using AWS API Gateway, allowing them to be accessed externally.
- In AWS API Gateway, create a REST API, define the necessary HTTP methods, and integrate them with the Lambda functions. After testing and deployment, the API can be accessed via a provided link.

![image](https://github.com/user-attachments/assets/3fd95579-c991-4586-a1c7-d102d4cf5ff9)

![image](https://github.com/user-attachments/assets/54c78b01-d65f-4234-9e00-66a467bcf3de)

![image](https://github.com/user-attachments/assets/d963c8dd-8489-4b35-8406-f5baba347ebd)

![image](https://github.com/user-attachments/assets/475e6925-53dd-4475-89ed-1d254a4d909f)

![image](https://github.com/user-attachments/assets/eb752fd9-93ec-43d0-b146-f7fc619593c1)

#### Step 6: 
- Once the backend setup is complete, begin the UI design and upload the code to GitHub.
- Deploy the code in AWS Amplify by linking the GitHub branch to Amplify. After successful deployment, the website will be accessible through a provided link.

![image](https://github.com/user-attachments/assets/24d6426e-b31f-48d0-958d-562e54e5e046)

![image](https://github.com/user-attachments/assets/62255f85-e5ec-4375-be1e-74135a995306)

![image](https://github.com/user-attachments/assets/214467ce-78c4-4420-ba58-79e82d6c2500)

![image](https://github.com/user-attachments/assets/9625bf3c-4ea0-4038-ad44-2ae0b23d0293)

## Externally Accessible Website
- **Website Link:** [JobMatch](https://main.d2pay4xgzuye20.amplifyapp.com/)

## Link to the Code
- **GitHub Repository:** [JobMatch](https://github.com/saiarun081/JobMatch/tree/main)
  - [Frontend](https://github.com/saiarun081/JobMatch/tree/Frontend)
  - [Backend](https://github.com/saiarun081/JobMatch/tree/Backend)

## Link to the Demo Video
- [Demo Video](https://drive.google.com/file/d/1b_FKXn4ALaKZhgPG3pmWb9D065kCz1Gz/view?usp=sharing)

## Future Improvements
- Deploy more data.
- Add more filters to optimize user search and sorting.
- Optimize the code.


