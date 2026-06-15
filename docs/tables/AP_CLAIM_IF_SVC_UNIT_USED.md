# AP_CLAIM_IF_SVC_UNIT_USED

> The quantitative measure of services. As an output from grouping, it may be different, after processing, from the ItemUnitsOfService input (which can be found in Clarity table AP_CLAIM_IF_OUT_SVC_UNITS). For outpatient reimbursement processing only, this field is used for input instead of the ItemUnitsOfService input field.

**Primary key:** `CLAIM_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `SVC_UNITS_USED` | VARCHAR |  | The quantitative measure of services. As an output from grouping, it may be different, after processing, from the ItemUnitsOfService input (which can be found in Clarity table AP_CLAIM_IF_OUT_SVC_UNITS). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

