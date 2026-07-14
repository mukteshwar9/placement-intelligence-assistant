from src.embeddings import EmbeddingModel

embedding = EmbeddingModel()

model = embedding.get_model()

vector = model.encode("I love Artificial Intelligence")

print(type(vector))

print(len(vector))

print(vector[:10])