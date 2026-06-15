# RXA_RESPONSE_COB

> The response Coordination of Benefits (COB) section received from the payer.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the adjudication record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `I_OT_PYR_CVG_TYPE` | VARCHAR |  | Code identifying the type of Other Payer ID (340-7C). |
| 6 | `I_OT_PYR_QUAL_ID` | NUMERIC |  | NCPDP code qualifying the Other Payer ID (340-7C). |
| 7 | `I_OT_PYR_QUAL_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 8 | `I_OT_PYR_ID` | VARCHAR |  | A unique ID assigned to the Other Payer. |
| 9 | `I_OT_PYR_PCN` | VARCHAR |  | A unique ID assigned to each non-primary payer (secondary, tertiary, etc.) |
| 10 | `I_OT_PYR_CARDH_ID` | VARCHAR |  | Cardholder ID for this member that is associated with the Payer noted. |
| 11 | `I_OT_PYR_GROUP_ID` | VARCHAR |  | A unique ID assigned to the cardholder group or employer group by a non-primary payer (secondary, tertiary, etc.) |
| 12 | `I_OT_PYR_PERS_CODE` | VARCHAR |  | A unique code assigned by the other payer to a specific person within a family. |
| 13 | `I_OT_PYR_HLP_DSK_PH` | VARCHAR |  | The phone number for the Other Payer's help desk. |
| 14 | `I_OT_PYR_PAT_REL_ID` | NUMERIC |  | NCPDP code assigned by the other payer to indicate the relationship of patient to cardholder. |
| 15 | `I_OT_PYR_PAT_REL_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 16 | `I_OT_PYR_BEN_EFF_DT` | DATETIME |  | The Other Payer's effective date of the patient's benefits. |
| 17 | `I_OT_PYR_BEN_TR_DT` | DATETIME |  | The Other Payer's termination date of the patient's benefits. |
| 18 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

