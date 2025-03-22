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
```plaintext
vector-db-comparison/
├── src/
│   ├── databases/
│   │   ├── weaviate_db/
│   │   ├── qdrant_db/
│   │   └── pgvector_db/
│   ├── benchmarks/
│   ├── data_processing/
│   ├── evaluation/
│   └── utils/
├── config/
│   ├── database_config.yaml
│   └── benchmark_config.yaml
├── tests/
├── scripts/
├── requirements.txt
├── setup.py
├── docker-compose.yml
└── specs.md
```

## Setup

### Prerequisites
- Python 3.8 or higher
- Docker and Docker Compose
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Araste1a/rinbp25-vector-db-comparison.git
cd rinbp25-vector-db-comparison
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start databases:
```bash
docker-compose up -d
```

## Running Tests
```bash
pytest tests/
```

## Database Configurations
- Weaviate: Running on port 8080
- Qdrant: Running on port 6333
- pgvector: Running on port 5432

## Documentation
See `specs.md` for detailed technical specifications and benchmarking methodology.

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
