# LAB_CASE_SNOMED

> The LAB_CASE_SNOMED table stores SNOMED related information for case (REQ) records.

**Primary key:** `REQUISITION_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REQUISITION_ID` | NUMERIC | PK shared | The unique identifier for the case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SNOMED_CUI` | VARCHAR |  | The unique SNOMED SmartData Identifier (HLX-40) for the Lexicon master file that is stored on this case. |
| 4 | `CODE_SEL_METHOD_C_NAME` | VARCHAR |  | The code selection method category number for the SNOMED code stored on the case. |
| 5 | `SNOMED_CODE` | VARCHAR |  | Stores the actual SNOMED code on the case for reporting purposes. |
| 6 | `SOURCE_TEST` | VARCHAR |  | Holds the tests selected for the source result during automatic SNOMED code generation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

