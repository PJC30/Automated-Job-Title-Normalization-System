# Job Title Normalization Pipeline

## Overview
This project features a **robust job title normalization pipeline** designed to process job titles in a CSV file, send them to an API in JSON format, and return the results in CSV format. The pipeline uses **Python**, **pandas**, **multiprocessing**, and API integration to standardize job titles efficiently, utilizing parallel processing for enhanced performance. The final result is a single consolidated CSV file containing the normalized job titles, along with their levels and departments, with all temporary chunk files cleaned up after processing.

## Features
- **CSV Input**: Job titles are read from a CSV file.
- **API Integration**: Job titles are sent to an external API for normalization. The API expects data in JSON format and returns results in JSON.
- **Multiprocessing**: The pipeline uses parallel processing to optimize performance by processing data in chunks.
- **Chunk-based Processing**: The input file is split into smaller chunks to allow for efficient parallel processing.
- **CSV Output**: The results from the API are converted back into CSV format, including normalized job titles, levels, and departments.
- **Clean-Up**: After the final output is generated, all temporary chunk files are deleted, leaving only the final CSV file.

## Workflow
1. **Data Ingestion**: Job titles are loaded from a CSV file.
2. **Normalization**:
   - Each job title is sent to the API as JSON for normalization.
   - The API response, which includes the normalized job title, department, and level, is processed.
3. **Parallel Processing**:
   - The data is split into chunks, and each chunk is processed in parallel using Python's multiprocessing library.
4. **Chunk Handling**:
   - Each processed chunk is saved as a separate CSV file.
   - After processing, all chunk files are combined into a single final output CSV file.
5. **Output**: The final result is a single **output.csv** file containing the normalized job titles, levels, and departments.
6. **Clean-Up**: All temporary chunk files are deleted after the final output is created.

## Code Overview
- **normalize_job_title**: Sends each job title to the API and processes the response to extract the normalized data.
- **process_chunk**: Processes each chunk of job titles, adds the normalized data, and writes it to a temporary CSV file.
- **split_input_file**: Splits the input CSV file into smaller chunks to enable parallel processing.
- **Combining Chunks**: The final output is created by concatenating all chunk files into a single CSV file.
- **Multiprocessing**: The `Pool` class is used to process the chunks in parallel, optimizing performance for large datasets.
- **Clean-Up**: After the final output file is created, all temporary chunk files are deleted.

## Technologies Used
- **Python**: Core scripting language.
- **pandas**: For reading and processing CSV files.
- **requests**: For sending HTTP requests to the API.
- **Multiprocessing**: For parallel processing of large datasets.
- **API**: For job title normalization.
