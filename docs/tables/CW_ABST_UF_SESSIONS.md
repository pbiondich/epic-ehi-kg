# CW_ABST_UF_SESSIONS

> Ultrafiltration sessions adequacy information from abstractions with clinical hemodialysis information reported to CROWNWeb, the United States ESRD patient registry.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UF_SESSION_ID` | VARCHAR |  | The hemodialysis patient's ultrafiltration session ID. |
| 4 | `UF_SESSION_DATE` | DATETIME |  | The hemodialysis patient's ultrafiltration session date. |
| 5 | `UF_SESSION_PRE_WEIGHT_VALUE` | NUMERIC |  | The hemodialysis patient's ultrafiltration session pre-treatment weight. |
| 6 | `UF_SESSION_PRE_WEIGHT_UNIT_C_NAME` | VARCHAR | org | The hemodialysis patient's ultrafiltration session pre-treatment weight unit. |
| 7 | `UF_SESSION_POST_WEIGHT_VALUE` | NUMERIC |  | The hemodialysis patient's ultrafiltration session post-treatment weight. |
| 8 | `UF_SESSION_POST_WEIGHT_UNIT_C_NAME` | VARCHAR |  | The hemodialysis patient's ultrafiltration session post-treatment weight unit. |
| 9 | `UF_SESSION_DELIVERED_MINUTES` | INTEGER |  | The hemodialysis patient's ultrafiltration session delivered minutes. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

