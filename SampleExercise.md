### Exercise: Create a Blob Storage Account

**Context:** Imagine you've been tasked with setting up a reliable storage solution for your company's growing collection of media files. By creating a Blob storage account in Azure, you'll ensure that these files are securely stored and easily accessible whenever needed, supporting various applications across your organisation.

**Instructions:**
- Navigate to the Azure portal and log in to your account.
- Click on "Create a resource" and search for "Storage account".
- Select "Storage account" from the search results.
- Fill out the required fields such as subscription, resource group, and storage account name.
- Choose your preferred location and replication options.
- Review the settings and click "Create" to provision your Blob storage account.

**Question:**  

Which option is NOT a valid replication option for Azure Blob storage?

A) Locally redundant storage (LRS)  
B) Zone-redundant storage (ZRS)  
C) Geo-redundant storage (GRS)  
D) Regionally redundant storage (RRS)  

**Clue:** This replication option ensures redundancy within the same region but not across regions.

**Correct Answer: D**

### Explanation:
- **Locally redundant storage (LRS)**: Provides redundancy within the same data center.
- **Zone-redundant storage (ZRS)**: Replicates data across multiple availability zones within a region.
- **Geo-redundant storage (GRS)**: Replicates data to a secondary region hundreds of miles away from the primary location.
- **Regionally redundant storage (RRS)**: **Not a valid option**; Azure does not offer a replication option specifically named "Regionally redundant storage" for Blob storage.
