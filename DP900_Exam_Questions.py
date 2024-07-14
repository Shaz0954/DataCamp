# This Quiz is something I would like to incorporate as part of the courses as they test the learners in the format of the exams.
# Please give it a go, if you dont know the answer press 'Enter' key to skip.
import random


quiz_questions = [
    {
        "question": "Which Azure service is primarily used for big data processing?",
        "options": ["A) Azure Data Factory", "B) Azure Synapse Analytics", "C) Azure HDInsight", "D) Azure Databricks"],
        "answer": "C"
    },
    {
        "question": "What is the primary purpose of a resource group in Azure?",
        "options": ["A) To manage and organize resources efficiently", "B) To deploy applications", "C) To secure data", "D) To create virtual machines"],
        "answer": "A"
    },
    {
        "question": "Which Azure service is a NoSQL database?",
        "options": ["A) Azure SQL Database", "B) Azure Cosmos DB", "C) Azure Database for MySQL", "D) Azure Synapse Analytics"],
        "answer": "B"
    },
    {
        "question": "What does ACID stand for in database transactions?",
        "options": ["A) Atomicity, Consistency, Isolation, Durability", "B) Availability, Consistency, Isolation, Durability", "C) Atomicity, Concurrency, Isolation, Durability", "D) Atomicity, Consistency, Integration, Durability"],
        "answer": "A"
    },
    {
        "question": "Which of the following is a relational database service in Azure?",
        "options": ["A) Azure Table Storage", "B) Azure Blob Storage", "C) Azure SQL Database", "D) Azure Data Lake Storage"],
        "answer": "C"
    },
    {
        "question": "What is the main benefit of using Azure Data Factory?",
        "options": ["A) To create virtual machines", "B) To process big data workloads", "C) To orchestrate data workflows", "D) To secure data"],
        "answer": "C"
    },
    {
        "question": "Which Azure service is designed for real-time data processing?",
        "options": ["A) Azure Data Lake", "B) Azure Stream Analytics", "C) Azure Synapse Analytics", "D) Azure SQL Database"],
        "answer": "B"
    },
    {
        "question": "Which of the following best describes 'horizontal scalability'?",
        "options": ["A) Adding more resources to an existing server", "B) Adding more servers to distribute the load", "C) Reducing the size of the database", "D) Increasing the size of the database"],
        "answer": "B"
    },
    {
        "question": "Which Azure service is primarily used for data warehousing?",
        "options": ["A) Azure Cosmos DB", "B) Azure SQL Database", "C) Azure Synapse Analytics", "D) Azure Blob Storage"],
        "answer": "C"
    },
    {
        "question": "What is a key feature of non-relational databases?",
        "options": ["A) Structured Schema", "B) ACID Compliance", "C) Flexible Schema", "D) SQL Queries"],
        "answer": "C"
    }
]

# Shuffle the questions to randomize the quiz
random.shuffle(quiz_questions)

# Function to conduct the quiz
def conduct_quiz():
    score = 0
    total_questions = len(quiz_questions)
    
    for i, question in enumerate(quiz_questions, 1):
        print(f"\nQuestion {i}: {question['question']}")
        for option in question["options"]:
            print(option)
        
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}.")
    
    print(f"\nYou scored {score} out of {total_questions}.")

# Run the quiz
if __name__ == "__main__":
    print("Welcome to the Azure DP-900 Quiz!\n")
    conduct_quiz()
    print("Thank you for participating in the DataCamp DP900 Exam style quiz! ")
