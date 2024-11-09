# Job Title Normalization Pipeline

## Overview
This project features a **robust job title normalization pipeline** designed to process job titles in a CSV file, send them to an API in JSON format, and return the results in CSV format. The pipeline uses **Python**, **pandas**, **multiprocessing**, and API integration to standardize job titles efficiently, utilizing parallel processing for enhanced performance.

## Features
- **CSV Input**: Job titles are read from a CSV file.
- **API Integration**: Job titles are sent to an external API for normalization. The API expects data in JSON format and returns results in JSON.
- **Multiprocessing**: The pipeline uses parallel processing to optimize performance by processing data in chunks.
- **CSV Output**: The results from the API are converted back into CSV format, including normalized job titles, levels, and departments.

## Workflow
1. **Data Ingestion**: The job titles are loaded from a CSV file.
2. **Normalization**:
   - Each job title is sent to the API as JSON for normalization.
   - The API response, which includes the job title's normalized form, department, and level, is processed.
3. **Parallel Processing**:
   - The data is split into chunks, and each chunk is processed in parallel using Python's multiprocessing library.
4. **Output**: The results, including normalized job titles, levels, and departments, are saved to a CSV file.

## Code Overview
- **normalize_job_title**: This function sends each job title to the API and processes the response.
- **process_chunk**: This function processes each chunk of job titles and writes the results to a CSV file.
- **split_input_file**: This function splits the input CSV file into smaller chunks to enable parallel processing.
- **Multiprocessing**: The `Pool` class is used to process the chunks in parallel, improving efficiency for large datasets.

## Technologies Used
- **Python**: Core scripting language.
- **pandas**: For reading and processing the CSV files.
- **requests**: For sending HTTP requests to the API.
- **Multiprocessing**: For parallel processing of large datasets.
- **API**: For job title normalization.
