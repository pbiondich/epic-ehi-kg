# CLM_DX

> All values associated with a claim are stored in the Claim External Value record. The CLM_DX table holds the diagnoses for the claim.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the Claim Info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `CLM_DX_QUAL` | VARCHAR |  | This item holds the qualifier identifying the code set for the claim diagnoses. |
| 4 | `CLM_DX` | VARCHAR |  | This item holds the diagnoses for the claim. The principal diagnosis is stored on the first line and the other diagnoses are on subsequent lines. |
| 5 | `CLM_DX_POA` | VARCHAR |  | This item identifies if the diagnosis was present when the patient was admitted. |
| 6 | `CLM_DX_CODE_SET_OID` | VARCHAR |  | The object ID (OID) for the diagnosis code set. |
| 7 | `CLM_DX_RANK` | INTEGER |  | This item holds the explicit rank of the diagnoses when it is present in the raw claims data. |
| 8 | `CLM_DX_FROM_HEADER_YN` | VARCHAR |  | Indicates whether the diagnosis was received at the header level. |
| 9 | `RX_DX_QUAL` | VARCHAR |  | This item holds the qualifier identifying the code set for the claim diagnoses on a pharmacy claim. |
| 10 | `CLM_AP_DX_POA_C_NAME` | VARCHAR |  | The present on admission (POA) indicator code for the diagnosis. |
| 11 | `DX_TYPE` | VARCHAR |  | This item stores the diagnosis type of the claim. |
| 12 | `DX_INFO_TYPE` | VARCHAR |  | This item stores the information type of the diagnosis info code. |
| 13 | `CMS_DX_TYPE` | VARCHAR |  | The CMS code classifying the diagnosis type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

