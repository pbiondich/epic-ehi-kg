# CLM_PROGRAM_INFO

> Contains the Value Based Program Identifier (I CEV 30001).

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim value record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROGRAM_IDENT` | VARCHAR |  | This item contains program identifiers representing internal Value Based Program (VBP) records from the payer instance, as part of Claims Exchange |
| 4 | `PROGRAM_NAME` | VARCHAR |  | This item holds the external program description of the program associated with a claim in an EOB resource. |
| 5 | `PROGRAM_REM_STATUS` | VARCHAR |  | This item holds the external program removal status of the program associated with a claim in a FHIR claim resource. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

