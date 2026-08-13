
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pypdf import PdfReader
import io

app = FastAPI(title="AskMyNotes API")


# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Home route
@app.get("/")
def home():
    return {
        "message": "AskMyNotes Backend is running!"
    }


# Ask question from uploaded PDF
@app.post("/ask")
async def ask_question(
    file: UploadFile = File(...),
    question: str = Form(...)
):

    # Check PDF
    if not file.filename.lower().endswith(".pdf"):
        return {
            "error": "Please upload a PDF file."
        }

    try:
        # Read uploaded PDF
        contents = await file.read()

        pdf = PdfReader(io.BytesIO(contents))

        # Extract text from PDF
        text = ""

        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        # Check whether text was extracted
        if not text.strip():
            return {
                "answer": "Could not extract text from this PDF."
            }

        # Convert question to lowercase words
        question_words = question.lower().split()

        # Split PDF text into sentences
        sentences = text.replace("\n", " ").split(".")

        relevant_sentences = []

        # Find sentences related to question
        for sentence in sentences:

            sentence_lower = sentence.lower()

            for word in question_words:

                if len(word) > 3 and word in sentence_lower:
                    relevant_sentences.append(sentence.strip())
                    break

        # Return relevant answer
        if relevant_sentences:

            answer = ". ".join(
                relevant_sentences[:5]
            )

            return {
                "question": question,
                "answer": answer
            }

        else:

            return {
                "question": question,
                "answer": "I could not find a relevant answer in the uploaded PDF."
            }

    except Exception as e:

        return {
            "error": str(e)
        }