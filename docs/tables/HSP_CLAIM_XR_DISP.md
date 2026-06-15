# HSP_CLAIM_XR_DISP

> This table contains the information used to display the details of calculations performed by contract pricing extensions when calculating expected reimbursement.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the claim print record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `XR_DISP_LINE_NUM` | VARCHAR |  | The line number to be displayed in the expected reimbursement detail of the Hospital Billing liability bucket. May include other characters for aid in display formatting. |
| 4 | `XR_DISP_DESCRIPTION` | VARCHAR |  | The explanatory or descriptive text to be displayed in the Hospital Billing Liability Bucket detail. This may be the description of a calculated quantity, which may include the arithmetic used in the calculation. It can also be the header used to label a section of the reimbursement calculation. |
| 5 | `XR_DISP_AMT` | NUMERIC |  | The amount calculated or other values for a line in the expected reimbursement detail of the Hospital Billing liability bucket. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

