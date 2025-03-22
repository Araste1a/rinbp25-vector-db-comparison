# Vector Database Comparison Project

Comparative analysis of vector databases (Weaviate, Qdrant, pgvector) for image search applications.

## Overview
This project evaluates the performance and capabilities of three vector databases:
- Weaviate
- Qdrant
- pgvector

## Key Metrics
- Indexing speed
- Query latency
- Recall accuracy

## Project Structure
`
src/
├── databases/          # Database client implementations
│   ├── weaviate_db/
│   ├── qdrant_db/
│   └── pgvector_db/
├── benchmarks/         # Benchmark implementations
├── data_processing/    # Data processing utilities
├── evaluation/         # Evaluation metrics
└── utils/             # Common utilities

config/                # Configuration files
tests/                 # Test suite
scripts/               # Utility scripts
`

## Setup
1. Install dependencies:
   \\\ash
   pip install -r requirements.txt
   \\\

2. Start databases:
   \\\ash
   docker-compose up -d
   \\\

## Running Tests
\\\ash
pytest tests/
\\\

## Documentation
See \specs.md\ for detailed technical specifications.
