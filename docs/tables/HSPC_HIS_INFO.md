# HSPC_HIS_INFO

> Contains information about Hospice Item Sets, such as the status, reason for record, and version.

**Primary key:** `DATASET_ID`  
**Columns:** 9  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DATASET_ID` | NUMERIC | PK shared | The unique identifier for the data set record. |
| 2 | `DATASET_NAME` | VARCHAR |  | The name of the dataset, formatted as the patient's name and the reason for record. |
| 3 | `INSTANT_NOADD_EDIT_DTTM` | DATETIME (Local) |  | The date and time that data that is not specific to a contact was edited for a data set. |
| 4 | `NOADD_ITEMS_EDITED` | VARCHAR |  | Data that is not specific to a contact that was edited for a data set. |
| 5 | `DATASET_STATUS_C_NAME` | VARCHAR | org | This item contains the current submission status of the Hospice Item Set. |
| 6 | `DATASET_TYPE_C_NAME` | VARCHAR |  | Stores what type of dataset the record is. Currently datasets can be OASIS or HIS. |
| 7 | `HIS_TYPE_C_NAME` | VARCHAR |  | Stores the reason for record (e.g. Admission or Discharge) of the HIS Dataset. This corresponds to item A0250 on the Hospice Item Set. |
| 8 | `HIS_VERSION_C_NAME` | VARCHAR | org | Version of Hospice Item Set to use. |
| 9 | `HIS_EPISODE_ID` | NUMERIC |  | The unique identifier of the hospice episode of care record associated with an HIS data set record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

