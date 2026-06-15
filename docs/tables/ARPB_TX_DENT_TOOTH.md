# ARPB_TX_DENT_TOOTH

> The DENTAL_TOOTH table contains tooth information. Since one transaction may be associated with multiple teeth, each row in this table represents one tooth code and is identified by the transaction ID (TX_ID) and tooth line number (TOOTH_NUMBER).

**Primary key:** `TX_ID`, `TOOTH_LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `TOOTH_LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TOOTH_NUM_C_NAME` | VARCHAR |  | The tooth number category ID for the charge. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

