# Architecture

## Application Components

### GPT Orchestrator
[Azure Function](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview)

The main orchestrator function app that handles the processing of requests, retrieval of data, and orchestration of prompt workflows.  

### ChatGPT-X
[Azure Web App](https://learn.microsoft.com/en-us/azure/app-service/overview)

Web application deployed for user interaction (including Teams integration).  

### Azure OpenAI Service
Deploy and manage OpenAI models such as GPT-3.5/4/4o for handling advanced natural language processing tasks such as content generation, summarization, extraction, and automation, all within the secure and scalable Azure cloud environment.

### Azure Cosmos DB
Stores and manages structured data, including Plans, prompts, user interactions, and external system data.

## Sequence Diagram
``` mermaid
sequenceDiagram
    participant User
    participant AppService as ChatGPT-X
    participant GPTOrchestrator as GPT Orchestrator
    participant SemanticKernel as Semantic Kernel
    participant OpenAI as Azure OpenAI
    participant CosmosDB as Azure Cosmos DB
    participant ExternalService as External Systems
    User->>AppService: Submits Query/Request
    AppService->>GPTOrchestrator: Sends query details and Plan
    GPTOrchestrator->>SemanticKernel: Orchestrates Plan execution
    SemanticKernel->>CosmosDB: Retrieve necessary data (e.g., history, user inputs)
    SemanticKernel->>ExternalService: Retrieve external data (FHIR, Epic, Availity)
    ExternalService->>SemanticKernel: Returns external data (if applicable)
    SemanticKernel->>OpenAI: Execute prompts in Azure OpenAI
    OpenAI->>SemanticKernel: Return LLM response
    SemanticKernel->>GPTOrchestrator: Aggregate and process responses
    GPTOrchestrator->>AppService: Return processed data to GPT-X
    AppService->>User: Display results to the user
```

## Azure Services

- **[Azure Subscription](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/create-subscription)**  
  **Purpose:** The environment where all resources will be created and managed.  

- **[Azure Resource Group](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal)**  
  **Purpose:** Logical grouping of all Azure resources for easier management.  

- **[Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview)**  
  **Purpose:** To store secrets such as connection strings, account keys, and credentials securely.  

- **[Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction)**  
  **Purpose:** NoSQL and vector database to store large-scale, distributed data.  

- **[Azure Storage Account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview)**  
  **Purpose:** To store binary large objects (e.g., files, logs) used in the application.  

- **[Azure Function App](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview)**  
  **Purpose:** Serverless compute service to run functions in the cloud.  

- **[Azure Web App](https://learn.microsoft.com/en-us/azure/app-service/overview)**  
  **Purpose:** Host web applications or APIs for the GPT-X service.  

- **[Azure App Service Plan](https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans)**  
  **Purpose:** Defines the underlying resources that the web apps and function apps will use.  

- **[Azure Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)**  
  **Purpose:** To monitor and provide insights into the performance and usage of the application.  

- **[Azure Document Intelligence (Form Recognizer Cognitive Service)](https://learn.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/)**  
  **Purpose:** To extract structured data from documents, such as OCR (Optical Character Recognition) processing. 

- **[Azure Speech Service](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/overview)**  
  **Purpose:** Provides speech recognition, text-to-speech, and speech translation capabilities.  

- **[Azure OpenAI Services](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/overview)**  
  **Purpose:** Deploy and manage OpenAI models such as GPT-4o/4o-mini for handling advanced natural language processing tasks such as content generation, summarization, extraction, and automation, all within the secure and scalable Azure cloud environment.

- **[Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search)**  
  **Purpose:** Store and query vectorized data from the GPT-X application. 

## Service Accounts and Keys

**Key Vault Secrets created during installation**:

- `ToFInstallationId`: Installation ID (12-digit random number).
- `ToFInstallationGuid`: Installation GUID.
- `ToFSubscriptionId`: Azure Subscription ID.
- `ToFResourceGroup`: Resource group name.
- `CosmosDBKey`: Key for accessing the Cosmos DB account.
- `StorageAccountConnection`: Connection string for the Azure Storage account.
- `OCR4ImagesKey`, `Speech Service Key`, `OpenAI Service Keys`, etc., for accessing respective services.
