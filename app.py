import streamlit as st
from youtube_processor import YouTubeProcessor
from ai_analyzer import AIAnalyzer


def main():
    st.title("AI Video Analysis Agent")
    st.write("Enter a YouTube URL to analyze the video content")

    yt_processor = YouTubeProcessor()
    ai_analyzer = AIAnalyzer()

    url = st.text_input("YouTube URL:")

    if url:
        with st.spinner("Processing video..."):
            try:
                
                transcript = yt_processor.process_video(url)
                st.success("Video processed successfully!")

               
                with st.expander("View Transcript"):
                    st.write(transcript)

               
                analysis_type = st.selectbox(
                    "Select Analysis Type",
                    [
                        "Summary",
                        "Sentiment Analysis",
                        "Question Answering",
                        "Keywords",
                        "Task Automation",
                    ],
                )

                if analysis_type == "Summary":
                    if st.button("Generate Summary"):
                        with st.spinner("Generating summary..."):
                            summary = ai_analyzer.generate_summary(transcript)
                            st.write(summary)

                elif analysis_type == "Sentiment Analysis":
                    if st.button("Analyze Sentiment"):
                        with st.spinner("Analyzing sentiment..."):
                            sentiment = ai_analyzer.analyze_sentiment(transcript)
                            st.write(sentiment)

                elif analysis_type == "Question Answering":
                    question = st.text_input("Enter your question about the video:")
                    if question and st.button("Get Answer"):
                        with st.spinner("Finding answer..."):
                            answer = ai_analyzer.answer_question(transcript, question)
                            st.write(answer)

                elif analysis_type == "Keywords":
                    if st.button("Extract Keywords"):
                        with st.spinner("Extracting keywords..."):
                            keywords = ai_analyzer.extract_keywords(transcript)
                            st.write(keywords)

                elif analysis_type == "Task Automation":
                    if st.button("Extract Tasks"):
                        with st.spinner("Identifying tasks..."):
                            tasks = ai_analyzer.process_command(transcript)
                            st.write(tasks)

            except Exception as e:
                st.error(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
