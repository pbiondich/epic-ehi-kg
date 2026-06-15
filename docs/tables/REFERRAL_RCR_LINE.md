# REFERRAL_RCR_LINE

> This table holds information about individual lines in a referral classifier rules table.

**Primary key:** `TABLE_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TABLE_ID_TABLE_NAME` | VARCHAR |  | The name of the referral rules table record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REQ_CLASSIFIER_ID` | VARCHAR |  | Stores the ID for the classifier required associated with this line of the referral classifier rules. |
| 4 | `REQ_CLASSIFIER_ID_CLASSIFIER_NAME` | VARCHAR |  | The title of the classifier record. |
| 5 | `NETWORK_LEVELS_C_NAME` | VARCHAR | org | The network status associated with this line of the referral classifier rules. |
| 6 | `AVAIL_CLASSIFIER_ID` | VARCHAR |  | Stores the ID for the classifier available associated with this line of the referral classifier rules. |
| 7 | `AVAIL_CLASSIFIER_ID_CLASSIFIER_NAME` | VARCHAR |  | The title of the classifier record. |
| 8 | `USE_UC_FEE_SCHED_YN` | VARCHAR |  | Set to "Y" if the Usual and Customary Fee Schedule is used for this line of the referral classifier rules. Otherwise, set to "N". |
| 9 | `PROV_PNLTY_TYPE_C_NAME` | VARCHAR |  | The penalty associated with this line of the referral classifier rules. |
| 10 | `EOB_CODE_ID_EOB_CODE_NAME` | VARCHAR |  | The name of the processing code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

