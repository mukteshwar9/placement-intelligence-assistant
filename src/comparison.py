class CompanyComparator:

    @staticmethod
    def create_prompt(question, docs):

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
You are an AI Placement Assistant.

Compare the companies using ONLY the provided context.

Present the answer as a Markdown table with these columns:

| Feature | Company 1 | Company 2 |

Include:
- Eligibility
- CGPA
- Backlogs
- Package
- Bond
- Selection Process
- Skills Required

Context:
{context}

Question:
{question}
"""

        return prompt