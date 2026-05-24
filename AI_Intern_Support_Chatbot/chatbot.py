import json
from sentence_transformers import SentenceTransformer, util

# Load AI model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load FAQ data
with open('faq_data.json', 'r') as file:
    faq_data = json.load(file)

questions = [item['question'] for item in faq_data]
answers = [item['answer'] for item in faq_data]

# Encode questions
question_embeddings = model.encode(questions, convert_to_tensor=True)

def get_response(user_query):

    query_embedding = model.encode(user_query, convert_to_tensor=True)

    similarity_scores = util.pytorch_cos_sim(
        query_embedding,
        question_embeddings
    )

    best_match = similarity_scores.argmax().item()

    confidence = similarity_scores[0][best_match]

    if confidence < 0.40:
        return "Sorry, I could not understand your query."

    return answers[best_match]