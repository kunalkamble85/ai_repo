# Load model directly
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline
import torch.nn.functional as F

pipe = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
print(pipe("I hate dogs"))

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
pipe = pipeline("text-classification", model=model, tokenizer= tokenizer)
print(pipe("I hate dogs"))

ids = tokenizer("My lovingly dogs")
print(ids)

tokens = tokenizer.tokenize("My lovingly dogs")
print(tokens)
ids = tokenizer.convert_tokens_to_ids(tokens)
print(ids)
str = tokenizer.decode(ids)
print(str)
print("------------------------------------------------------------------------------------------")
x_train = ["I hate dogs", "My lovingly dogs"]
print(pipe(x_train))

batch = tokenizer(x_train, padding = True, max_length =512, truncation =  True, return_tensors = "pt")
print(batch)

with torch.no_grad():
    output = model(**batch)
    print(output)
    predications = F.softmax(output.logits, dim=1)
    print(predications)
    labels = torch.argmax(predications, dim=1)
    print(labels)


