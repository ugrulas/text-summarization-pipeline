# text-summarization-pipeline

## To-Do List

### Repository Setup
- [ ] **Repository Setup:** 
    - [ ] Setup pre-commit hooks
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

- [ ] **Summarization Model:** 
    - [x] Develop an initial text summarization model on wikilingua dataset 
    - [ ] Implement evaluation metrics (BLEU, ROUGE, etc.)

- [ ] **Integration with Vector Store for RAG:** 
    - [ ] Integrate the summarization model with the vector store
    - [ ] Run the model on the pfizer data
    - [ ] Implement map-reduce
    - [ ] Test and validate model performance under different settings

### Deployment Strategies

- [ ] **Deployment Pipeline Development:** Establish robust deployment pipelines for the integrated modules.

- [ ] **Scalability and Maintenance:** Ensure the infrastructure is scalable and maintainable.

### Documentation

- [ ] **Documentation:** Document the code and the deployment pipelines.
