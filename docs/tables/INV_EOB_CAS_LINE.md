# INV_EOB_CAS_LINE

> This table holds the edited explanation of benefits (EOB) information at the line level for a claim associated with this invoice.

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The invoice ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EDIT_EOB_CVG_ID` | NUMERIC |  | The edited explanation of benefits coverage. |
| 4 | `EDIT_EOB_CLM_LN` | INTEGER |  | The edited explanation of benefits line. |
| 5 | `EDIT_EOB_GRP_LN_C_NAME` | VARCHAR | org | The edited explanation of benefits line group code. |
| 6 | `EDIT_EOB_RMT_CD_LN` | VARCHAR |  | The edited explanation of benefits line remittance code. |
| 7 | `EDIT_EOB_AMT_LN` | NUMERIC |  | The edited explanation of benefits line level service adjustment. |
| 8 | `EDIT_EOB_QTY_LN` | INTEGER |  | The edited explanation of benefits line quantity. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

