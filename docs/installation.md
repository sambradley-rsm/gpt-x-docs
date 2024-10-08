# GPT-X Platform Installation Guide

**Version: 0.1**  
_Last Updated: 10/8/2024_

---

## Introduction

### Purpose of the Guide

This installation guide provides step-by-step instructions for installing the GPT-X Platform — a cutting-edge, Azure-based Platform-as-a-Service (PaaS) solution. It is intended for IT administrators and DevOps professionals responsible for deploying enterprise applications.

### Product Overview

GPT-X Platform leverages advanced AI capabilities to deliver transformative solutions for your enterprise. It integrates seamlessly with Azure services, offering scalability, security, and high availability.

### Installation Time Estimate

- **Initial Setup**: Approximately 2-3 hours, depending on system configuration and network conditions.
- **Upgrade/Repair**: Approximately 1-2 hours.

---

## System Requirements

- **PowerShell**: Version 5.1 or higher
- **Azure CLI**: Version 2.30.0 or higher

---

## Pre-Installation Checklist

- [ ] **Permissions**: Verify that you have one of the following roles on the VM/PC on which the installation will be ran:
    - MS Windows Administrator
    - Member of MS Windows Local Administrators

    This is required to install the product binaries to the Program Files(x86) directory

- [ ] **Azure Subscription Access**: Verify that you have one of the following role sets in the target Azure subscription:
    - Contributor **and** User Access Administrator roles
    - Owner role
- [ ] **Azure Quotas**: Ensure sufficient quotas for services like Compute, Storage, Cosmos DB, and OpenAI.
- [ ] **Dependencies Installed**:
    - [ ] PowerShell modules
    - [ ] Azure CLI and necessary extensions
- [ ] **Disable Internet Explorer Enhanced Security Configuration**: Required for PowerShell scripts interacting with MS Graph API.
- [ ] **Azure Resource Provider Registration**: Each Azure service requires its corresponding resource provider to be registered at the subscription level before you can create or manage resources of that type. If you have previously used a service in the target Azure subscription, the Resource Provider is likely already registered. If they are not registered, you may encounter errors when trying to deploy resources.

    ??? info "Resouce Provider Mapping"
        | **Azure Service**                          | **Required Resource Provider Namespace**       |
        |--------------------------------------------|-----------------------------------------------|
        | Azure Key Vault                            | `Microsoft.KeyVault`                          |
        | Cosmos DB                                   | `Microsoft.DocumentDB`                        |
        | Cognitive Services (e.g., Form Recognition) | `Microsoft.CognitiveServices`                 |
        | App Service (Web Apps, Function Apps)       | `Microsoft.Web`                               |
        | Azure Storage                               | `Microsoft.Storage`                           |
        | Application Insights                        | `Microsoft.Insights`                          |
        | Azure OpenAI Services                       | `Microsoft.CognitiveServices`                 |
        | Virtual Machines (if applicable)            | `Microsoft.Compute`                           |
        | Azure Active Directory (Azure AD/Entra ID)  | `Microsoft.AAD`                               |

    ??? info "Azure CLI command to check if all required Resource Providers are registered"
        ``` bash
        az provider show --namespace Microsoft.KeyVault
        az provider show --namespace Microsoft.DocumentDB
        az provider show --namespace Microsoft.CognitiveServices
        az provider show --namespace Microsoft.Web
        az provider show --namespace Microsoft.Storage
        az provider show --namespace Microsoft.Insights
        az provider show --namespace Microsoft.Compute
        az provider show --namespace Microsoft.AAD
        ```

---

## Installation Package Overview

Before proceeding with the installation, familiarize yourself with the contents of the installation package. Each file has a specific role in the installation and configuration of the GPT-X Platform. Below is a description of the key files and folders included in the package.

| **File/Folder**                          | **Description**                                                                                                    |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| `GPT-X-Setup.bat`                        | A batch file that initiates the installation process. It serves as the entry point for running the installation scripts. |
| `iHealthSetup.ps1`                       | The main PowerShell script responsible for creating and configuring Azure resources as part of the installation.     |
| `Logger.ps1`                             | A PowerShell script that logs the installation steps and tracks any issues or errors encountered during the process. |
| `GPT-X_Installation_Guide.<version>.pdf` | The installation guide in PDF format, providing detailed steps and explanations for setting up the GPT-X Platform.   |
| `$Installation<version>.txt`               | A text file containing installation keys and other information regarding the setup process.             |
| `$ReleaseNotes_<version>.xml`                 | A document outlining the latest updates, improvements, and known issues for the given release of the GPT-X Platform. |
| `error.txt`                                  | This file appears if an error occurs during the installation, containing specific error messages to help with troubleshooting. |
| `logs/`                          | Contains log files that provide detailed information on the installation process, useful for debugging any issues.    |



---

## Installation Steps

### 1. Run the Installer

Launch the Command Line, navigate to the GPT-X directory, and execute `GPT-X-Setup.bat` to start the installation.

### 2. Checking/Installing Prerequisites

The installation script will verify the following:

- **Azure CLI**: Checks for the required version and prompts for installation or upgrade.
- **Azure CLI Extensions**: Installs necessary extensions.
- **PowerShell Modules**: Installs or updates required modules.
- **Installation Key**: The installation will request your Installation Key. This can be found in the `$Installation<version>.txt` file.

### 3. Key Vault Selection/Creation

**Select or Create Key Vault**: The script will search for exisitng Key Vaults and give you the option whether to choose an existing Key Vault, or create a new one (reccomended for new installations).

**Resource Group Selection**: Select an existing Resource Group or create a new one.

**Permissions**: Ensure you have access rights to the Key Vault if upgrading.

**Resources Created**:

- **Key Vault**: `GPT-X-KV-<InstallationId>`

**Key Vault Secrets Created**:

- `ToFInstallationId`
- `ToFInstallationGuid`
- `ToFSubscriptionId`
- `ToFResourceGroup`

*Note: The Installation ID is a 12-digit random number used for resource naming.*

### 4. Storage Account Selection/Creation

**Storage Account Options**: Select an existing Storage Account or create a new one.

**Naming**: New Storage Accounts will be named `gptxstore<InstallationId>`.

**Key Vault Secrets Created/Updated**:

- `StorageAccountConnection`

*Note: Function Apps cannot reference Storage Accounts in other Azure subscriptions.*

### 5. Cosmos DB Selection/Creation

**Cosmos DB Options**: Select an existing Cosmos DB Account or create a new one.

**Naming**: New Cosmos DB Accounts will be named `gptorchestrator-<InstallationId>`.

**Key Vault Secrets Created/Updated**:

- `CosmosDBAccountName`
- `CosmosDBKey`

### 6. Form Recognition Cognitive Service

**Service Options**: Select an existing Form Recognition service or create a new one.

**Naming**: New services will be named `OCR4Images-<InstallationId>`.

**Key Vault Secrets Created/Updated**:

- `OCR4ImagesName`
- `OCR4ImagesKey`
- `OCR4ImagesURL`

### 7. Speech Service Selection/Creation

**Service Options**: Select an existing Speech Service or create a new one.

**Naming**: New services will be named `GPT-X-Speech-<InstallationId>`.

**Key Vault Secrets Created/Updated**:

- `GPT-X-SpeechName`
- `GPT-X-SpeechKey`
- `GPT-X-SpeechURL`

### 8. OpenAI Service Pool Creation

**Define Pool Size**: Enter the number of OpenAI services to create (up to 20).

**Select Model**: Choose the OpenAI model to deploy across the services. Reccomended: GPT-4o.

**Service Creation**: The script will create or reuse services, potentially across multiple subscriptions/locations based on quota availability.

**Naming**: Services will be named `GPT-X-OpenAI-<InstallationId>`, `GPT-X-OpenAI4Search-<InstallationId>`

**Key Vault Secrets Created/Updated**:

- `OpenAIKey`
- `OpenAIName`
- `OpenAIURL`
- `OpenAIModelName`
- `OpenAIModelDeploymentURL`

### 9. Application and Function Deployment

#### PublishGPTPlans Utility

- **Deployment Location**:
    - `Program Files (x86)\GPT-X-PIE\PublishGPTPlans-<InstallationId>`
- **Data Deployment**:
    - Select a root folder when prompted to deploy utility data.

#### GPTOrchestratorSvc Function App

- **Deployment**:
    - The script deploys the `GPTOrchestratorSvc-<InstallationId>` Function App.
- **Resources Created**:
    - Function App
    - App Service Plan
    - Application Insights

**Key Vault Secrets Created/Updated**:

- `GPTOrchestratorSvcAccessKey`

#### ChatGPT-X App Service

- **Deployment**:
    - Deploys `ChatGPT-X-<InstallationId>` Web App with Azure AD registration.
- **Resources Created**:
    - Web App
    - App Service Plan
    - Application Insights
    - Azure AD Application

**Key Vault Secrets Created/Updated**:

- `ChatGPT-X-ClientId`
- `ChatGPT-X-ClientSecret`

### 10. Microsoft Teams App Deployment

1. **Connect to Microsoft Teams**:
    - The script will attempt to connect using your current Azure account.
    - If unsuccessful, you will be prompted to log in with another account.
2. **Approve Permissions**:
    - Grant the necessary permissions for `ChatGPT-X-<InstallationId>` application.
    - **Admin Consent**: It's recommended to provide admin consent on behalf of your organization.
3. **Application Naming**:
    - You will be prompted to enter or modify the Teams application name.

---

## Post-Installation Steps

### Verification

1. **Azure Portal Check**:
    - Log into the Azure Portal and verify that all resources have been created successfully.
2. **Service Status**:
    - Ensure that all services are running and not in a failed state.
3. **Key Vault Secrets**:
    - Verify that all necessary secrets have been populated in the Key Vault.

### Initial Configuration

1. **User Setup**:
    - Add necessary users and assign appropriate roles within the application.
2. **Azure AD Integration**:
    - Confirm that the Azure AD application is properly configured for authentication.
3. **Application Settings**:
    - Review and adjust application settings as needed in the Azure Portal.

### Testing the Installation

1. **Functionality Test**:
    - Use provided sample scripts or interfaces to test the functionality of the GPT-X Platform.
2. **Service Connectivity**:
    - Test connections to OpenAI services, Cosmos DB, and other integrated services.

### Best Practices for Production Environments

- **Scaling**: Adjust resource capacities to match production workloads.
- **High Availability**: Implement multi-region deployments if necessary.
- **Monitoring**: Set up alerts and monitoring dashboards using Application Insights.

---

## Maintenance and Monitoring

### System Monitoring

- **Application Insights**:
    - Utilize Application Insights for performance monitoring and diagnostics.
- **Azure Monitor**:
    - Set up Azure Monitor to track resource utilization and health.

### Resource Scaling

- **Manual Scaling**:
    - Adjust resource tiers for services like Cosmos DB and App Service Plans through the Azure Portal.
- **Auto-Scaling**:
    - Configure auto-scaling rules where applicable to handle variable workloads.

### Updating and Patching

- **Application Updates**:
    - Follow provided instructions for updating the GPT-X application when new versions are released.
- **Azure Updates**:
    - Keep Azure services up to date by applying patches and updates as recommended by Microsoft.

---

## Terraform Installation Method

### Can I use Terraform to install GPT-X instead of PowerShell and the CLI?

Yes, you can use **Terraform** to install GPT-X, but we recommend starting with the supported installation method in a development/test sandbox environment. This will help you understand the necessary Azure resources and configurations before deploying them with Terraform.

### Recommended Workflow

1. **Sandbox Installation**:  
   Begin by performing the standard installation in a development or test sandbox environment using our **PowerShell and Azure CLI** method. This process automatically sets up and configures all necessary Azure resources.
   
2. **Testing and Validation**:  
   After the sandbox installation is complete, test the system to ensure that all components and applications are functioning as expected. This step also helps you observe the resource configurations that have been applied.
   
3. **Terraform Configuration**:  
   Once the sandbox environment is working, you can replicate the setup using Terraform for other environments like QA or Production. Inspect the resources created in the sandbox and use those configurations as a basis for writing your Terraform scripts.
   
    _Example Terraform Resource Block_
    ```hcl
    resource "azurerm_resource_group" "gptx" {
      name     = "GPTX-ResourceGroup"
      location = "East US"
    }

    resource "azurerm_storage_account" "gptx_store" {
      name                     = "gptxstore123456"
      resource_group_name      = azurerm_resource_group.gptx.name
      location                 = azurerm_resource_group.gptx.location
      account_tier             = "Standard"
      account_replication_type = "LRS"
    }
    ```

4. **Resource Management**:
    During installation, you can choose to select existing Azure resources if applicable. This provides flexibility in managing and deploying resources across multiple environments.

By following this method, you can ensure that all required resources are correctly configured and tested before deploying GPT-X using Terraform in critical environments.

---

## Uninstallation and Rollback Procedures

### Uninstallation Process

1. **Run Uninstall Script**:
    - Use the provided uninstallation script to remove GPT-X resources.
2. **Manual Cleanup**:
    - Verify that all resources have been deleted from the Azure Portal.
    - Remove any residual files from the local machine.

### Rollback

1. **Backup Restoration**:
    - Restore configurations and data from backups taken prior to installation.
2. **Version Rollback**:
    - If downgrading, follow the installation steps for the previous version using the backup Installation ID and Key Vault.

---

## Troubleshooting

### Common Errors and Fixes

- **Script Execution Disabled**:
    - **Error**: `iHealthSetup.ps1 cannot be loaded because running scripts is disabled on this system.`
    - **Solution**: Adjust PowerShell execution policies as described in the Pre-Installation Setup.

- **Insufficient Permissions**:
    - **Solution**: Ensure that you have the required Azure and local administrative permissions.

- **Quota Limits Reached**:
    - **Solution**: Check Azure subscription quotas and request increases if necessary.

### Log File Location

- **Installation Logs**:
    - Located in `%LOCALAPPDATA%\GPT-X-Logs\`
- **Azure Activity Logs**:
    - Accessible via the Azure Portal under Monitor > Activity Log.

---

## Support Information

### Contact Support

- **Email**: ...
- **Phone**: ...
- **Support Portal**: ...

---

## Appendix

### A. Glossary of Terms

- **Azure AD (Azure Active Directory)**: Microsoft’s cloud-based identity and access management service.
- **Key Vault**: Azure service for storing and accessing secrets securely.
- **Function App**: Azure service for running small pieces of code (functions) without worrying about application infrastructure.
- **App Service Plan**: Defines the compute resources for your web app.

### B. Resource Naming Conventions

- **Key Vault**: `GPT-X-KV-<InstallationId>`
- **Storage Account**: `gptxstore<InstallationId>`
- **Cosmos DB Account**: `gptorchestrator-<InstallationId>`
- **OpenAI Services**: `GPT-X-OpenAI-<InstallationId>`, `GPT-X-OpenAI2-<InstallationId>`, etc.
- **Function App**: `GPTOrchestratorSvc-<InstallationId>`
- **Web App**: `ChatGPT-X-<InstallationId>`

*Note: `<InstallationId>` is a unique 12-digit number generated during installation.*

### C. Version History

| Version | Date          | Description                                                                           |
|---------|---------------|---------------------------------------------------------------------------------------|
| 0.0     | 10/3/2024     | Initial release of the installation guide. Need to confirm details and import images. |
| 0.1     | 10/8/2024     | Format changes and addition of Azure Resource Provider Registration pre-requisite.    |