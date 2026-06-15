# DOCS_RCVD_CARE_TEAMS

> External Care Team information.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CTM_REFERENCE_ID` | VARCHAR |  | Reference ID of an external care team member. |
| 6 | `CTM_PCP_TYPE_ID_C_NAME` | VARCHAR | org | Care Team Member PCP Type ID which links to the internal Care Team Member PCP Type. |
| 7 | `CTM_PCPTYPE_RELATIONSHIP_NAME` | VARCHAR |  | Care Team Member's functional role. This value is a string that might be the display name of the mapped value from an external system. This value could also be the name of the original value from an external system before it was mapped. The actual mapped values are found in Care Team Member PCP Type and Relationship to Patient. |
| 8 | `CTM_RELATIONSHIP_ID_C_NAME` | VARCHAR | org | The ID for the Care Team Member's relationship to patient that maps to an internal relationship to patient value. |
| 9 | `CTM_EFFECT_DTTM` | DATETIME (Local) |  | Care team member effective or start date. |
| 10 | `CTM_TERM_DTTM` | DATETIME (Local) |  | Care team member termination or end date. |
| 11 | `CTM_SOURCE_DXR_CSN` | NUMERIC |  | The contact serial number of the received document which contains the Care Team Member data. |
| 12 | `CTM_HIST_STATUS_C_NAME` | VARCHAR |  | This item indicates whether the care team member is current or historical or a more specific subset of historical. |
| 13 | `CTM_HIST_DATE` | DATETIME |  | This item stores the date that the historical status for this care team member is valid through. After this date, the historical status needs to be rechecked. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

