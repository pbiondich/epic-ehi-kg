# HSP_PMT_LINE_REMIT

> This is a type of summary level of the remittance actions associated with a payment transaction. This table will summarize remittance information from Electronic Remittance and manual payment posting as stored on the transaction. This table is meant to hold a high level summary of line-level reason code information. Data will not be populated if a payment was posted at the invoice-level.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LINE_SVCLINE` | INTEGER |  | Stores the service line number for line level payments. |
| 4 | `LINE_GRP_CODE_C_NAME` | VARCHAR | org | Stores the group code corresponding to the reason code at the line level. |
| 5 | `LINE_REMIT_CODE_ID` | VARCHAR |  | Stores the reason code or remark code from the service line. |
| 6 | `LINE_REMIT_CODE_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 7 | `LINE_RSN_CODE_EXTL` | VARCHAR |  | Stores the external claim level reason code or remark code from the service line. |
| 8 | `LINE_RMT_AMT` | NUMERIC |  | Stores the amount associated with the reason code at the line level. |
| 9 | `LINE_RMK_CODES` | VARCHAR |  | Stores information about the remark codes that are associated with specific reason codes at the line level. This is a comma delimited list of remark codes. The system will associate all remark codes present at any particular service line to every reason code on the same line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

