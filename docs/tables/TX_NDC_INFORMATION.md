# TX_NDC_INFORMATION

> This table contains Medical National Drug Code (NDC) information. Since one transaction may be associated with multiple NDC codes, each row in this table represents one NDC code and is identified by the transaction ID and line number. The data for this table is extracted using a KB_SQL query.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique accounts receivable transaction record ID. |
| 2 | `LINE` | INTEGER | PK | Line number to identify each row of Medical National Drug Code (NDC) data associated with an individual transaction. |
| 3 | `NDC_CODES_ID` | VARCHAR |  | The ID of the Medical National Drug Code (NDC) associated with a transaction. |
| 4 | `NDC_CODES_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 5 | `NDC_CODES_ADMIN_AMT` | NUMERIC |  | The NDC amount associated with this charge. |
| 6 | `NDC_CODES_UNIT_C_NAME` | VARCHAR |  | The Medical National Drug Code (NDC) unit associated with the charge. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

