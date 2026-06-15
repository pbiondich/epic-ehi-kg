# CW_ABST_VASCULAR_ACCESS

> Vascular access information from abstractions with clinical hemodialysis or other dialysis information reported to the United States ESRD patient registry.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `VA_SESS_DATE` | DATETIME |  | The dialysis patient's vascular access session date. |
| 3 | `VA_TYPE_C_NAME` | VARCHAR |  | The dialysis patient's current vascular access type. |
| 4 | `VA_CHANGE_DATE` | DATETIME |  | The dialysis patient's vascular access change date. |
| 5 | `AVF_USABLE_DATE` | DATETIME |  | The dialysis patient's vascular access arteriovenous fistula change date. |
| 6 | `AVF_IS_MATURING_YN` | VARCHAR |  | Shows whether the dialysis patient's vascular access arteriovenous fistula is maturing or not. |
| 7 | `AVF_STATE_C_NAME` | VARCHAR |  | The dialysis patient's vascular access arteriovenous fistula current state. |
| 8 | `AVF_CREATION_DATE` | DATETIME |  | The dialysis patient's vascular access arteriovenous fistula creation date. |
| 9 | `AVG_IS_MATURING_YN` | VARCHAR |  | Shows whether the dialysis patient's vascular access arteriovenous fistula graft is maturing or not. |
| 10 | `AVG_STATE_C_NAME` | VARCHAR |  | The dialysis patient's vascular access arteriovenous fistula graft current state. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

