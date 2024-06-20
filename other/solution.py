student_names = 

for loop for each student:
 
    # Inputs for General understanding
    understanding_level = 1-4
    contribution_level = 1-4
    completion_level = 1-4
 
    # Inputs for Learner punctuality and engagement
    punctuality_level = 1-4
    engagement_level = 1-4
    webcam_usage_level = 1-4
 
    # Input for Recommendations on further learning
    further_learning = 1-4
 
    # map input to descriptions
    understanding_descriptions = {"1": "a basic understanding", "2": "", "3": "", "4": ""}
    contribution_descriptions = {"1": "contributed to group discussions when asked", "2": "", "3": "", "4": ""}
    completion_description = {"1": "completing some of the labs as required", "2": "", "3": "", "4": ""}
    punctuality_description = {"1": "was sometimes punctual", "2": "", "3": "", "4": ""}
    engagement_description = {"1": "engaged to some extent", "2": "", "3": "", "4": ""}
    webcam_usage_description = {"1": "would benefit from having their webcam on in session to promote interaction", "2": "", "3": "", "4": ""}
    further_learning_description = {"1": "basic concepts", "2": "", "3": "", "4": ""}
    learning_concepts = {"1": "iteration/conditionals/collections", "2": "", "3": "", "4": ""}
 
    # template for feedback
    feedback = f"General comments\n{student} demonstrated {understanding_descriptions[understanding_level]} of Python and general programming concepts.\n{student} {contribution_descriptions[contribution_level]},\n{completion_description[completion_level]}.\n\n"
    feedback += f"Learner punctuality and Engagement\n{student} {punctuality_description[punctuality_level]} and {engagement_description[engagement_level]} throughout the module.\n{student} {webcam_usage_description[webcam_usage_level]}.\n\n"
    feedback += f"Recommendations on further learning\nContinue to practice {further_learning_description[further_learning]}, such as {learning_concepts[further_learning]}."
 
    # Write the feedback to a file
   