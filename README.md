# Vector Database Comparison for Image Search Applications

## Project Overview

This project aims to comprehensively compare three popular vector databases (Weaviate, Qdrant, and pgvector) for image search applications. Vector databases are increasingly important for powering similarity search and recommendation systems in AI applications, particularly for image retrieval tasks. This repository contains the benchmarking framework, evaluation tools, and results of our comparative analysis.

## Project Objectives

- Evaluate and compare the performance characteristics of Weaviate, Qdrant, and pgvector for image search workloads
- Measure and analyze key performance metrics including indexing speed, query latency, and recall accuracy

## Databases Being Compared

### Weaviate
- Open-source vector search engine
- Built with scalability in mind
- Provides semantic search capabilities with various distance metrics
- Supports multiple vectorization modules

### Qdrant
- Vector similarity search engine
- Focuses on extended filtering and high-performance vector search
- Implements HNSW (Hierarchical Navigable Small World) algorithm
- Optimized for production-ready applications

### pgvector
- PostgreSQL extension for vector similarity search
- Integrates directly with traditional relational database capabilities
- Supports multiple indexing methods including IVFFlat
- Leverages SQL for complex queries with vector similarity

## Methodology and Evaluation Criteria

The comparison evaluates each database across several dimensions:

### Performance Metrics
- **Indexing Speed**: Time required to index large collections of image vectors
- **Query Latency**: Response time for different types of similarity searches
- **Recall Accuracy**: Precision of returned results compared to ground truth
- **Throughput**: Number of queries processed per second under load

### Technical Considerations
- Scalability with increasing data volume
- Memory consumption
- CPU utilization
- Storage requirements
- Ease of deployment and management

### Testing Approach
- Standardized image dataset with pre-computed embeddings
- Consistent hardware environment for all tests
- Progressive load testing with varying dataset sizes
- Batch and real-time query scenarios
## Project Structure

The project is structured as follows, with both implemented and planned components:

```plaintext
vector-db-comparison/
├── src/                      # Core implementation (implemented)
│   ├── databases/            # Database client implementations
│   │   ├── weaviate_db/
│   │   ├── qdrant_db/
│   │   └── pgvector_db/
│   ├── benchmarks/           # Benchmark implementations
│   ├── data_processing/      # Data processing utilities
│   ├── evaluation/           # Evaluation metrics
│   └── utils/                # Common utilities
├── config/                   # Configuration files (implemented)
│   ├── database_config.yaml
│   └── benchmark_config.yaml
├── tests/                    # Test suite (implemented)
├── scripts/                  # Utility scripts (implemented)
│
# Planned directory structure additions:
├── data/                     # Test datasets and embeddings
├── docker/                   # Additional Docker configurations
├── results/                  # Benchmark results and analysis
├── notebooks/                # Jupyter notebooks for analysis
├── visualizations/           # Result visualizations and charts
│
# Configuration and documentation:
├── requirements.txt          # Python dependencies (implemented)
├── setup.py                  # Package installation (implemented)
├── docker-compose.yml        # Container setup (implemented)
└── specs.md                  # Technical specifications (implemented)
```
## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Docker and Docker Compose
- Git
- Sufficient storage space for image datasets

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

3. Start databases using our Docker Compose setup:
```bash
docker-compose up -d
```

This will start:
- Weaviate on port 8080
- Qdrant on port 6333
- pgvector (PostgreSQL) on port 5432

Our docker-compose.yml configures:
  - **Weaviate**: With anonymous access enabled and persistent storage
  - **Qdrant**: With volume mapping for data persistence
  - **pgvector**: Using the ankane/pgvector image with preconfigured database settings

### Environment Setup
```bash
# Create and activate a virtual environment (recommended)
python -m venv venv

# On Windows
.\venv\Scripts\activate
# On Unix/MacOS
source venv/bin/activate
```

## Running Tests
```bash
pytest tests/
```

## Results

### Indexing Performance
*This section will contain results comparing the indexing speed across databases with various dataset sizes.*

### Query Performance
*This section will present query latency measurements for different types of searches.*

### Recall Accuracy
*This section will display precision and recall metrics for each database.*

### Resource Utilization
*This section will compare CPU, memory, and storage requirements.*

### Overall Comparison
*This section will provide a comprehensive comparison table and recommendations.*

## Documentation
See `specs.md` for detailed technical specifications and benchmarking methodology.


