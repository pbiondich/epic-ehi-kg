# ORDER_RES_OT

> This table stores tracked recommendation information and Blood result dispense status for orders-related results. This table can also store Dermatology Skin Findings.

**Primary key:** `FINDING_ID`, `CONTACT_DATE_REAL`  
**Columns:** 20  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique ID of the finding record corresponding to this result. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `REC_STATUS_C_NAME` | VARCHAR | org | The recommendation status category ID for a result finding. |
| 5 | `ADMINPX_ORD_DAT` | VARCHAR |  | A unique contact date in decimal format from which the corresponding order's tracked result originated. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 6 | `ADMINPX_BLOODSTAT_C_NAME` | VARCHAR | org | The blood product status history category ID for the order, as sent via a results interface from a blood bank. |
| 7 | `LESION_REMOVE_CMT` | VARCHAR |  | The comments entered by the user when a lesion was removed from a patient's record. |
| 8 | `LAST_DOC_DTTM` | DATETIME (UTC) |  | The date and time when this finding was last documented on. |
| 9 | `LESION_REMOVE_RSN_C_NAME` | VARCHAR | org | The removal reason category ID for the lesion. |
| 10 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 11 | `NOTE_ID` | VARCHAR | shared | The unique ID of the note associated with this finding. |
| 12 | `REGION_ID` | NUMERIC |  | The unique ID of the anatomic region where a finding was placed. |
| 13 | `REGION_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 14 | `BACKGROUND_AVATAR_C_NAME` | VARCHAR |  | The avatar image category ID that was showing when the result finding was placed onto a location on the body. |
| 15 | `DERM_FINDING_COUNT` | INTEGER |  | The number of findings in this result finding record. Allows user to document like findings in the same anatomical region under one result finding record |
| 16 | `FINDING_LOC_SUFFIX` | VARCHAR | discont. | This items stores a suffix string that was added by the user to make a finding location unique. |
| 17 | `FINDING_LOC_NAME` | VARCHAR |  | This items stores an override name string that was added by the user to make a finding location unique. |
| 18 | `GROUP_NOTE_ID` | VARCHAR |  | The unique ID of the group note associated with this finding. |
| 19 | `PLAN_NOTE_ID` | VARCHAR |  | The unique ID of the plan note associated with this finding. |
| 20 | `FOLLOWUP_RESP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

