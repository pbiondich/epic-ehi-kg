# NSQIP_OPIOIDS_DISCHARGE

> The NSQIP_OPIOIDS_DISCHARGE table contains information on opioids prescribed at discharge for NSQIP registry data for the surgeries that are selected for NSQIP submission. It is used in conjunction with NSQIP_INFO table.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 13  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `REGISTRY_TYPE_C_NAME` | VARCHAR | org | Stores the type of registry |
| 3 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, etc...) |
| 4 | `NSQIP_OPIOID_TYPE_C_NAME` | VARCHAR |  | Indicates the type of opioid prescribed at discharge. |
| 5 | `NSQIP_OP_TYPE_OTHER` | VARCHAR |  | Stores comments related to opioid type. |
| 6 | `NSQIP_OP_METHOD_C_NAME` | VARCHAR |  | Indicates the method of administration for the opioid. |
| 7 | `NSQIP_OP_MTH_OTHER` | VARCHAR |  | Stores comments related to opioid method type. |
| 8 | `NSQIP_OPIOID_DOSE` | NUMERIC |  | Stores the opioid dosage amount. |
| 9 | `NSQIP_OP_DOSE_UNT_C_NAME` | VARCHAR |  | Stores the unit of the dose entered in the dose item. |
| 10 | `NSQIP_OP_LIQUID_VOL` | NUMERIC |  | Stores the opioid liquid volume. |
| 11 | `NSQIP_DOSE_FREQ_C_NAME` | VARCHAR |  | Indicates the opioid dose frequency. |
| 12 | `NSQIP_PRS_DOSE_TTL` | INTEGER |  | Stores the total number of opioid doses prescribed. |
| 13 | `NSQIP_PRS_RENEW_YN` | VARCHAR |  | Indicates if patient had opioid prescription renewed or not. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

