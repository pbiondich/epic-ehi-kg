# TC_REQUEST_PROV_DOC

> This contains the decisions that were made by potential accepting providers about whether to accept or decline a Transfer Center request.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique identifier for the communication record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONTACT_IDNT` | INTEGER |  | This stores the line number of a Contact Log entry that made a decision on whether or not to accept a Transfer Center request. |
| 4 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 5 | `PAT_SERVICE_C_NAME` | VARCHAR | org | The hospital service category ID for which a decision was made about whether or not to accept a Transfer Center request. |
| 6 | `PROV_APPROVED_YN` | VARCHAR |  | Indicates whether a provider approved or declined a Transfer Center request. 'Y' indicates that the provider approved the transfer. 'N' indicates that they did not approve the transfer. |
| 7 | `DECISION_INST_DTTM` | DATETIME (UTC) |  | Represents the instant at which a decision was made to accept or decline a Transfer Center request. |
| 8 | `TC_PROV_DECLN_RSN_C_NAME` | VARCHAR | org | The decline reason category ID that specifies why a provider declined a Transfer Center request. |
| 9 | `ADMT_PROV_YN` | VARCHAR |  | Indicates whether this decision was also where the provider was decided to be the admitting provider for the resultant encounter of the Transfer Center request. 'Y' indicates that the provider will be the admitting provider. 'N' indicates that the provider will not be the admitting provider. |
| 10 | `ASSOCIATED_CALL_ID` | VARCHAR |  | The ID of the call record on which a decision was made. |
| 11 | `CURRENT_YN` | VARCHAR |  | Indicates whether this decision is current or has been overridden by a later decision. 'Y' indicates that this decision is still current, 'N' indicates that this decision has been overridden by a later one. |
| 12 | `LOC_IS_REF_YN` | VARCHAR |  | This indicates whether the decision was made for the referring facility of the Transfer Center request before a referring facility was actually entered. 'Y' indicates that this decision was made for the referring facility. 'N' indicates that this decision was not made for the referring facility. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

