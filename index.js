document.addEventListener("DOMContentLoaded", function() {
    const jobTable = document.getElementById("jobTable");
    const showJobDataBtn = document.getElementById("showJobData");

    // Event listener for showing job data table
    showJobDataBtn.addEventListener("click", function() {
        showJobDataBtn.style.display = "none"; // Hide the button after clicking
        jobTable.style.display = "table"; // Display the table
        
        // Job data
        const jobData = [
            {
                job_title: "Software Engineer",
                salary: 80000,
                salary_currency: "USD",
                employee_residence: "Remote",
                experience_level: "Mid",
                company_size: "Large",
                employment_type: "Full-time",
                company_location: "San Francisco"
            },
            {
                job_title: "Data Scientist",
                salary: 90000,
                salary_currency: "USD",
                employee_residence: "On-site",
                experience_level: "Senior",
                company_size: "Medium",
                employment_type: "Contract",
                company_location: "New York"
            }
            // Add more job data as needed
        ];

        // Populate job table
        const jobTableBody = document.getElementById("jobTableBody");
        jobData.forEach(job => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${job.job_title}</td>
                <td>${job.salary}</td>
                <td>${job.salary_currency}</td>
                <td>${job.employee_residence}</td>
                <td>${job.experience_level}</td>
                <td>${job.company_size}</td>
                <td>${job.employment_type}</td>
                <td>${job.company_location}</td>
            `;
            jobTableBody.appendChild(row);
        });
    });
});
