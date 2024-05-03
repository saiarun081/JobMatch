document.addEventListener("DOMContentLoaded", function() {
    const jobTableBody = document.getElementById("jobTableBody");
    const fetchJobDescriptionBtn = document.getElementById("fetchJobDescription");
    const jobTitlesDropdown = document.getElementById("jobTitlesDropdown");

    let jobData; // Variable to store the job data

    fetch("info.json")
        .then(response => response.json())
        .then(data => {
            jobData = data; // Store the job data in the variable
            // Populate job titles dropdown
            const uniqueJobTitles = [...new Set(jobData.map(job => job.job_title))];
            uniqueJobTitles.forEach(title => {
                const option = document.createElement("option");
                option.value = title;
                option.textContent = title;
                jobTitlesDropdown.appendChild(option);
            });

            // Populate job table
            // Populate job table
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
        <td>${job.JobmatchID}</td> <!-- Add JobmatchID column -->
    `;
    jobTableBody.appendChild(row);
});
        })
        .catch(error => console.log("Error:", error));

    // Event listener for fetching job description
// Event listener for fetching job description
fetchJobDescriptionBtn.addEventListener("click", function() {
    let jobDescription = "Job Descriptions:\n";
    jobData.forEach(job => {
        jobDescription += `
            Job Title: ${job.job_title}
            Salary: ${job.salary} ${job.salary_currency}
            Employee Residence: ${job.employee_residence}
            Experience Level: ${job.experience_level}
            Company Size: ${job.company_size}
            Employment Type: ${job.employment_type}
            Company Location: ${job.company_location}
            JobmatchID: ${job.JobmatchID}\n\n`;
    });

    alert(jobDescription);
});

    // Event listener for filtering jobs based on selected job title
    jobTitlesDropdown.addEventListener("change", function() {
        const selectedTitle = this.value;
        const rows = jobTableBody.querySelectorAll("tr");
        rows.forEach(row => {
            const jobTitle = row.querySelector("td:first-child").textContent;
            if (selectedTitle === "" || jobTitle === selectedTitle) {
                row.style.display = "table-row";
            } else {
                row.style.display = "none";
            }
        });
    });
});
