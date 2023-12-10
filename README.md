# text-summarization-pipeline

## To-Do List

### Repository Setup
- [ ] **Repository Setup:** 
    - [ ] Setup pre-commit hooks
    - [ ] Development and Testing Environment Setup
    - [ ] Setup CI/CD pipeline

### Model Development
- [ ] **Web Scraping Module Development:** Create a module for efficient and scalable web scraping.
    - [x] Identify and select scraping libraries and tools
    - [x] Develop scraping scripts for pfizer
    - [ ] Generalize the scripts for other websites
    - [ ] Implement a robust scraping pipeline that handles images, tables, etc.

- [ ] **Vector Store:** 
    - [x] Select an basic embedding model
    - [x] Build the vector store using wikilingua dataset
    - [ ] Select a more advanced embedding model that handles long sequences better
    - [ ] Test and validate model performance (PCA, t-SNE, etc. can be useful for visualization)
    - [ ] Vector Database Implementation (Need for large scale deployment)

- [x] **RAG QA:**
    - [x] Implement RAG QA on the pfizer data
    - [ ] Evaluate the model on Finetuned Llama 2
    - [ ] Instruct Embedding Model to generate embeddings for the documents

- [ ] **Summarization Model:** 
    - [x] Develop an initial text summarization model on wikilingua dataset 
    - [x] Implement evaluation metrics (BLEU, ROUGE, etc.)
    - [ ] Play with temperature, top-k, top-p, repetetion penalty, etc. to improve the model performance
    - [ ] Finetune Llama 2 with LoRA

- [ ] **Integration with Vector Store for RAG:** 
    - [x] Integrate the summarization model with the vector store
    - [ ] Run the model on the pfizer data
    - [ ] Implement map-reduce for efficient processing and summarization of multiple documents
    - [ ] Test and validate model performance under different settings (e.g. zero-shot, few-shot, finetuned, etc.)


### Deployment Strategies
- [ ] **Deployment Pipeline Development:** Establish robust deployment pipelines for the integrated modules.

- [ ] **Scalability and Maintenance:** Ensure the infrastructure is scalable and maintainable.

### Documentation

- [ ] **Documentation:** Document the code and the deployment pipelines.
