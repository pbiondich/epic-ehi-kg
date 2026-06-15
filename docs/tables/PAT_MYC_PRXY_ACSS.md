# PAT_MYC_PRXY_ACSS

> Proxy access in web based chart system provides the means for one patient to view data for another patient. A typical use of this functionality is for a parent to be able to view their minor child's medical record. The items in this table keep track of current proxy relationships.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting’s security utility. |
| 2 | `LINE` | INTEGER | PK | Since a patient may have more than one proxy relationship, the line number identifies each relationship for a given patient. |
| 3 | `PROXY_PREFERENCES_ID` | NUMERIC |  | The ID number of the communication preferences record for the proxy. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

