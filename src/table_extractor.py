import torch
from transformers import LayoutLMv3ForTokenClassification

id2label = {
    0: "O",
    1: "B-HEADER",
    2: "I-HEADER",
    3: "B-ROW",
    4: "I-ROW",
    5: "B-COLUMN",
    6: "I-COLUMN"
}

model = LayoutLMv3ForTokenClassification.from_pretrained(
    "microsoft/layoutlmv3-base",
    num_labels=len(id2label)
)

def run_model(encoded_inputs):
    with torch.no_grad():
        outputs = model(**encoded_inputs)
        predictions = outputs.logits.argmax(-1).squeeze().tolist()
    return predictions
