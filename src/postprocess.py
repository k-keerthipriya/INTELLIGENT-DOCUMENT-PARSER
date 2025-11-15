import pandas as pd

def reconstruct_table(words, boxes, labels):
    header = []
    rows = []

    current_row = []

    for word, label in zip(words, labels):
        if "HEADER" in label:
            header.append(word)

        elif "ROW" in label:
            current_row.append(word)

        if label == "O" and current_row:
            rows.append(current_row)
            current_row = []

    df = pd.DataFrame(rows, columns=header if header else None)
    return df
