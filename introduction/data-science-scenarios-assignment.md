# Assignment: Data Science Scenarios

In this first assignment, we ask you to think about some real-life process or problem in different problem domains, and how you can improve it using the Data Science process. Think about the following:

1. Which data can you collect?
1. How would you collect it?
1. How would you store the data? How large the data is likely to be?
1. Which insights you might be able to get from this data? Which decisions we would be able to take based on the data?

Try to think about 3 different problems/processes and describe each of the points above for each problem domain.

Here are some of the problem domains and problems that can get you started thinking:

1. How can you use data to improve education process for children in schools?
1. How can you use data to control vaccination during the pandemic?
1. How can you use data to make sure you are being productive at work?
## Instructions

Fill in the following table (substitute suggested problem domains for your own ones if needed):

| Problem Domain | Problem | Which data to collect | How to store the data | Which insights/decisions we can make | 
|----------------|---------|-----------------------|-----------------------|--------------------------------------|
| Education| In University, we typically have low attendance to lectures and we have the hypothesis that students who attend lectures on average do better during the exam. We want to stimulate attendance and test the hypothesis.|We can track attendance through pictures taken by the security camera or by tracking bluetooth/wifi addresses of student mobile phones in class. Exam data is already available in the university database.|In case we track security camera images - we need to store a few (5-10) photographs during the class(unstructured data) and then use AI to identify faces of students ( Convert data to structured form).| We can compute average attendance data of each student, and see if there is any correlation with exam grades. In order to stimulate student attendance, we can publish the weekly attendance rating on school portal and draw prices among those with highest attendance. |
| Vaccination | In a district, many people don't get the vaccination. We have a hypothesis that if we spread awareness regarding the importance of vaccination, people will take vaccination seriously. We want to stimulate vaccination count and test the hypothesis. | Data of population per district is available in health departments database along with who has taken the vaccinations (structured data) | Categorize people based on sex and age groups  | check how many people have taken vaccination, from the ones who have not taken check there age, sex and plan for the advertisements accordingly in schools, offices, public places, rally in the areas if those are house wifes to make awareness per ward. To Stimulate the vaccination, publish the reports advertisements of all the wards who have completed full or mostly vaccinations and give them award or banner posting. |
| Productivity | In office, it often takes more time than estimated to deliver features. We have a hypotheis that this is caused because of the low productivity of the employees becuase their time is getting consumed on other activities as well. We want to stimulate the employees productivity and prove our hypothesis.  | We can get the employees data/task related data from the orgnisations database. (structured/unstructured) | With the data we have, extract the time employees spend on in meetings, outings, interview, meeting guests, document preparations and log that time vs check time employee actually have to work on the feature. Also, find the data related to feature such as number of bugs, criticality of bugs, amount of rework | If more time is getting spent in outside feature implementation then suggest the time management courses to the employee. Also from task point of view, number of bugs are more and we trace the amount of rework then there is lack of clarity on the task. This can be tackled with better execution plan with more clarity on the requirements. |

## Rubric

Exemplary | Adequate | Needs Improvement
--- | --- | -- |
One was able to identify reasonable data sources, ways of storing data and possible decisions/insights for all problem domains | Some of the aspects of the solution are not detailed, data storage is not discussed, at least 2 problem domains are described | Only parts of the data solution are described, only one problem domain is considered.
