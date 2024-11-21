from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from sentence_transformers import SentenceTransformer
import chromadb

API_KEY = "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"

encoder = SentenceTransformer("all-mpnet-base-v2")
client = chromadb.PersistentClient("vectorstore")
collection = client.get_or_create_collection(name="posts")


# posts = ["Pakistan drama industry is seeing a big boom these days."]
# embeddings = encoder.encode(posts)

# collection.add(
#     documents=posts,
#     embeddings=embeddings,
#     metadatas=[{ "id": 2 }],
#     ids=["2"]
# )

user_query = "What's happening in cricket these days?"
user_query_vec = encoder.encode(user_query)


response = collection.query(
    query_embeddings=[user_query_vec],
    n_results=5
)

post_ids = [metadata['id'] for metadata in response["metadatas"][0]]

posts_content =  "\n".join(response['documents'][0])

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0.5,
    api_key=API_KEY
)

prompt = PromptTemplate.from_template(
        """
        ### POSTS:
        {posts}
        
        ### INSTRUCTION:
        Write a summary of the posts based on the prompt of the user. Your summary should be short and concise. Use formal English.
        Extract the main points from the posts and write a summary. If the post is irrelevant to the prompt, ignore it.
        ### PROMPT:
        {prompt}

        Do not provide a preamble.
        """
        )

chain_email = prompt | llm
res = chain_email.invoke({"posts": posts_content, "prompt": user_query})
summary = res.content

prompt_relevant_ids = PromptTemplate.from_template(
    """
    ### POSTS:
    {posts}
    
    ### IDS:
    {ids}
    
    ### INSTRUCTION:
    Based on the prompt of the user, return only the IDs of those posts that are relevant to the prompt.
    ### PROMPT:
    {prompt}

    Do not provide a preamble.
    """
)

chain_relevant_ids = prompt_relevant_ids | llm
res_relevant_ids = chain_relevant_ids.invoke({"posts": posts_content, "ids": post_ids, "prompt": user_query})
ids = eval(res_relevant_ids.content)
print(f'''
    Summary: {summary}
    Relevant IDs: {ids} 
''')