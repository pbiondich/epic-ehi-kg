# DOCS_RCVD_FAM_HX_PROB

> This table stores discrete family history problem information received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 18  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `FAMILY_PROB_REFID` | VARCHAR |  | The unique ID of the family member's problem for this row. |
| 6 | `FAMILY_PROB_ID_C_NAME` | VARCHAR | org | The category ID of the family member's problem for this row. |
| 7 | `FAM_MMB_PROB_NAME` | VARCHAR |  | The display name of the family member's problem for this row. |
| 8 | `FAM_MMB_PROB_ONSAGE` | INTEGER |  | The age of onset for the family member's problem for this row. |
| 9 | `FAM_PROB_EFF_TIME_DTTM` | DATETIME (Attached) |  | The date and time at which the family member's problem for this row was observed. |
| 10 | `FAMILY_MEMBER_REFID` | VARCHAR |  | The unique ID of the family member for this row. This column is frequently used to link to the DOCS_RCVD_FAM_HX_MEM table. |
| 11 | `FAM_PRB_PERT_NEG_YN` | VARCHAR |  | The value that determines whether the problem for this row is a pertinent negative for the family member. |
| 12 | `FAM_MEMPROB_COD_YN` | VARCHAR |  | The value that determines whether the problem for this row was a cause of death for the family member. |
| 13 | `FAM_PROB_COMMENTS` | VARCHAR |  | Comments left for the problem in this row. |
| 14 | `FAM_PROB_PAT_HX_RESP_C_NAME` | VARCHAR |  | The value that indicates the response the patient gave for a given family history problem. |
| 15 | `FAM_MEMPROB_ONSET_AGE_END` | INTEGER |  | End of range for family member problem age of onset. |
| 16 | `FAM_MEMPROB_LINKED_DX` | INTEGER |  | Stores the diagnosis ID linked to a family history problem. |
| 17 | `FAM_MMB_PROB_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 18 | `FAM_MMB_PROB_NKP_YN` | VARCHAR |  | If the family member problem represents "No Known Problems" for the family member, then this item is set to Yes. If it is not representing no known problems, then this item is set to No or left empty. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

