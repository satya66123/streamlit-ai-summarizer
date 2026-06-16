import re

import requests
from openai import OpenAI

OLLAMA_URL = "http://localhost:11434/api/generate"


# ======================================
# OLLAMA GENERATION
# ======================================
def ollama_generate(
    prompt,
    model_name,
    num_predict
):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model_name,
            "prompt": prompt,
            "stream": False,
            "keep_alive": "30m",
            "options": {
                "temperature": 0.1,
                "num_predict": num_predict,
                "top_p": 0.9
            }
        },
        timeout=300
    )

    response.raise_for_status()

    return response.json().get(
        "response",
        ""
    ).strip()


# ======================================
# OPENAI GENERATION
# ======================================
def openai_generate(
    prompt,
    api_key,
    model_name="gpt-4o-mini"
):

    client = OpenAI(
        api_key=api_key
    )

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.1
    )

    return response.choices[0].message.content.strip()


# ======================================
# UNIVERSAL GENERATE
# ======================================
def generate(
    prompt,
    provider,
    model_name,
    num_predict,
    api_key=None
):

    if provider == "OpenAI":

        return openai_generate(
            prompt,
            api_key,
            model_name
        )

    return ollama_generate(
        prompt,
        model_name,
        num_predict
    )


# ======================================
# CHUNK TEXT
# ======================================
def chunk_text(
    text,
    chunk_size=500
):

    words = text.split()

    chunks = []

    for i in range(
        0,
        len(words),
        chunk_size
    ):

        chunks.append(
            " ".join(
                words[i:i + chunk_size]
            )
        )

    return chunks


# ======================================
# PROMPT BUILDER
# ======================================
def build_prompt(
    text,
    summary_type
):

    if summary_type == "Short":

        prompt = f"""
        You are an expert text summarizer.

        Summarize the following text.

        Rules:
- Return exactly 1 complete sentence ending with a period.
- Maximum 50 words.
- Include only key information.
- Use only information present in the text.
- Do NOT add or infer facts.
- No bullet points, headings, or introductions.
- Return only the summary sentence.

        Text:
        {text}
        """

        num_predict = 120

    elif summary_type == "Detailed":

        prompt = f"""
        You are an expert text summarizer.

        Create a detailed summary.

        Rules:
- Write 3 to 5 complete sentences.
- Every sentence must end with a period (.).
- Cover all major points from the text.
- Preserve important facts and statistics if present.
- Use only information explicitly stated in the text.
- Do NOT add external knowledge.
- Do NOT infer facts, statistics, dates, names, industries, or trends not mentioned in the text.
- Do not leave incomplete sentences or unfinished thoughts.
- Do not stop mid-paragraph.
- Do not use bullet points, headings, introductions, or conclusions.
- Return only the summary.
- Keep the summary between 80 and 100 words.

        Text:
        {text}
        """

        num_predict = 250

    else:

        prompt = f"""
        You are an expert text summarizer.

        Rules:
- Generate exactly 5 bullet points.
- Put each bullet point on a separate line.
- Start every line with "- ".
- Each bullet point must be a complete sentence.
- Each bullet point must end with a period (.).
- Use only information from the text.
- Do not add external knowledge.
- Do not generate introductions or conclusions.
- Return only the bullet points.

        Text:
        {text}
        """

        num_predict = 180

    return prompt, num_predict


# ======================================
# MAIN SUMMARIZER
# ======================================
def summarize_text(
    text,
    summary_type,
    model_name,
    provider="Ollama",
    api_key=None
):

    # --------------------------------
    # WORD COUNT
    # --------------------------------

    word_count = len(
        text.split()
    )

    # --------------------------------
    # SMALL DOCUMENTS
    # --------------------------------

    if word_count <= 1000:

        prompt, num_predict = build_prompt(
            text,
            summary_type
        )

        summary = generate(
            prompt,
            provider,
            model_name,
            num_predict,
            api_key
        )

        # Remove extra spaces/newlines
        if summary_type != "Bullet Points":
            summary = " ".join(summary.split())
        else:
            summary = "\n".join(
                line.strip()
                for line in summary.splitlines()
                if line.strip()
            )

        # Ensure complete ending
        if (
            summary
            and summary[-1]
            not in ".!?"
        ):
            summary += "."

        summary = clean_output(
            summary,
            summary_type
        )

        return summary

    # --------------------------------
    # LARGE DOCUMENTS
    # --------------------------------

    chunks = chunk_text(
        text,
        chunk_size=500
    )

    chunk_summaries = []

    for chunk in chunks:

        chunk_prompt = f"""
You are an expert text summarizer.

Summarize the text.

Rules:
- Keep only important information.
- Remove repetition.
- Use complete sentences only.
- Every sentence must end with a period.
- Do not leave incomplete thoughts or unfinished sentences.
- Use only information explicitly present in the text.
- Do NOT add external knowledge.
- Do NOT infer facts not explicitly stated.
- Do NOT invent statistics, dates, names, industries, or trends.
- Preserve important facts and statistics if present.
- Return only the summary.

Text:
{chunk}
"""

        summary = generate(
            chunk_prompt,
            provider,
            model_name,
            80,
            api_key
        )

        # Clean chunk summary
        summary = summary.strip()

        if (
            summary
            and summary[-1]
            not in ".!?"
        ):
            summary += "."

        chunk_summaries.append(
            summary
        )

    # --------------------------------
    # COMBINE CHUNKS
    # --------------------------------

    combined_summary = " ".join(
        chunk_summaries
    )

    # --------------------------------
    # FINAL SUMMARY
    # --------------------------------

    final_prompt, num_predict = build_prompt(
        combined_summary,
        summary_type
    )

    final_summary = generate(
        final_prompt,
        provider,
        model_name,
        num_predict,
        api_key
    )

    # --------------------------------
    # CLEAN FINAL OUTPUT
    # --------------------------------

    if summary_type != "Bullet Points":

        final_summary = " ".join(
            final_summary.split()
        )

    else:

        lines = [
            line.strip()
            for line in final_summary.splitlines()
            if line.strip()
        ]

        final_summary = "\n".join(lines)

    # Ensure proper ending
    if (
        final_summary
        and final_summary[-1]
        not in ".!?"
    ):
        final_summary += "."

    final_summary = clean_output(
        final_summary,
        summary_type
    )

    return final_summary

def clean_output(text, summary_type):

    if summary_type == "Short":
        return " ".join(text.split())

    elif summary_type == "Detailed":

        text = " ".join(text.split())

        sentences = re.split(
            r'(?<=[.!?])\s+',
            text
        )

        return "\n\n".join(
            s.strip()
            for s in sentences
            if s.strip()
        )

    else:  # Bullet Points

        lines = []

        for line in text.splitlines():

            line = line.strip()

            if not line:
                continue

            if not line.startswith("-"):
                line = "- " + line.lstrip("•* ")

            if line[-1] not in ".!?":
                line += "."

            lines.append(line)

        return "\n".join(lines)

import json

def ollama_stream(
    prompt,
    model_name
):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model_name,
            "prompt": prompt,
            "stream": True,
            "keep_alive": "30m",
            "options": {
                "temperature": 0.1
            }
        },
        stream=True
    )

    response.raise_for_status()

    for line in response.iter_lines():

        if not line:
            continue

        try:

            data = json.loads(
                line.decode("utf-8")
            )

            yield data.get(
                "response",
                ""
            )

        except Exception:
            continue

def openai_stream(
    prompt,
    api_key,
    model_name
):

    client = OpenAI(
        api_key=api_key
    )

    stream = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.1,
        stream=True
    )

    for chunk in stream:

        if (
            chunk.choices
            and chunk.choices[0].delta.content
        ):

            yield chunk.choices[0].delta.content
def stream_summary(
    text,
    summary_type,
    model_name,
    provider="Ollama",
    api_key=None
):

    prompt, _ = build_prompt(
        text,
        summary_type
    )

    if provider == "OpenAI":

        return openai_stream(
            prompt,
            api_key,
            model_name
        )

    return ollama_stream(
        prompt,
        model_name
    )
