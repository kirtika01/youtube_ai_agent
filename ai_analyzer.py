import google.generativeai as genai
from config import GOOGLE_API_KEY


class AIAnalyzer:
    def __init__(self):
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel("gemini-2.0-flash-001")

    def _safe_generate(self, prompt):
        """Safely generate content with error handling"""
        try:
            response = self.model.generate_content(prompt)
            return response.text if response.text else "No response generated"
        except Exception as e:
            return f"Error processing request: {str(e)}"

    def generate_summary(self, transcript):
        prompt = """
        Please provide a concise and clear summary of the following transcript, highlighting the main points 
        and key takeaways in a structured format:

        Transcript:
        {text}
        """.format(
            text=transcript
        )

        return self._safe_generate(prompt)

    def analyze_sentiment(self, transcript):
        prompt = """
        Analyze the sentiment of this transcript. Consider:
        1. Overall tone (positive, negative, neutral)
        2. Key emotional points
        3. Notable shifts in tone
        4. Main emotional themes

        Transcript:
        {text}
        """.format(
            text=transcript
        )

        return self._safe_generate(prompt)

    def answer_question(self, transcript, question):
        prompt = """
        Using only the information from the following transcript, answer this question:
        Question: {q}

        Base your answer strictly on the transcript content:
        {text}
        """.format(
            q=question, text=transcript
        )

        return self._safe_generate(prompt)

    def extract_keywords(self, transcript):
        prompt = """
        Extract the most important keywords and topics from this transcript.
        Format them in a clear, organized list with brief explanations of their significance.

        Transcript:
        {text}
        """.format(
            text=transcript
        )

        return self._safe_generate(prompt)

    def process_command(self, transcript):
        prompt = """
        Identify actionable tasks, steps, or instructions from this transcript.
        Format them as a clear, organized to-do list.

        Transcript:
        {text}
        """.format(
            text=transcript
        )

        return self._safe_generate(prompt)
