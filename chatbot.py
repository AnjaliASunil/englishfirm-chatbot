import re

# Dictionary of responses with patterns for better matching
responses = {
    r"locations?": "We have locations in Parramatta, Sydney, Melbourne, and Kochi, Kerala.",
    r"contact.*details": "You can reach us in Sydney at +61432269874 and in Kerala at +917356326173.",
    r"services?": "We offer PTE Coaching, IELTS Coaching, NAATI Coaching, General English Courses, and Migration Services.",
    r"core.*value": "Our core value is to provide customized guidance, low-cost training, one-on-one sessions, both classroom and online options, free evaluation and feedback, and flexible timing.",
    r"training.*details": "We offer a free demo, practice materials, expert evaluation, unlimited feedback, and flexible timing.",
    r"PTE.*coaching": "PTE coaching includes one-on-one training, free demo, 2 to 4 weeks of class preparation materials, unlimited feedback, and flexible timing.",
    r"IELTS.*coaching": "IELTS coaching includes one-on-one training, free demo, 2 to 4 weeks of class preparation materials, unlimited feedback, and flexible timing.",
    r"NAATI.*coaching": "NAATI coaching is available in Hindi and Punjabi, includes a free demo, 4 weeks of class preparation materials, unlimited feedback, and is available on weekends.",
    r"General.*English.*course": "The General English course includes one-on-one training, a free demo, 4 to 8 weeks of course preparation materials, unlimited feedback, and flexible timing.",
    r"migration.*services?": "We offer free migration consultation for Englishfirm students and a 50% discount for the PTE+NAATI+MIGRATION combo.",
    r"about.*englishfirm": "Englishfirm provides expert coaching for PTE, IELTS, NAATI, and General English courses, and also offers migration services. We have locations in Sydney, Melbourne, and Kochi, Kerala."
}

# Function to get a response based on user input
def get_response(user_input):
    # Normalize the input to lowercase and remove extra spaces
    user_input = user_input.strip().lower()
    
    # Check each pattern for a match
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response
    
    # Default response if no match found
    return "I'm sorry, I don't understand your question. Can you please ask something else?"

# Interactive chat
print("Hello! How can I assist you today? (Type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Goodbye!")
        break
    response = get_response(user_input)
    print(f"Bot: {response}")
