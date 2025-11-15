from src.ocr import run_ocr
from src.utils import prepare_inputs
from src.table_extractor import run_model, id2label
from src.postprocess import reconstruct_table

def process_document(image_path: str):
    words, boxes, img = run_ocr(image_path)
    encoded_inputs = prepare_inputs(words, boxes, img)
    predictions = run_model(encoded_inputs)

    labels = [id2label[p] for p in predictions]
    df = reconstruct_table(words, boxes, labels)
    return df
