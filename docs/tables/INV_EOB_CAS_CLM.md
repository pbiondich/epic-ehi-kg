# INV_EOB_CAS_CLM

> This table holds the edited explanation of benefits (EOB) information for a claim to be used by claim processing for any claim associated with this invoice (INV).

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The invoice record ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EDIT_EOB_CLM_CVG_ID` | NUMERIC |  | The edited explanation of benefits coverage at the claim level. |
| 4 | `EDIT_EOB_GRP_CLM_C_NAME` | VARCHAR | org | The edited explanation of benefits group code at the claim level. |
| 5 | `EDIT_EOB_RMT_CD_CLM` | VARCHAR |  | The edited explanation of benefits remit code at the claim level. |
| 6 | `EDIT_EOB_AMT_CLM` | NUMERIC |  | The edited explanation of benefits amount at the claim level. |
| 7 | `EDIT_EOB_QTY_CLM` | INTEGER |  | The edited explanation of benefits quantity at the claim level. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

