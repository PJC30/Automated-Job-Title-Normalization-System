import pandas as pd
import requests
import json
import os
from multiprocessing import Pool



url = "https://research-gateway.salesintel.io/service/research/normalize"
headers = {
    'Authorization': 'Basic Z3Jha2VjaGFAYXN0ZWdpYy5jb206QWxwaGEzMjEj',
    'Content-Type': 'application/json'
}


def normalize_job_title(title):
    payload = json.dumps({"title": title})
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        try:
            data = response.json()
            return data.get("level", ""), data.get("department", ""), data.get("normalizedTitle", "")
        except json.JSONDecodeError:
            pass
    return None, None, None


def process_chunk(chunk_number, df_chunk):
    normalized_data = df_chunk["title"].apply(normalize_job_title)
    df_chunk[["level", "department", "normalizedTitle"]] = pd.DataFrame(normalized_data.tolist(), index=df_chunk.index)
    output_file = f"output_chunk_{chunk_number}.csv"
    df_chunk.to_csv(output_file, index=False, columns=["title", "level", "department", "normalizedTitle"])
    return output_file


def split_input_file(input_file, chunk_size=int(input('Enter a chunk size:\n'))):
    df = pd.read_csv(input_file)
    num_chunks = (len(df) - 1) // chunk_size + 1
    chunks = [df[i * chunk_size:(i + 1) * chunk_size] for i in range(num_chunks)]
    return chunks


if __name__ == "__main__":
    input_file = "input.csv"
    chunks = split_input_file(input_file)

    with Pool() as pool:
        results = []
        for i, chunk in enumerate(chunks):
            result = pool.apply_async(process_chunk, args=(i, chunk))
            results.append(result)

        pool.close()
        pool.join()

    final_output_df = pd.concat([pd.read_csv(result.get()) for result in results], ignore_index=True)

    final_output_df.to_csv("output.csv", index=False, columns=["title", "level", "department", "normalizedTitle"])

    for result in results:
        output_file = result.get()
        os.remove(output_file)
