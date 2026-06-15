# INV_NDC_INFO

> This table holds the National Drug Code (NDC) information for the invoice (INV) record.

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The invoice record ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NDC_ID` | VARCHAR | FK→ | The national drug code record ID. |
| 4 | `NDC_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 5 | `NDC_NUM` | VARCHAR |  | The national drug code number. |
| 6 | `NDC_QTY` | NUMERIC |  | The national drug code quantity. |
| 7 | `NDC_UNITS_C_NAME` | VARCHAR |  | The billable units for the national drug code. |
| 8 | `LINE_PTR` | NUMERIC |  | The invoice line for the national drug code. |
| 9 | `MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 10 | `RX_NUM` | VARCHAR |  | The prescription number. |
| 11 | `COMPOUND_LINK_NUM` | VARCHAR |  | The link sequence number for an associated ingredients in a compound drug. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |
| `NDC_ID` | [RX_NDC](RX_NDC.md) | sole_pk | high |

