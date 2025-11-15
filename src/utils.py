from transformers import LayoutLMv3Processor
from PIL import Image

processor = LayoutLMv3Processor.from_pretrained("microsoft/layoutlmv3-base")

def prepare_inputs(words, boxes, image):
    encoded_inputs = processor(
        image,
        words,
        boxes=boxes,
        return_tensors="pt",
        truncation=True,
        padding="max_length",
        max_length=512
    )
    return encoded_inputs
