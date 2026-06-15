# RXA_NCPDP_OVERRIDE

> National Council for Prescription Drug Programs (NCPDP) override values during prescription claims adjudication.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the adjudication record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `OVR_NCPDP_FIELD` | VARCHAR |  | The override NCPDP field to be sent out during prescription adjudication. |
| 6 | `OVR_NCPDP_VALUE` | VARCHAR |  | The override NCPDP value to be sent out during prescription adjudication. |
| 7 | `OVR_NCPDP_PARENT` | VARCHAR |  | Override NCPDP parent fields to be sent out during prescription adjudication. When a user enters an override value for an NCPDP field and that NCPDP field is part of a counter, the system automatically populates this column with the field ID of the counter parent. If the field being overridden is part of a double-counter (such as in the COB segment), this column stores both counters, the parent of the field, and the parent of that parent. For example, if 431-DV is overridden with 10.00, RXA 1220 stores 341-HB, 337-4C. |
| 8 | `OVR_NCPDP_PRN_COUNT` | INTEGER |  | The parent counter for the NCPDP override. For a field under a single counter, this does not apply. For a field that is under a double counter (e.g. 363-2H Compound Ingredient Modifier Code in the Compound segment), this is the index of main counter (e.g. for compounds, this indicates which ingredient it is). |
| 9 | `OVERRIDE_SEGMENT` | VARCHAR |  | The NCPDP segment that the override field belongs to. |
| 10 | `OVR_NCPDP_CTR_IDX` | INTEGER |  | The counter index for the NCPDP override. For a field under a single counter, this is the index for that field. For a field under a double counter (e.g. 363-2H Compound Ingredient Modifier Code in the Compound segment), this is also the index for that field. For example, if there are two values for field 363-2H for the third ingredient in the compound, then this item tracks the index for these two values. That is, item 1230 will have a value of 3 (for the third ingredient), item 1225 will have a value of 1 for the first 363-2H value, and a value of 2 for the second 363-2H value. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

