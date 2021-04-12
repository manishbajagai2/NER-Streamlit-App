import wikipedia
import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')

import streamlit as st
import spacy_streamlit
import datetime

# Sumy Summary Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')


HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

# Function for Sumy Summarization


def sumy_summarizer(docx):
    parser = PlaintextParser.from_string(docx, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, 3)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result


def analyze_text(text):
    return nlp(text)


def main():

    activities = ["Wiki Search Analysis","Analyse Sentence"]
    choice = st.sidebar.selectbox("Select Activity", activities)

    x = datetime.datetime.now()
    st.sidebar.subheader("Dated :")
    st.sidebar.write(" ", x.strftime("%d - %b - %Y"))
    st.sidebar.write(" ", x.strftime("%I : %M %p"))
    st.title("Search by Summary from Wikipedia")
    st.subheader("Please enter a valid keyword. For example - manish")

    st.sidebar.subheader("By")
    st.sidebar.write("Manish Bajagai")

    if choice == 'Wiki Search Analysis':
        
        search1 = st.text_input("Enter Text Here to get the data")

        summarizer = {}
        for items in wikipedia.search("\"" + search1 + "\"", results=5):
            summarizer[items] = wiki_wiki.page(items).summary

        if st.button("1. Search the above "):
            page = wiki_wiki.page("\'"+search1+"\'")
            st.spinner("Showing top five search results if page exist...")
            titles = list(summarizer.keys())
            for i, j in enumerate(titles, start=1):
                st.write(i, "- ", j)

            desc = list(summarizer.values())
            for i in titles:
                for j in desc:
                    st.write(i)
                    st.write(j)
                    break
            if page.exists == False:
                st.warning("Sorry, the page does not exist. Please try again")
        res = ''.join(key +"\n" +str(val) for key, val in summarizer.items())
        if st.button("2. Show Annoted Text"):
            docx = analyze_text(res)
            spacy_streamlit.visualize_ner(docx,labels=nlp.get_pipe('ner').labels)
                # html = displacy.render(docx, style="ent")
                # html = html.replace("\n\n", "\n")
                # st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)
        
        if st.button('3. Summarize'):
            summary_result = sumy_summarizer(res)
            st.write(summary_result)

        if st.button("4. Show Tokens and Lemma in JSON"):
            doc = nlp(res)
            allData = [('"Token":{},\n"Lemma":{}'.format(token.text, token.lemma_))for token in doc]
            st.json(allData)
        
    if choice == 'Analyse Sentence':
        sentence = st.text_input("Enter your sentence to analyse diagramatically")
        if st.button("Analyse "):
            doc = nlp(sentence)
            html = displacy.render(doc, style='dep',  options={'distance': 90})
            html = html.replace("\n\n", "\n")
            st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)

    


if __name__ == '__main__':
    main()
