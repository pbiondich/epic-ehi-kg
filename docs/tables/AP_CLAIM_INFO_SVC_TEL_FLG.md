# AP_CLAIM_INFO_SVC_TEL_FLG

> Identifies a HCPCS line item that is a telehealth service or is reported with a Telehealth Modifer (95, GT, G0 or GQ) and/or a place of service value of 2.

**Primary key:** `CLAIM_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the claim info record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `TLH_SVC_FLG` | VARCHAR |  | Identifies a HCPCS line item that is a telehealth service or is reported with a Telehealth Modifer (95, GT, G0 or GQ) and/or a place of service value of 2. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

