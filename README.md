# Vector Database Comparison

## Project Overview

This project provides a comprehensive comparison of three popular vector databases (Chroma, pgvector, and Milvus) for vector similarity search applications. Chroma is tested using Google Colab notebooks, while pgvector and Milvus are tested using Python scripts with cloud/hosted instances. Vector databases are increasingly important for powering similarity search and recommendation systems in AI applications.

## Project Objectives

- Evaluate and compare the performance characteristics of Chroma, pgvector, and Milvus for vector similarity search
- Measure and analyze key performance metrics including indexing speed, query latency, and recall accuracy
- Provide insights into the strengths and weaknesses of each database for different use cases

## Databases Being Compared

### Chroma
- Open-source embedding database
- Designed for use with LLMs and embedding models
- Provides simple Python-native interface
- Supports multiple storage backends and distance metrics
- Optimized for AI/ML workflows

### pgvector
- PostgreSQL extension for vector similarity search
- Integrates directly with traditional relational database capabilities
- Supports multiple indexing methods including IVFFlat
- Leverages SQL for complex queries with vector similarity

### Milvus
- Distributed vector database built for scalability
- Supports multiple index types (HNSW, IVF_FLAT, etc.)
- Provides rich filtering capabilities
- Features cloud-native architecture
- Optimized for high-performance similarity search

## Project Structure

The project is organized into separate testing implementations:

### Chroma Testing (Google Colab)
```plaintext
notebooks/
├── chroma/
│   ├── chroma_setup.ipynb          # Environment setup and configuration
│   ├── chroma_benchmarks.ipynb     # Performance and accuracy testing
│   └── chroma_analysis.ipynb       # Results analysis and visualization
```

### pgvector Testing (Scripts)
```plaintext
pgvector/
├── connection/
│   └── db_setup.py                 # Database connection and setup
└── benchmarks/
    ├── index_performance.py        # Indexing benchmarks
    ├── query_performance.py        # Query performance tests
    └── accuracy_tests.py           # Accuracy evaluation
```

### Milvus Testing (Scripts)
```plaintext
milvus/
├── connection/
│   └── cluster_setup.py            # Cluster connection and setup
└── benchmarks/
    ├── index_performance.py        # Indexing benchmarks
    ├── query_performance.py        # Query performance tests
    └── accuracy_tests.py           # Accuracy evaluation
```

## Prerequisites

For Chroma testing:
- Google Colab access
- Google Drive account (optional, for saving results)

For pgvector testing:
- Python 3.8+
- Access to one of:
  - ElephantSQL account (free tier)
  - Supabase account (free tier)
  - Neon.tech account (free tier)

For Milvus testing:
- Python 3.8+
- Access to one of:
  - Zilliz Cloud account (free tier with $10 credit)
  - Local Python environment for Milvus Lite

General requirements:
- Basic understanding of vector databases
- Python scripting knowledge

## Database Setup Notes

### Chroma Setup
- Runs directly in Colab environment
- No additional setup required
- Installation handled via pip install commands in notebooks

### pgvector Setup
- Options provided for:
  - Managed PostgreSQL service with pgvector extension
  - Self-hosted PostgreSQL instance
  - Connection details configured in scripts

### Milvus Setup
- Options provided for:
  - Zilliz Cloud (managed Milvus service)
  - Self-hosted Milvus instance
  - Connection details configured in scripts

## Database Testing Environments

This section provides detailed instructions for setting up testing environments for pgvector and Milvus. We focus on free-tier and easy-to-use options that work well with our testing scripts.

### pgvector Testing Options

#### Option 1: ElephantSQL (Recommended for Quick Testing)
1. Sign up at [ElephantSQL](https://www.elephantsql.com/)
2. Create a new instance (Free "Turtle" plan):
   - Choose any name for your instance
   - Select the "Tiny Turtle (Free)" plan
   - Choose a data center near you
3. Enable pgvector:
   ```sql
   CREATE EXTENSION vector;
   ```
4. Connection string format:
   ```python
   DATABASE_URL = "postgresql://user:password@yourserver.elephantsql.com/dbname"
   ```

#### Option 2: Supabase (Free Tier with Vector Support)
1. Create account at [Supabase](https://supabase.com/)
2. Start a new project:
   - Choose organization
   - Select region
   - Use free tier
3. Enable pgvector extension:
   - Go to SQL Editor
   - Run: `CREATE EXTENSION vector;`
4. Connection details:
   ```python
   DATABASE_URL = "postgresql://postgres:[YOUR-PASSWORD]@db.[YOUR-PROJECT-REF].supabase.co:5432/postgres"
   ```

#### Option 3: Neon.tech (Free Tier)
1. Sign up at [Neon](https://neon.tech/)
2. Create a new project:
   - Vector similarity is enabled by default
   - Choose the free compute size
3. Connection string:
   ```python
   DATABASE_URL = "postgresql://[YOUR-USER]:[YOUR-PASSWORD]@[YOUR-ENDPOINT]/[YOUR-DATABASE]"
   ```

### Milvus Testing Options

#### Option 1: Zilliz Cloud (Free Tier with $10 Credit)
1. Sign up at [Zilliz Cloud](https://cloud.zilliz.com/)
2. Create a cluster:
   - Choose the free tier
   - Select region
   - Note: Includes $10 monthly credit
3. Connection setup in Python:
   ```python
   from pymilvus import connections
   
   connections.connect(
       alias="default",
       uri="https://[YOUR-CLUSTER].zillizcloud.com",
       token="[YOUR-API-KEY]"
   )
   ```

#### Option 2: Milvus Lite (In-Memory Testing)
Milvus Lite runs directly in Python, perfect for quick testing:

1. Installation:
   ```python
   !pip install milvus
   ```

2. Usage example:
   ```python
   from pymilvus import connections, MilvusLite
   
   # Initialize Milvus Lite
   lite = MilvusLite()
   
   # Connect to the instance
   connections.connect(alias="default", lite=lite)
   ```

### Configuration Examples

The following examples show how to configure each database connection:

#### Chroma Configuration
[For Colab notebook]
```python
from chromadb import Client

client = Client()
```

#### pgvector Configuration
[In scripts]
```python
import os
from urllib.parse import urlparse

# Set your database URL (use environment variables)
os.environ['DATABASE_URL'] = "postgresql://user:password@host:port/dbname"

# Parse connection details
db_url = urlparse(os.getenv('DATABASE_URL'))
DB_CONFIG = {
    'host': db_url.hostname,
    'port': db_url.port,
    'database': db_url.path[1:],
    'user': db_url.username,
    'password': db_url.password
}
```

#### Milvus Configuration
[In scripts]
```python
import os

# For Zilliz Cloud
MILVUS_URI = "https://[YOUR-CLUSTER].zillizcloud.com"
MILVUS_TOKEN = "[YOUR-API-KEY]"

# For Milvus Lite
MILVUS_LITE = True  # Set to False for Zilliz Cloud

def setup_milvus():
    if MILVUS_LITE:
        lite = MilvusLite()
        connections.connect(alias="default", lite=lite)
    else:
        connections.connect(
            alias="default",
            uri=MILVUS_URI,
            token=MILVUS_TOKEN
        )
```

### Testing Your Setup

Use these functions to verify your database connections:

1. For pgvector:
   ```python
   import psycopg2
   
   def test_pgvector_connection():
       try:
           conn = psycopg2.connect(**DB_CONFIG)
           cur = conn.cursor()
           cur.execute('SELECT version();')
           print("Connection successful!")
           conn.close()
       except Exception as e:
           print(f"Connection failed: {e}")
   ```

2. For Milvus:
   ```python
   from pymilvus import utility
   
   def test_milvus_connection():
       try:
           print(f"Milvus version: {utility.get_server_version()}")
           print("Connection successful!")
       except Exception as e:
           print(f"Connection failed: {e}")
   ```

For more information, refer to:
- pgvector documentation: [GitHub - pgvector](https://github.com/pgvector/pgvector)
- Milvus documentation: [Milvus Docs](https://milvus.io/docs)

## Testing Methodology

Testing is implemented in two ways:

### Chroma (Colab Notebooks)
- Interactive testing environment in Google Colab
- Real-time visualization and analysis
- Easy setup and execution
- Built-in resource monitoring

### pgvector and Milvus (Python Scripts)
- Automated testing scripts
- Cloud/hosted database instances
- Consistent test execution
- Reproducible results

All implementations follow these testing steps:

1. **Data Preparation**
   - Generate or load vector datasets
   - Configure test parameters
   - Set up database connections

2. **Performance Testing**
   - Indexing performance
   - Query latency
   - Throughput under load
   - Resource utilization

3. **Accuracy Testing**
   - Precision and recall metrics
   - Result quality analysis
   - Consistency checks

4. **Results Collection**
   - Automated metrics collection
   - Performance statistics
   - Visualization generation

## Results
Results are automatically generated from both Colab notebooks (Chroma) and Python scripts (pgvector, Milvus) and include:

### Indexing Performance
- Build time for different index types
- Memory usage during indexing
- Disk space utilization

### Query Performance
- Latency measurements for different query types
- Throughput under various loads
- Performance scaling with data size

### Recall Accuracy
- Precision and recall metrics
- Trade-offs between speed and accuracy
- Comparative analysis across databases

## Contributing

Feel free to contribute by:
1. Opening issues for bugs or suggestions
2. Submitting pull requests with improvements:
   - Chroma: Enhance Colab notebooks
   - pgvector/Milvus: Improve Python scripts
3. Adding new test scenarios:
   - Additional vector dimensions
   - Different data distributions
   - New performance metrics
4. Sharing your test results from different environments:
   - Various cloud providers
   - Different hardware configurations
   - Alternative database versions

See `specs.md` for detailed technical specifications and benchmarking methodology.
