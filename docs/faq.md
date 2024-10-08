# GPT-X FAQ

## General Questions

### 1. What is GPT-X?
GPT-X is a Platform-as-a-Service (PaaS) that automates workflows and enhances business operations using AI-driven processes powered by the Azure OpenAI Service. It leverages Large Language Models (LLMs) built by [OpenAI](https://openai.com/) to execute intelligent workflows that integrate seamlessly with enterprise systems. This allows organizations to design custom workflows that streamline processes, extract insights from data, and significantly improve operational efficiency.

### 2. What are the key benefits of using GPT-X?
- Flexible and customizable workflows
- Microsoft Azure native
- Seamless integration with Microsoft Teams
- End-to-end automation across various enterprise systems
- Scalable architecture to grow with your business

### 3. Who is GPT-X designed for?
GPT-X is designed for mid-market to large enterprises looking to automate workflows, improve operational efficiency, and integrate AI into their business processes. It is particularly well-suited for organizations using the Microsoft Azure ecosystem.

### 4. What is a plan and a message in GPT-X?
A **plan** in GPT-X is a workflow that can be executed by the GPT Orchestrator service in either attended or unattended mode. Each plan can consist of one or more GPT chat prompts. Within each prompt, there is a **message variable** that represents the instructional portion of the prompt. During plan execution, the message variable is dynamically replaced by the actual input provided by the user or client interacting with the GPT Orchestrator.

---

## Platform Features

### 5. How does GPT-X integrate with Microsoft Teams?
GPT-X directly integrates with Microsoft Teams, allowing users to interact with workflows within the Teams interface. You can initiate tasks, retrieve data, and collaborate on business processes in real-time through Teams.

### 6. What kind of enterprise applications can GPT-X integrate with?
GPT-X integrates with a wide variety of enterprise applications, including ERP systems (e.g., SAP, Oracle), CRM platforms (e.g., Salesforce, HubSpot), and Microsoft 365. It connects via secure APIs, VPNs, and other enterprise-grade solutions.

### 7. Can GPT-X handle unattended workflows?
Yes, GPT-X can run both unattended and attended workflows. Unattended workflows automate back-office operations, while attended workflows guide users through tasks in real-time.

### 8. Who can create and manage messages in GPT-X?
Any GPT-X user can create, edit, send, and manage messages within their personal catalog. Users with the **Message Publisher** role can add messages to shared catalogs that belong to a specific plan. All users can access messages in shared catalogs for that plan. However, each plan has its own catalog, meaning messages are only available within the plan they are associated with.

### 9. What happens if I improve or edit a message? How can I ensure others see the updated version?
Users can edit messages within their personal or shared catalogs. If a **Message Publisher** updates a message in a shared catalog, the updated version becomes available to all users within that plan after the catalog is refreshed. Users can also copy a message from the shared catalog, modify it, and save it as a new message in their personal catalog.

### 10. Does GPT-X keep a history of questions or messages?
Yes, every message sent to the GPT Orchestrator and its corresponding response is stored in Azure Cosmos DB indefinitely, or until it is manually deleted by an Azure Cosmos DB administrator.

---

## Installation

### 11. Can I use Terraform to install GPT-X instead of PowerShell and the CLI?

Yes, you can use Terraform to install GPT-X, but the recommended approach is to first use our supported installation method in a **development/test sandbox environment**. This initial installation will create and configure all necessary Azure resources automatically. Here’s how the process works:

1. **Sandbox Installation**: In the development/test sandbox, our installation will set up the required Azure resources and configure them properly. This step ensures that everything works as expected and gives you visibility into what resources are created and which options are applied.

2. **Testing**: After the resources are created, you can test the system to confirm that all components and applications function as intended. This also allows your team to observe and understand the resource configurations.

3. **Terraform Configuration**: Once the sandbox environment is set up and tested, you can replicate the resource setup using Terraform. You can inspect the resources created in the sandbox and use that as a basis for your Terraform configurations when deploying GPT-X to QA or Production environments.

4. **Resource Management**: Our installations also support the option to select **existing Azure resources** during the installation process. This gives you flexibility in managing your resources between environments.

By following this approach, you ensure that all required resources are identified and tested before rolling out GPT-X to critical environments using Terraform.

---

## Security and Compliance

### 12. Does GPT-X have built-in mechanisms to ensure secure and resilient AI system design, development, and operation?
The GPT-X platform leverages the Azure OpenAI Service and a robust suite of Azure resources to ensure a resilient and secure design. Every component within GPT-X, including the OpenAI Service, Cosmos DB, Function App, App Service, and Azure Storage, is built with enterprise-grade features like redundancy, load balancing, dynamic capacity scaling, fault tolerance, and disaster recovery capabilities.

Key elements of the GPT-X infrastructure include:

- **Dynamic Workfload Optimization and Throttling**: GPT-X is engineered to handle fluctuations in workload efficiently. If the platform becomes overloaded or specific Azure resources experience issues, GPT-X automatically optimizes or throttles workloads to maintain performance. In these scenarios, the system is designed to gracefully degrade functionality, ensuring minimal impact on business operations.
- **Load Balancing and High Availability**: GPT-X’s core components are built for maximum reliability. OpenAI Services and Function Apps are dynamically load-balanced to distribute demand evenly across multiple instances. Cosmos DB is designed for high availability with guaranteed performance and multi-region replication to prevent data loss.

This architecture enables GPT-X to maintain functionality during unexpected events, providing a stable and secure AI-driven environment that minimizes disruptions and ensures continuous operation even in challenging conditions.

### 13. Does GPT-X comply with industry regulations?
Yes, GPT-X can be configured to comply with industry standards and regulations, including HIPAA, GDPR, and others, depending on your business requirements and workflow design.

### 14. What if I don't want everyone to see my message, but I want only a specific team to use it?
Currently, this feature is not available in the existing version of GPT-X. However, the next version will introduce **role-based access control** for plans, which will allow you to limit access to specific messages and plans for certain teams or users.

---

## Support and Troubleshooting

### 15. Who do I contact for support?
For technical support, reach out to our support team at [support@example.com](mailto:support@example.com), or visit our support portal at [support.example.com](#).

---

Have more questions? Reach out to our team at [contact@example.com](mailto:contact@example.com).
