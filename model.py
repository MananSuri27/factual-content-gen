from sentence_transformers import SentenceTransformer, util


def rankDocs(query, docs,n):


    #Load the model
    model = SentenceTransformer('sentence-transformers/multi-qa-MiniLM-L6-cos-v1')

    #Encode query and documents
    query_emb = model.encode(query)
    doc_emb = model.encode(docs)

    #Compute dot score between query and all document embeddings
    scores = util.dot_score(query_emb, doc_emb)[0].cpu().tolist()

    #Combine docs & scores
    doc_score_pairs = list(zip(docs, scores))

    #Sort by decreasing score
    doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)

    #Output passages & scores

    top_n = []

    

    for doc, score in doc_score_pairs:
        if n==0:
            break
        top_n.append(doc)
        n = n-1


    print("Ranked docs for ",query, " with ", len(top_n), " outputs.")
    return top_n

