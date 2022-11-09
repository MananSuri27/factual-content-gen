# factual-content-gen

## Hypothesis

- External knowledge is essential to ensure factuallity + veracity of content.
- Since writing points form the basis for the final blog, accuracy in writing points can boost accuracy of the final blog.

## System Design

### Current Model (Scalenut Cruise Mode)
![current](https://cdn.discordapp.com/attachments/891317274936483871/1039789173395169402/2.png)

### Web engine based Model
![new](https://cdn.discordapp.com/attachments/891317274936483871/1039789173722329119/3.png)


## Example Comparison


Keywords: elon musk twitter takeover
H2: Financials of the Deal

### Current Model (Scalenut Cruise Mode)

Writing Points:
- Twitter announced on Monday that it had made a deal with Tesla, but the details of the agreement are still murky. 
- Some people think the deal was to get more followers for Tesla, while others speculate that Musk wanted more control over his messaging.
- We don't know the full extent of what happened between Tesla and Twitter, but we'll be watching to see how it all plays out. 
- In the meantime, this is an interesting financial move by Elon Musk that deserves closer attention!


### Web engine based Model

Writing Points:
- "The closing of the deal, which followed months of drama and legal challenges as Mr",
- "Meanwhile, the company had less than $1 billion in cash flow",
- "Musk began working to line up financing for the deal and sold 9.6 million of his Tesla shares to free up about $8.4 billion.",
- "NYT reports that he saddled the company with over $13 billion in debt to acquire it, meaning it has to pay $1 billion annually in interest alone",
- "Basically, it generated less money last year than what it now owes lenders annually."

## Implementation Details
Search Engine: Google
Sentence Transformer:
sentence-transformers/multi-qa-MiniLM-L6-cos-v1

This is a sentence-transformers model: It maps sentences & paragraphs to a 384 dimensional dense vector space and was designed for semantic search. It has been trained on 215M (question, answer) pairs from diverse sources. 

## Run the repository
Set-up:
```
git clone https://github.com/MananSuri27/factual-content-gen/
conda create --name fact
conda activate fact
pip install -r requirements.txt
```
Run:
cd to the directory
change parameters in main.py, then:
```
conda activate fact
python3 main.py
```



