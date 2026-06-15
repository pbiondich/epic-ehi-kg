# CL_RMT_CLAIM_QTY

> Contains claim supplemental quantity information from the electronic remittance payment. This information is sent in the QTY segment of an ANSI 835 Health Care Claim Payment/Advice file. This segment is used to send quantity information associated with the claim being paid. These quantities are in defined categories and sent only when the quantity is non-zero. This information is stored in the remittance image record.

**Primary key:** `IMAGE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | ID for the remittance image record containing the claim supplemental information. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CLM_QTY_QUAL_C_NAME` | VARCHAR |  | The quantity qualifier code for the claim supplemental quantity information. This is a standard code that indicates what the quantity represents. |
| 4 | `CLAIM_SUPPL_QTY` | NUMERIC |  | Quantity for the supplemental claim quantity information. The specific meaning of this quantity is indicated by the associated quantity qualifier code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

