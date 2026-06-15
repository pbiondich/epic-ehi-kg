# DENT_EOB_INFO

> This table contains explanation of benefits (EOB) information for the dental treatment plan.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | VARCHAR | PK shared | The unique identifier for the treatment plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EOB_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 4 | `EOB_AUTH_NUM` | VARCHAR |  | The authorization number of the Explanation of Benefits (EOB) information. |
| 5 | `EOB_AUTH_DATE` | DATETIME |  | The date when the payor sent Explanation of Benefits authorization. |
| 6 | `EOB_TOTAL_AMOUNT` | NUMERIC |  | The total EOB amount. |
| 7 | `EOB_COVERED_AMOUNT` | NUMERIC |  | The covered amount of the EOB information. |
| 8 | `EOB_ENTRY_DATE` | DATETIME |  | The date when the Explanation of Benefits information was entered in the system. |
| 9 | `EOB_DELETED_YN` | VARCHAR |  | Indicates whether a EOB information is deleted for the dental treatment plan. Y indicates that the EOB information is deleted. N or a null value indicates that EOB information is not deleted. |
| 10 | `EOB_ENTRY_USER_ID` | VARCHAR |  | The unique ID of the user record who entered the Explanation of Benefits information. This column is frequently used to link to the CLARITY_EMP table. |
| 11 | `EOB_ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `EOB_ENTRY_TIME` | DATETIME |  | The time when EOB information was entered in the system. |
| 13 | `EOB_DEL_USER_ID` | VARCHAR |  | The unique ID of the user record who deleted the Explanation of Benefits information. This column is frequently used to link to the CLARITY_EMP table. |
| 14 | `EOB_DEL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `EOB_DEL_DATE` | DATETIME |  | The date when the Explanation of Benefits information was deleted from the system. |
| 16 | `EOB_DEL_TIME` | DATETIME |  | The date when EOB information was entered in the system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

