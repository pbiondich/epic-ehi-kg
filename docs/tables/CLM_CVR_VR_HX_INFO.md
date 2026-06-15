# CLM_CVR_VR_HX_INFO

> This table contains contraceptive vaginal ring (CVR) void or resubmit history information.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the Claim Info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CVR_VR_HX_TYPE_C_NAME` | VARCHAR |  | Contraceptive vaginal ring (CVR) resubmission or void history type. |
| 4 | `CVR_VR_HX_USER_ID` | VARCHAR |  | Contraceptive vaginal ring (CVR) resubmission or void history user ID. |
| 5 | `CVR_VR_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `CVR_VR_HX_TIME` | DATETIME (Local) |  | Contraceptive vaginal ring (CVR) resubmission or void history time stamp. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

