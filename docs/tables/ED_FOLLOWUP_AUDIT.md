# ED_FOLLOWUP_AUDIT

> Each record in ED_FOLLOWUP_AUDIT corresponds to a patient's edited follow-up information -- i.e. information for where and when a patient was told to follow up with other providers. This table does not include the current follow-up information.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this edit. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the deployment owner for this contact. |
| 6 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 7 | `CONTACT_INFO` | VARCHAR |  | The contact information for the patient's follow-up. |
| 8 | `SUMMARY` | VARCHAR |  | A summary of the patient contact. |
| 9 | `EDIT_COUNT` | NUMERIC |  | Stores the number of units (days/weeks/months) for follow up associated with this contact. |
| 10 | `ED_FUP_UNIT_TYPE_C_NAME` | VARCHAR |  | Stores whether patient has to follow-up in days/weeks/months or on a specific day. |
| 11 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 12 | `ED_FU_PRN_USED_C_NAME` | VARCHAR |  | This column shows a 1 if there is something written in the comments field. |
| 13 | `ED_FU_PRN_TEXT` | VARCHAR |  | The free text entry from the comments field for providers to enter any other information they deem important. |
| 14 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 15 | `ED_FU_OTHER` | VARCHAR |  | The free text entry that contains with whom the patient should follow up. |
| 16 | `ED_FUP_HOW_C_NAME` | VARCHAR |  | Stores how the patient should follow up (Call, Make an appointment, etc.). |
| 17 | `USER_ID` | VARCHAR | FK→ | The unique ID associated with the user record who entered this follow-up information. |
| 18 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 19 | `ED_FU_INST` | DATETIME (Local) |  | The date and time when this follow-up information was filed. |
| 20 | `ED_FUEDIT_DATE` | DATETIME |  | Stores the history of the follow-up dates entered for an encounter. |
| 21 | `ED_FUEDIT_ADDR_KEY` | VARCHAR |  | The edit trail for the ED Follow Up Provider Address Key. |
| 22 | `IP_FUEDIT_ORD_ID` | NUMERIC |  | The edit trail of the follow-up provider order IDs specified for the encounter |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

