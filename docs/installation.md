# Installation

Instructions for installing the project.

## Prerequisites
- Dedicated Azure Virtual Machine for the installation
- Azure OpenAI Service Quota
- Installer must have the following permissions:
    - **MS Windows Administrator Role** or membership in the local Administrators group on the PC/VM.  
      Required for installation via PowerShell, which installs the product binaries and disables Internet Explorer Enhanced Security Configuration (ESC).
    - **Application Administrator role** in Azure Active Directory (Entra ID).  
      Allows for creating and managing applications in the Azure tenant.  
      [Learn More](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference)
    - **Contributor, User Access Administrator, or Owner roles** in the Azure Subscription.  
      Required for managing Azure resources during the installation.  
    [Learn More](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)

## GPT-X Setup Scripts

- **GPT-X-Setup.bat**: Batch file to run the installation.
- **iHealthSetup.ps1**: PowerShell script for the installation process.
- **Logger.ps1**: PowerShell script for logging installation activities.

## Teams Integration

- **Microsoft Entra ID App Registration**  
  Purpose: The GPT-X Teams application will be registered in Azure Active Directory.  
  [Learn More](https://learn.microsoft.com/en-us/azure/active-directory/develop/app-registrations-overview)

- **Service Principal Consent**: The installer will need Global Administrator access for Microsoft Teams to approve permissions and give consent on behalf of the organization.