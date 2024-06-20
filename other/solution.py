import os
import subprocess
 
subfolder = "feedback_files"
 
os.makedirs(subfolder, exist_ok=True)
 
def get_input(prompt):
    return input(prompt)
 
def open_in_editor(filename):
    editor = os.getenv('EDITOR')
    subprocess.run([editor, filename])
 
student_names = get_input("Enter the names of students separated by commas: ").split(",")
print(student_names)
for student in student_names:
    student = student.strip()
    print(f"\nEntering feedback for {student}: ")
 
    # General understanding
    understanding_level = get_input("Enter understanding level (1: basic, 2: good, 3: very good, 4: excellent): ")
    contribution_level = get_input("Enter contribution level (1: minimum, 2: moderate, 3: high, 4: exceptional): ")
    completion_level = get_input("Enter lab completion level (1: partial, 2: most, 3: nearly all, 4: all): ")
 
    # Learner punctuality and engagement
    punctuality_level = get_input("Enter punctuality level (1: sometimes punctual, 2: usually punctual, 3: consistently punctual, 4: always punctual): ")
    engagement_level = get_input("Enter engagement level (1: basic, 2: good, 3: very good, 4: excellent): ")
    webcam_usage_level = get_input("Enter webcam usage (1: seldom on, 2: often on, 3: mostly on, 4: always on): ")
 
    # Recommendations on further learning
    further_learning = get_input("Enter further learning level (1: basic, 2: intermediate, 3: challenging, 4: advanced): ")
 
    # map input to descriptions
    understanding_descriptions = {"1": "a basic understanding", "2": "a good understanding", "3": "a very good understanding", "4": "an excellent understanding"}
    contribution_descriptions = {"1": "contributed to group discussions when asked", "2": "often contributed to group discussions", "3": "frequently contributed to group discussions and helped colleagues", "4": "consistently led group discussions and brought new ideas"}
    completion_description = {"1": "completing some of the labs as required", "2": "completing most of the labs as required", "3": "completing most/all labs to a good standard", "4": "completing all labs to an excellent standard including further stretch goals"}
    punctuality_description = {"1": "was sometimes punctual", "2": "was generally punctual", "3": "was consistently punctual", "4": "was always punctual and ready"}
    engagement_description = {"1": "engaged to some extent", "2": "engaged well", "3": "was very engaged", "4": "was highly engaged and interactive"}
    webcam_usage_description = {"1": "would benefit from having their webcam on in session to promote interaction", "2": "would benefit from having their webcam on in session to promote interaction", "3": "often had their webcam on throughout the module, enhancing interaction", "4": "always had their webcam on during sessions, greatly enhancing interaction"}
    further_learning_description = {"1": "basic concepts", "2": "intermediate concepts", "3": "challenging concepts", "4": "advanced topics"}
    learning_concepts = {"1": "iteration/conditionals/collections", "2": "functions/files/modules/testing", "3": "OOP/Databases", "4": "advanced algorithms/data structures and start to specialise in your own area"}
 
    # template for feedback
    feedback = f"General comments\n{student} demonstrated {understanding_descriptions[understanding_level]} of Python and general programming concepts.\n{student} {contribution_descriptions[contribution_level]},\n{completion_description[completion_level]}.\n\n"
    feedback += f"Learner punctuality and Engagement\n{student} {punctuality_description[punctuality_level]} and {engagement_description[engagement_level]} throughout the module.\n{student} {webcam_usage_description[webcam_usage_level]}.\n\n"
    feedback += f"Recommendations on further learning\nContinue to practice {further_learning_description[further_learning]}, such as {learning_concepts[further_learning]}."
 
    # Write the feedback to a file
    filename = os.path.join(subfolder, f"{student}_feedback.txt")
    with open(filename, "w") as file:
        file.write(feedback)
        print(f"Feedback for {student} written to file {filename}")
 
    # Open the feedback in the default text editor
    print(f"Opening {filename} in the default editor to make any final adjustments...")
    open_in_editor(filename)
 
    print(f"Feedback for {student} has been edited and saved in file {filename}")