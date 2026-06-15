# INV_CLM_ICN

> This table holds information of claim override internal control number (ICN) on A/R Invoice (INV) for Resolute Professional Billing.

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The invoice record ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CLM_OVRD_ICN_CVG_ID` | INTEGER |  | The override coverage ID for the internal control number for the claim. |
| 4 | `CLM_OVERRIDE_ICN` | VARCHAR |  | The override internal control number for the claim. |
| 5 | `CLM_OVRD_ICN_T_DTTM` | DATETIME (Attached) |  | The override edit time for the internal control number for the claim. |
| 6 | `CLM_OVRD_ICN_USR_ID` | VARCHAR |  | The override edit user for the internal control number for the claim. |
| 7 | `CLM_OVRD_ICN_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `CLM_OVRD_ICN_IGN_YN` | VARCHAR |  | Whether or not the override for the internal control number for the claim was ignored. |
| 9 | `CLM_OVRD_ICN_CMNT` | VARCHAR |  | The override comment for the internal control number for the claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

