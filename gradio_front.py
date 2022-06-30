# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import gradio as gr
from fastai.text.all import *
from nltk import tokenize

# %%
import nltk
nltk.download('punkt')

# %%
model_pkl = "https://cloudstor.aarnet.edu.au/plus/s/rJzjZMk7ieZGsao/download"
p = Path("./formality.pkl")

# %%
if not p.exists():
    import urllib.request
    urllib.request.urlretrieve(model_pkl, "./formality.pkl")

# %%
m = load_pickle("./formality.pkl")

# %%
formal_sentences = "The Gram matrix (or Gramian matrix, Gramian) of a set of vectors in an inner product space is the Hermitian matrix of inner products. C'man, man, don't leave holding the bag!"

# %%
L(tokenize.sent_tokenize(formal_sentences)).map(lambda x: m.predict(x)[0])

# %%
m = load_learner("./data/learner.pkl")


# %% tags=[]
def formal_informal(text):
    # a = m.predict(text)
    # assessment = "style: {0}, confidence {1:.2f}%".format( a[0], a[2][0] * 100)
    sentences = L(tokenize.sent_tokenize(text))
    predictions = sentences.map(lambda x: m.predict(x)[0])
    # assessment = "style: {0}".format(a[0])
    assessment = zip(sentences.map(lambda x: x + ' '), predictions)
    return assessment
    
demo = gr.Interface(formal_informal, 
                    gr.Textbox(label="Your text", lines=5, value=""), 
                    gr.HighlightedText(label="Stylistic analysis", color_map={'formal': 'blue', 'informal': 'yellow'},
                                       combine_adjacent=True, show_legend=False), 
                    examples=["I returned and saw under the sun, that the race is not to the swift, nor the battle to the strong, neither yet bread to the wise, nor yet riches to men of understanding, nor yet favour to men of skill; but time and chance happeneth to them all.",
                              "Objective consideration of contemporary phenomena compels the conclusion that success or failure in competitive activities exhibits no tendency to be commensurate with innate capacity, but that a considerable element of the unpredictable must invariably be taken into account."])
demo.launch()

# %%
